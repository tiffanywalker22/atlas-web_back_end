#!/usr/bin/env python3
"""Implement a get_hyper_index method with two integer arguments:
index with a None default value and page_size with
default value of 10"""

from typing import Optional, Dict, List
import csv

class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Function that returns a dictionary with deletion-resilient
        hyperlinked pagination data"""
        assert isinstance(index, int) and isinstance(page_size, int) and \
            index >= 0 and page_size > 0

        indexed_dataset = self.indexed_dataset()
        max_index = len(indexed_dataset) - 1
        index = min(index, max_index)

        data = []
        next_index = index

        while len(data) < page_size and next_index <= max_index:
            if indexed_dataset.get(next_index):
                data.append(indexed_dataset[next_index])
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index if next_index <= max_index else None,
        }
