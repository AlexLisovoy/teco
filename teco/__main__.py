import argparse
import os
import time
from pathlib import Path
import operator

from .terms_counter import TermsCounter


ARGS = argparse.ArgumentParser(description="Term counter")
ARGS.add_argument('file', help='file with terms')
ARGS.add_argument('folder',
                  help='folder with files, which contains text for counting')
ARGS.add_argument(
    '--num', action='store', type=int, metavar='N', default=0,
    help='show N most frequently occurring terms (default: all)')


def main():
    args = ARGS.parse_args()
    start_time = time.time()

    with open(args.file, 'r') as fp:
        counter = TermsCounter(fp.read().splitlines())

    result = (0 for _ in range(len(counter.terms_list)))

    for item in Path(os.path.abspath(args.folder)).glob('**/*'):
        if item.is_file():
            with item.open() as fp:
                result = map(operator.add, result,
                             counter.compute_occurrences_count(fp.read()))

    result = sorted(zip(counter.get_terms(), result),
                    key=operator.itemgetter(1),
                    reverse=True)
    if args.num:
        result = result[:args.num]
    for term, count in result:
        print("{}:\t {}".format(term, count))

    print("{}\nTime: {:4f} sec".format('-' * 30, time.time() - start_time))


if __name__ == '__main__':
    main()
