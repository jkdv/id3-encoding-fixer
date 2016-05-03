import glob
import os

import chardet
from mutagen.easyid3 import EasyID3


class ConvertException(Exception):
    pass


def fix_save_batch(path, recursive=False):
    assert isinstance(path, str)

    if os.path.isdir(path):
        pathlist = glob.glob(os.path.join(path, '*.mp3'), recursive=recursive)
        for p in sorted(pathlist):
            fix_save(p)
    elif os.path.isfile(path):
        fix_save(path)
    else:
        raise ConvertException('Path given is not a file nor a directory.')


def fix_save(path):
    assert isinstance(path, str)
    if not os.path.isfile(path):
        raise ConvertException('Path given is not a file.')

    audio = EasyID3(path)
    for tag, values in audio.items():
        fixed_values = list()
        for value in values:
            try:
                raw = value.encode(encoding='cp1252')
                exaggerated_raw = raw
                assert isinstance(raw, bytes)
                for i in range(10):
                    exaggerated_raw += raw
            except UnicodeEncodeError:
                continue

            detected = chardet.detect(exaggerated_raw)
            confidence = detected['confidence']
            encoding = 'EUC-KR'
            if confidence > 0.8:
                encoding = detected['encoding']

            try:
                decoded_text = raw.decode(encoding=encoding)
            except UnicodeDecodeError:
                continue

            fixed_values.append(decoded_text)

        if len(fixed_values) > 0:
            audio[tag] = fixed_values

    try:
        audio.save()
        print_msg('SUCCESS', path)
    except IOError:
        print_msg('FAIL', path)


def print_msg(msg1, msg2):
    print('{:8s} {:72s}'.format(msg1, msg2))
