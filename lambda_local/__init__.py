'''
python-lambda-local: Main module

Copyright 2015-2017 HDE, Inc.
Licensed under MIT.
'''

from __future__ import print_function
import argparse
import sys
from multiprocessing import Process
import pkg_resources

from .main import run


__version__ = pkg_resources.require("python-lambda-local")[0].version


def main():
    args = parse_args()

    print(args.version)
    return

    p = Process(target=run, args=(args,))
    p.start()
    p.join()

    sys.exit(p.exitcode)


def parse_args():
    parser = argparse.ArgumentParser(description="Run AWS Lambda function" +
                                     " written in Python on local machine.")
    parser.add_argument("file", metavar="FILE", type=str,
                        help="lambda function file name")
    parser.add_argument("event", metavar="EVENT", type=str,
                        help="event data file name")
    parser.add_argument("-l", "--library", metavar="LIBRARY_PATH",
                        type=str, help="path of 3rd party libraries")
    parser.add_argument("-f", "--function", metavar="HANDLER_FUNCTION",
                        type=str, default="handler",
                        help="lambda function handler name, \
default: \"handler\"")
    parser.add_argument("-t", "--timeout", metavar="TIMEOUT", type=int,
                        default=3,
                        help="seconds until lambda function timeout, \
default: 3")
    parser.add_argument("-a", "--arn-string", metavar="ARN_STRING", type=str,
                        default="", help="ARN string for lambda function")
    parser.add_argument("-v", "--version-name", metavar="VERSION_NAME",
                        type=str, default="",
                        help="lambda function version name")

    parser.add_argument("--version", action="version",
                        version="%(prog)s " + __version__,
                        help="print the version of python-lambda-local and exit")

    return parser.parse_args()


if __name__ == "__main__":
    main()
