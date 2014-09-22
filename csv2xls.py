#!/usr/bin/python

from __future__ import print_function
import openpyxl
import csv, os, argparse

def parse_args():
	parser = argparse.ArgumentParser(description = 'Convert a csv file to'
			+ ' xlsx format. The converted file will be placed next to the given'
			+ ' file')
	parser.add_argument('file',
			help = 'the csv file to convert')
	parser.add_argument('-e', '--encoding',
			default = 'latin1',
			help = 'the character encoding of the given file')
	return parser.parse_args()


def build_dst_filename(path):
	# get the file path without the extension
	base_path = os.path.splitext(path)[0]
	return base_path + ".xlsx"


def convert(path, encoding):
	workbook = openpyxl.Workbook()
	sheet = workbook.active

	with open(path) as f:
		reader = csv.reader(f)

		for row_idx, row in enumerate(reader):
			for col_idx, col in enumerate(row):
				# read cell with the given encoding and encode it back to utf-8
				cell_val = unicode(col, encoding).encode('utf-8')
				sheet.cell(row = row_idx + 1, column = col_idx + 1).value = cell_val

	return workbook


def main():
	args = parse_args()

	workbook = convert(args.file, args.encoding)
	workbook.save(build_dst_filename(args.file))


if __name__ == '__main__':
	main()
