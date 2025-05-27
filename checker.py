import argparse
import csv
import os
import shutil
import sys
import logging
from tqdm import tqdm

__author__ = "Miguel Angel Salinas Gancedo"
__copyright__ = "Simur"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

files_to_check = []

def parse_extensions(ext_string):
    # Split by comma, strip whitespace, ensure each starts with dot, and make a set
    return {ext.strip() if ext.strip().startswith('.') else '.' + ext.strip()
            for ext in ext_string.split(',')}

def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="BIN to CSV Converter")

    parser.add_argument(
        "-sr",
        "--source-root",
        required=True,
        dest="source_root",
        help="Source root folder",
    )
    parser.add_argument(
        "-df",
        "--destination-file",
        required=True,
        dest="destination_file",
        help="Destination file",
    )                 
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )

    return parser.parse_args(args)

def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )

def get_files(args):
    for root, dirs, files in os.walk(args.source_root):
        for file in files:           
            files_to_check.append((os.path.basename(root), file))            

    files_ordered = sorted(files_to_check, key=lambda x: x[0])

    return files_ordered

def check_files(args, files_to_check):
    with open(args.destination_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(files_to_check)       

_logger.info("Starting checker ...")

args = parse_args(sys.argv[1:])
setup_logging(args.loglevel)

_logger.info("Get files to be checked ...")
files_to_check = get_files(args)

_logger.info("Check files ...")
check_files(args, files_to_check)

_logger.info("Ending checker ...")