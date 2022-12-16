"""
Module containing the ParallelSingleFileSearch
"""
from src.result import Result

class ParallelSingleFileSearch:
    """
    Class representing a parallel search for a string in a file.
    The main idea is to split the file into multiple smaller parts and use parallel programming to search through it faster.
    """

    def __init__(self, workers: int = 1) -> None:
        """
        Initializes the MultithreadedSingleFileSearch class with a given amount (N) of workers for parallel search

        Parameters:
            workers - represents the amount of workers for the parallel search. Default is 1
        """
        pass

    def search(self, string: str, file_path: str, output_file_path: str):
        """
        Searches for `string` in the file located at `file_path`.
        A match is defined the following way: if `string` is seen as a substring in a line of the file,
            e.g. the string "own" will match with "the quick brown fox".
        
        Splits the input file into N parts and searches in paralel in those N parts.

        Saves the matches (represented as Result objects) into a single file, located at output_file_path

        Parameters:
            string - the string to search for
            file_path - the path to the file to search into
            output_file_path - the path to the file that will contain the matches

        Exceptions:
            If `file_path` does not exist, raise FileNotFoundError
        """

        pass
