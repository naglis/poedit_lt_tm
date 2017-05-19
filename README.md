# poedit\_lt\_tm

This project contains a Python script for converting the Lithuanian translation
memory, available at
[Raštija.lt](https://www.raštija.lt/lokalizavimas/vertimo-atmintis/281), to PO
format, which can then be imported in [Poedit](https://poedit.net/).

All credits for the translation memory should go to its original authors.

## Usage

1. Download the latest PO file from
   [releases](https://github.com/naglis/poedit_lt_tm/releases).
2. In _Poedit_, go to _Edit &rarr; Preferences &rarr; TM_, click on _Learn From
   Files..._ and select the downloaded PO file.
3. The translation memory should now be available for use while translating.

## Converting

Note: the conversion script was written to work with Python 3.6.

1. Install _polib_:

```sh
pip install polib
```

2. Download the CSV version of the translation memory available at
   [Raštija.lt](https://www.raštija.lt/lokalizavimas/vertimo-atmintis/281),
   unzip the file.

3. Convert the unzipped CSV file to PO:

```sh
python tmcsv2po.py export.csv lt.po
```

## License

The conversion script is released into the public domain.
