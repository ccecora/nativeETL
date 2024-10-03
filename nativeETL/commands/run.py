from csv import DictReader
from pathlib import Path

from ..utilities.validations import verify_file_type
from ..utilities.warnings import check_file_size

DATA_HOME = Path("nativeETL/data")

def run_pipeline(config, data):
    verify_file_type(data, [".csv"])

    src_file_location = DATA_HOME/data

    check_file_size(src_file_location)
    with open(src_file_location) as src_file:
        mapped_rows = list(DictReader(src_file))

    # Test
    for row in mapped_rows:
        print(row)