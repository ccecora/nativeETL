import yaml
import csv


with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)


with open('example.csv', mode='r') as file:
    # Create a DictReader object
    csv_reader = csv.DictReader(file)