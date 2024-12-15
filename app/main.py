from time import sleep

from app.services.csv_service import read_data_from_csv
from app.services.json_service import process_teachers_in_batches, read_json

path = r"C:\\Users\\user\\PycharmProjects\\proj_data\\app\\sources\\reviews_with_students.csv"
path_j = r"C:\\Users\\user\\PycharmProjects\\proj_data\\app\\sources\\academic_network.json"

if __name__ == '__main__':
    for batch in process_teachers_in_batches(read_json(path_j)):
        for record in batch:
            print(record)
        sleep(10)
    for batch in read_data_from_csv(path):
        for record in batch:
            print(record)
        sleep(10)