#! /usr/bin/env python
import csv
from argparse import ArgumentParser
from sanskrit_parser import Parser
from itertools import islice
from indic_transliteration import sanscript

    

def conll_tests(conll_file):
    # CONLL files are treated as tsv
    print(conll_file.name)
    treader = csv.reader(conll_file, delimiter='\t')
    tl = []
    for row in treader:
        if len(row):
            tl.append(row[1])
        elif tl:
            yield tl
            tl = []
    if tl:
        yield tl
            
def parse_test(parser, test, conll_writer=None, max_splits=1, max_parses=1):
    written = False
    for si, split in enumerate(parser.split(" ".join(test),
                                                  limit=max_splits,
                                                  pre_segmented=True)):
        print(f'Lexical Split: {split}')
        for pi, parse in enumerate(split.parse(limit=max_parses)):
            print(f'Parse {pi} : (Cost = {parse.cost})')
            print(f'{parse}')
            if conll_writer is not None:
                for line in parse.to_conll():
                    conll_writer.writerow(line)
                conll_writer.writerow([])
                written = True
            if pi > 8:
                break
    if not written and conll_writer is not None:
        for i,t in enumerate(test):
            conll_writer.writerow([i+1, t, "_",
                                   ["unknown"], "0", "unknown"])
        conll_writer.writerow([])
    return None



if __name__ == "__main__":
    def getArgs(argv=None):
        # Parser Setup
        parser = ArgumentParser(description='CONLL Reader')
        # String to encode
        parser.add_argument('files', nargs="+", type=str)
        parser.add_argument('-o', '--output', type=str)
        parser.add_argument('-n', '--num-tests', type=int, default=5)
        args = parser.parse_args(argv)
        return args

    def main(args):
        parser = Parser(input_encoding=sanscript.SLP1,
                        strict_io=False,
                        output_encoding=sanscript.SLP1,
                        replace_ending_visarga=None,
                        score=False,
                        split_above=5,
                        lexical_lookup="combined")
        with open(args.output, "wt") as of:
            cwriter = csv.writer(of, delimiter='\t')
            for fname in args.files:
                print(fname)
                with open(fname, "rt") as f:
                    for test in islice(conll_tests(f), args.num_tests):
                        print(f"Test: {test}")
                        print("\n")
                        parse_test(parser, test, conll_writer=cwriter)

    main(getArgs())
