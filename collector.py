import argparse
import os
import shutil
import sys
import logging
from tqdm import tqdm

__author__ = "Miguel Angel Salinas Gancedo"
__copyright__ = "Simur"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

files_to_copy = []

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
        "-dr",
        "--destination-root",
        required=True,
        dest="destination_root",
        help="Destination root folder",
    ) 
    parser.add_argument(
        "-in",
        "--include-extensions",
        type=parse_extensions,
        required=True,
        help="Include files extensions",
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

def filter_files(args):
    for root, dirs, files in os.walk(args.source_root):
        for file in files:
            if any(file.endswith(ext) for ext in args.include_extensions):
                source_file = os.path.join(root, file)
                relative_path = os.path.relpath(source_file, start=args.source_root)
                destination_file = os.path.join(args.destination_root, relative_path)
                files_to_copy.append((source_file, destination_file))

    return files_to_copy

def copy_files(files_to_copy):
    with tqdm(total=len(files_to_copy), unit="file") as pbar:
        for source_file, destination_file in files_to_copy:
            pbar.set_description(f"Copying: {os.path.basename(source_file)}")
            os.makedirs(os.path.dirname(destination_file), exist_ok=True)
            shutil.copy2(source_file, destination_file)
            pbar.update(1)

_logger.info("Starting collector python module ...")

args = parse_args(sys.argv[1:])
setup_logging(args.loglevel)

_logger.info("Filering files to be copied ...")
files_to_copy = filter_files(args)

_logger.info("Copying files ...")
copy_files(files_to_copy)

_logger.info("Ending collector python module ...")