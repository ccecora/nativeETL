from csv import DictReader

def run_pipeline(filename):
    
    

    with open(filename) as src_file:
        mapped_rows = DictReader(src_file)