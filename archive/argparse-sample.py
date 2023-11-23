import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", required=True, help="something here")
parser.add_argument("-f", required=True, help="csv filename path")
parser.add_argument("-d", required=False, help="something here")
args = parser.parse_args()
#call
#args.o
#args.f
org_name = args.o
