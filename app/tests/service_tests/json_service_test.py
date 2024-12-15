import pytest
import json
from unittest.mock import patch, mock_open
from app.services.json_service import read_json, batch_data, process_teachers_in_batches, process_classes_in_batches, process_relationships_in_batches

mock_data = {
    "teachers": [
        {"id": "CS-9416", "name": "Jeffery Arnold", "department": "Computer Science"},
        {"id": "CS-7315", "name": "Stephen Lozano", "department": "Computer Science"},
    ],
    "classes": [
        {"id": "CS-515", "course_name": "Computer Science 101", "section": 1},
        {"id": "CS-516", "course_name": "Computer Science 102", "section": 1},
    ],
    "relationships": [
        {"id": "R-001", "teacher_id": "CS-9416", "class_id": "CS-515"},
        {"id": "R-002", "teacher_id": "CS-7315", "class_id": "CS-516"},
    ]
}

@pytest.fixture
def mock_open_file():
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        yield

def test_read_json(mock_open_file):
    data = read_json("C:\\Users\\user\\PycharmProjects\\proj_data\\app\\sources\\academic_network.json")
    assert data["teachers"] == mock_data["teachers"]
    assert data["classes"] == mock_data["classes"]
    assert data["relationships"] == mock_data["relationships"]

def test_batch_data():
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    batches = list(batch_data(data_list, batch_size=5))
    assert len(batches) == 3  # ישנם 3 באטצ'ים
    assert batches[0] == [1, 2, 3, 4, 5]
    assert batches[1] == [6, 7, 8, 9, 10]
    assert batches[2] == [11]

def test_process_teachers_in_batches(mock_open_file):
    data = read_json("C:\\Users\\user\\PycharmProjects\\proj_data\\app\\sources\\academic_network.json")
    batches = list(process_teachers_in_batches(data, batch_size=1))  # נבדוק אם יש פיצול לבאטצ'ים בגודל 1
    assert len(batches) == 2
    assert batches[0] == [{"id": "CS-9416", "name": "Jeffery Arnold", "department": "Computer Science"}]
    assert batches[1] == [{"id": "CS-7315", "name": "Stephen Lozano", "department": "Computer Science"}]

def test_process_classes_in_batches(mock_open_file):
    data = read_json("C:\\Users\\user\\PycharmProjects\\proj_data\\app\\sources\\academic_network.json")
    batches = list(process_classes_in_batches(data, batch_size=1))  # נבדוק אם יש פיצול לבאטצ'ים בגודל 1
    assert len(batches) == 2  # יהיו 2 באטצ'ים
    assert batches[0] == [{"id": "CS-515", "course_name": "Computer Science 101", "section": 1}]
    assert batches[1] == [{"id": "CS-516", "course_name": "Computer Science 102", "section": 1}]

def test_process_relationships_in_batches(mock_open_file):
    data = read_json("C:\\Users\\user\\PycharmProjects\\proj_data\\app\\sources\\academic_network.json")
    batches = list(process_relationships_in_batches(data, batch_size=1))  # נבדוק אם יש פיצול לבאטצ'ים בגודל 1
    assert len(batches) == 2  # יהיו 2 באטצ'ים
    assert batches[0] == [{"id": "R-001", "teacher_id": "CS-9416", "class_id": "CS-515"}]
    assert batches[1] == [{"id": "R-002", "teacher_id": "CS-7315", "class_id": "CS-516"}]
