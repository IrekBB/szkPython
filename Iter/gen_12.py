"""
Przykłady zastosowania generatorów z życia wzięte
Oto, co się tu dzieje: 
1. read_large_csv czyta plik linia po linii, tworząc każdy wiersz jako słownik.  
2. filter_by_region filtruje wiersze na podstawie określonego regionu.
3. Potok przetwarza dane przyrostowo, unikając przeciążenia pamięci.
"""

def read_large_csv(file_path):
    """ Generator to read a large CSV file line by line."""
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row
def filter_by_region(data,region):
    """ Generator to filter rows by a specific region."""
    for row in data:
        if row["category"]==region:
            yield row

def main(args):
    # Generator pipeline
    file_path = "sales_data.csv"
    category = "Electronics"
    data = read_large_csv(file_path)
    filtered_data = filter_by_region(data, category)
    
    # Process the filtered data
    for record in filtered_data:
        print(record)

if __name__=="__main__":
    import sys
    import csv
    sys.exit(main(sys.argv))