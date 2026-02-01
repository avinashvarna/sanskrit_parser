#! /usr/bin/env python
import os
import csv
from argparse import ArgumentParser
from sanskrit_parser import Parser
from itertools import islice
from indic_transliteration import sanscript
import time

def conll_tests(conll_file):
    # CONLL files are treated as tsv
    treader = csv.reader(conll_file, delimiter='\t')
    tl = []
    for row in treader:
        if len(row) > 1:
            tl.append(row[1])
        elif tl:
            yield tl
            tl = []
    if tl:
        yield tl

def parse_test(parser, test, max_splits=1, max_parses=1):
    print(f"Testing: {' '.join(test)}")
    start = time.time()
    splits = list(parser.split(" ".join(test), limit=max_splits, pre_segmented=True))
    split_time = time.time() - start
    print(f"  Split took {split_time:.4f}s")

    for si, split in enumerate(splits):
        start_parse = time.time()
        parses = list(split.parse(limit=max_parses))
        parse_time = time.time() - start_parse
        print(f"  Split {si}: Parse took {parse_time:.4f}s")
        for pi, parse in enumerate(parses):
            print(f"    Parse {pi} cost: {parse.cost}")

def main():
    parser = ArgumentParser(description='Profile KISS Sanskrit Parser')
    parser.add_argument('files', nargs="+", type=str, help='CONLL files to process')
    parser.add_argument('-n', '--num-tests', type=int, default=1, help='Number of tests to run from each file')
    parser.add_argument('-s', '--skip', type=int, default=0, help='Number of tests to skip')
    parser.add_argument('--max-splits', type=int, default=1)
    parser.add_argument('--max-parses', type=int, default=1)
    parser.add_argument('--pyinstrument', action='store_true', help='Use pyinstrument for profiling')

    args = parser.parse_args()

    if args.pyinstrument:
        from pyinstrument import Profiler
        profiler = Profiler()
        profiler.start()

    parser_obj = Parser(input_encoding=sanscript.SLP1,
                        strict_io=False,
                        output_encoding=sanscript.SLP1,
                        replace_ending_visarga=None,
                        score=False,
                        split_above=5,
                        lexical_lookup="combined")

    for fname in args.files:
        print(f"Processing {fname}...")
        with open(fname, "rt") as f:
            tests = islice(conll_tests(f), args.skip, args.skip + args.num_tests)
            for i, test in enumerate(tests):
                print(f"Test Case {args.skip + i + 1}:")
                parse_test(parser_obj, test, max_splits=args.max_splits, max_parses=args.max_parses)

    if args.pyinstrument:
        profiler.stop()
        profiler.print()

if __name__ == "__main__":
    main()
