#!/usr/bin/env python3
"""Implement a method named get_page that takes two integer arguments page
with default value 1 and page_size with default value 10"""
import csv
from typing import List

class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Function that paginates the dataset based on given parameters"""
        assert isinstance(page, int) and isinstance(page_size, int) and \
            page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]


def index_range(page: int, page_size: int) -> tuple:
    """Function that calculates start and end index for pagination"""
    return (page_size * (page - 1), page_size * page)
