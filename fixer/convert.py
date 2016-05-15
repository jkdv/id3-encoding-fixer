import glob
import os

import chardet
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError


class ConvertException(Exception):
    pass


def fix_save_batch(path, encoding=None, recursive=False):
    assert isinstance(path, str)
    assert isinstance(encoding, str) or encoding is None

    if os.path.isdir(path) and not recursive:
        pathlist = glob.glob(os.path.join(path, '*.mp3'), recursive=recursive)
        for p in sorted(pathlist):
            fix_save(p, encoding)

    elif os.path.isdir(path) and recursive:
        for dirpath, dirnames, filenames in os.walk(path):
            for name in filenames:
                fullpath = os.path.join(dirpath, name)
                _, extension = os.path.splitext(fullpath)
                if extension.lower() != '.mp3':
                    continue
                fix_save(fullpath, encoding)

    elif os.path.isfile(path):
        fix_save(path, encoding)

    else:
        raise ConvertException('Path given is not a file nor a directory.')


def fix_save(path, encoding):
    assert isinstance(path, str)
    assert isinstance(encoding, str) or encoding is None
    if not os.path.isfile(path):
        raise ConvertException('Path given is not a file.')

    try:
        audio = EasyID3(path)
    except ID3NoHeaderError:
        label = 'NO ID3'
    else:
        label = 'SUCCESS'

        for tag, values in audio.items():
            fixed_values = list()
            for value in values:
                try:
                    decoded_text = convert_encoding(value, encoding)
                except UnicodeEncodeError:
                    continue
                except UnicodeDecodeError:
                    continue
                fixed_values.append(decoded_text)

            if len(fixed_values) > 0:
                audio[tag] = fixed_values

        try:
            audio.save()
        except IOError:
            label = 'FAIL'

    print_msg(label, path)


def convert_encoding(text, encoding=None):
    assert isinstance(text, str)

    try:
        raw = text.encode(encoding='cp1252')
    except UnicodeEncodeError as e:
        raise e

    if encoding is None:
        exaggerated_raw = raw
        for i in range(10):
            exaggerated_raw += raw
        detected = chardet.detect(exaggerated_raw)
        encoding = detected['encoding']

        try:
            decoded_text = raw.decode(encoding=encoding)
        except UnicodeDecodeError as e:
            raise e

    else:
        assert isinstance(encoding, str)
        decoded_text = raw.decode(encoding=encoding)

    return decoded_text


def print_msg(msg1, msg2):
    print('{:8s} {:72s}'.format(msg1, msg2))
