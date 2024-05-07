#!/usr/bin/env python3
"""Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary containing the following
key-value pairs:
page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer"""

import csv
import math
from typing import List, Optional, Union


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Function that returns a dictionary with hyperlinked
        pagination data"""
        assert isinstance(page, int) and isinstance(page_size, int) and \
            page > 0 and page_size > 0

        dataset_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper_data = {
            "page_size": len(dataset_page),
            "page": page,
            "data": dataset_page,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return hyper_data


def index_range(page: int, page_size: int) -> tuple:
    """Function that calculates start and end index for pagination"""
    return (page_size * (page - 1), page_size * page)
