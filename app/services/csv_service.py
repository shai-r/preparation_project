import csv

def read_data_from_csv(path: str, batch_size: int = 10):
    with open(path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        batch = []
        for row in csv_reader:
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch