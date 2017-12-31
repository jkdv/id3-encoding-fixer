# ID3 Encoding Fixer
ID3 Encoding Fixer converts encoding of ID3 tags in MP3 files to the right one.


## Usage
### Install dependencies
```
$ pip install -r requirements.txt
```
### Run if encoding is unknown.
```
$ python3 -m ief -R /path/to/mp3
```
Or, you can also specify an encoding type.
```
$ python3 -m ief -R -e euc-kr /path/to/mp3
```
