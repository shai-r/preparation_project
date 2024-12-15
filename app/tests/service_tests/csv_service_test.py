import pytest

from app.services.csv_service import read_data_from_csv


def test_read_csv_existing_file():
    path = r"C:\\Users\\user\\PycharmProjects\\proj_data\\app\\sources\\reviews_with_students.csv"
    batches = list(read_data_from_csv(path, batch_size=10))

    assert len(batches) > 0

    for batch in batches[:-1]:
        assert len(batch) == 10
    assert len(batches[-1]) <= 10

    assert isinstance(batches[0][0], dict)