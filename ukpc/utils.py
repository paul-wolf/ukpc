import sys
import csv
import time
import re
import traceback
import argparse

from __init__ import parse_pc, PostCode

"""
https://www.doogal.co.uk/PostcodeDownloads.php
"""

areas = set()
districts = set()
sectors = set()
units = set()

def iterate_file(path, verbose=True, print_regex=None, stats=False, callback=None):

    with open(path, 'r') as csvfile:
        pcreader = csv.reader(csvfile)
        i = 0
        for row in pcreader:
            try:
                pc_str = row[0]
                if not i == 0: # skip header
                    pc = PostCode(pc_str)
                    if callback and callable(callback):
                        callback(pc)
                    if print_regex:
                        if re.match(print_regex, pc_str):
                            print(pc_str, str(pc))
                    if stats:
                        areas.add(pc.area)
                        districts.add(pc.fdistrict)
                        sectors.add(pc.fsector)
                        units.add(pc.unit)
                i += 1

                if verbose and not i % 10000:
                    print(i)
            except Exception as e:
                traceback.print_exc()
                print(e)
                print("row: {}, {}".format(i, pc_str))
                print(pc)
                return



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="File path of csv with first column is a postcode")
    parser.add_argument("--regex", help="A regex to search for; print each occurance", action="store")
    parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("--stats", help="print stats at end", action="store_true")
    args = parser.parse_args()

    start = time.time()
    iterate_file(args.path, 
                 verbose=args.verbose, 
                 print_regex=args.regex,
                 stats=args.stats)
    print("time in secs: {}".format(int(time.time() - start)))

    if args.stats:
        print("areas: {}".format(len(areas)))
        print("districts: {}".format(len(districts)))
        print("sectors: {}".format(len(sectors)))
        print("units: {}".format(len(units)))
