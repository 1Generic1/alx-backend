#!/usr/bin/env python3
"""
    Calculate the start and end indices for a
    given page in a paginated dataset.
"""


def index_range(page, page_size):
    """
    Calculate the start and end indices for a
    given page in a paginated dataset.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1
    return start_index, end_index
