# ID3 Encoding Fixer
ID3 Encoding Fixer converts encoding of ID3 tags in MP3 files to the right one.

## Dependencies
* chardet
* mutagen


## Usage
### Install dependencies
```
$ pip install chardet mutagen
```
### Run if encoding is unknown.
```
$ python3 -m ief -R /path/to/mp3
```
Or, you can also specify an encoding type.
```
$ python3 -m ief -R -e euc-kr /path/to/mp3
```
