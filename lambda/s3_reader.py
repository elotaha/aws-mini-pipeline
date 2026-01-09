import csv
import os

def read_csv():
    script_dir = os.path.dirname(__file__)  
    csv_path = os.path.join(script_dir, '../sample_data/example.csv')
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)

if __name__ == "__main__":
    read_csv()
