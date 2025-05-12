#!/usr/bin/env python3
"""Module to implement deletion-resilient hypermedia pagination
"""


import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names and ensure
       that it is resilient to deletions between queries.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Caching for dataset and indexed dataset
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches the dataset from the CSV file

           Returns:
              List[List]: returns the dataset as a list of rows.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Creates a dict where the key is the original index and the value
           is the row.

           Returns:
              Dict[int, List]: A dict mapping indexes to dataset rows
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                    i: row for i, row in enumerate(dataset)
                    }
        return self.__indexed_dataset

    def get_hyper_index(
            self,
            index: int = None,
            page_size: int = 10) -> Dict[str, Any]:
        """Returns a page of the dataset starting from a specific index,
           accounting for deletions so data is not skipped between queries.

           Args:
              index (int): Starting index.
              page_size (int): Number of records to return.

           Returns:
              Dict[str, Any]: Dictionary with keys: index, next_index,
              page_size, data.
        """
        assert isinstance(index, int) and index >= 0
        indexed_data = self.indexed_dataset()
        assert index < max(indexed_data.keys())

        data = []
        current = index

        while len(data) < page_size and current < len(self.__dataset):
            if current in indexed_data:
                data.append(indexed_data[current])
            current += 1

        return {
            "index": index,
            "next_index": current,
            "page_size": len(data),
            "data": data
        }
