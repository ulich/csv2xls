csv2xls
=======

A python script that converts a csv file to Excel format (.xlsx).

It was written with python 2.7 but may work with python 3.

## Instalation:

csv2xls requires openpyxl (https://bitbucket.org/openpyxl/openpyxl). The best way to install this is via virtualenv:

```
git clone https://github.com/ulich/csv2xls.git
cd csv2xls
virtualenv env
. env/bin/activate
pip install -r requirements.txt
python csv2xls.py -h
```

## Usage:

```
usage: csv2xls.py [-h] [-e ENCODING] file

Convert a csv file to xlsx format. The converted file will be placed next to
the given file

positional arguments:
  file                  the csv file to convert

optional arguments:
  -h, --help            show this help message and exit
  -e ENCODING, --encoding ENCODING
                        the character encoding of the given file
```
