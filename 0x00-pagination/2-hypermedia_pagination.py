#!/usr/bin/env python3
"""
    Calculate the start and end indices for a
    given page in a paginated dataset.
"""
import csv
import math
from typing import List
from math import ceil


def index_range(page, page_size):
    """
    Calculate the start and end indices for a
    given page in a paginated dataset.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Calculate the start and end indices for a
        given page in a paginated dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset_length = len(self.dataset())
        total_pages = ceil(dataset_length / page_size)

        if page > total_pages:
            return []
        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index+1]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieve metadata about the dataset pagination.
        """
        page_data = self.get_page(page, page_size)
        dataset_length = len(self.dataset())
        total_pages = math.ceil(dataset_length / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
