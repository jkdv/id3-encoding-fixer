#!/usr/bin/env python3
import argparse

from fixer import convert


def main():
    description = 'ID3 Tag Encoding Fixer'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-R', action='store_true', dest='recursive', help='Recursively fix all under the directory')
    parser.add_argument('path', nargs='?', metavar='<PATH>', help='Path to files or a directory')
    args = parser.parse_args()

    if args.path is None:
        parser.print_usage()
        exit()

    try:
        convert.fix_save_batch(args.path, args.recursive)
    except convert.ConvertException as e:
        parser.print_usage()
        print(e)


if __name__ == '__main__':
    main()
