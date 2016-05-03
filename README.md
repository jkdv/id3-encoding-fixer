# ID3 Encoding Fixer

# Dependencies
* chardet
* mutagen


## Usage
### Install dependencies
$ pip install chardet mutagen <br>
### Run if encoding is unknown.
$ python3 -m ief -R /path/to/mp3 <br>
OR you can also specify an encoding type.<br>
$ python3 -m ief -R -e euc-kr /path/to/mp3
