#!/usr/bin/env python

import argparse
import csv
import datetime
import pathlib

import polib

DATETIME_FORMAT = '%Y-%m-%d %H:%M%z'


def main():
    parser = argparse.ArgumentParser(
        description='Convert translation memory CSV file to PO format',
    )

    parser.add_argument(
        'input_file',
        type=pathlib.Path,
        help='path to the translation memory CSV file',
    )
    parser.add_argument(
        'output_file',
        type=pathlib.Path,
        help='PO output file path',
    )
    parser.add_argument(
        '--input-encoding',
        default='utf-8-sig',
        help='input CSV file encoding. Default: %(default)s',
    )
    parser.add_argument(
        '--delimiter',
        default=';',
        help='CSV file delimiter. Default: %(default)s',
    )

    args = parser.parse_args()

    now = datetime.datetime.now()

    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': '1.0',
        'POT-Creation-Date': now.strftime(DATETIME_FORMAT),
        'PO-Revision-Date': now.strftime(DATETIME_FORMAT),
        'Language-Team': 'Lithuanian',
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-Transfer-Encoding': '8bit',
    }

    with open(args.input_file, encoding=args.input_encoding) as f:
        reader = csv.reader(f, delimiter=args.delimiter)

        for idx, row in enumerate(reader, start=1):
            msg_id, msg_str = row[:2]
            po.append(polib.POEntry(
                msgid=msg_id,
                msgstr=msg_str,
                occurrences=[(args.input_file.name, f'{idx}')],
            ))

    po.save(args.output_file)


if __name__ == '__main__':
    main()
