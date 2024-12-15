import json


import json

def read_json(path: str):
    with open(path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def batch_data(data_list, batch_size: int = 10):
    batch = []
    for item in data_list:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch

def process_teachers_in_batches(data: dict, batch_size: int = 10):
    teachers = data.get('teachers', [])
    return batch_data(teachers, batch_size)

def process_classes_in_batches(data: dict, batch_size: int = 10):
    classes = data.get('classes', [])
    return batch_data(classes, batch_size)

def process_relationships_in_batches(data: dict, batch_size: int = 10):
    relationships = data.get('relationships', [])
    return batch_data(relationships, batch_size)




