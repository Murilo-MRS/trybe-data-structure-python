import pytest
from ting_file_management.priority_queue import PriorityQueue

data_1 = {
    "nome_do_arquivo": "arquivo_1.txt",
    "qtd_linhas": 4,
    "linhas_do_arquivo": ["1", "2", "3", "4"],
}
data_2 = {
    "nome_do_arquivo": "arquivo_2.txt",
    "qtd_linhas": 5,
    "linhas_do_arquivo": ["5", "6", "7", "8", "9"],
}
data_3 = {
    "nome_do_arquivo": "arquivo_3.txt",
    "qtd_linhas": 5,
    "linhas_do_arquivo": ["10", "11", "12", "13", "14"],
}

mock_data = [data_1, data_2, data_3]


def test_basic_priority_queueing():
    priority_queue_test = PriorityQueue()

    priority_queue_test.enqueue(data_3)

    priority_queue_test.enqueue(data_2)

    priority_queue_test.enqueue(data_1)

    assert len(priority_queue_test) == 3

    assert priority_queue_test.search(0) == mock_data[0]

    priority_queue_test.dequeue()

    assert priority_queue_test.search(0) == mock_data[2]
    assert priority_queue_test.search(1) == mock_data[1]

    with pytest.raises(IndexError):
        priority_queue_test.search(-1)
