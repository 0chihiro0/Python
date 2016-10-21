

import argparse

parser = argparse.ArgumentParser(description = 'Process of some integers')

parser.add_argument('integers', metavar='N', type=int, nargs='+', help='integers for the accumulate')
parser.add_argument('--sum', dest = 'accumulate', action='store_const', const=sum, default=max, help='sum the integer or find the max(fefault)')

args = parser.parse_args()
print(args.accumulate(args.integers))
