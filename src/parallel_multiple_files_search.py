"""
Module containing the ParallelMultiFileSearch
"""
from typing import List
from src.result import Result

class ParallelMultiFileSearch:
    """
    Class representing a parallel search (with context) for a string in multiple files.
    The main idea is use parallel programming to search into multiple files simultaneously
    """
    def __init__(self, context: int = 0) -> None:
        """
        Initializes the ParallelMultiFileSearch class with a given amount of lines to be shown in the result before and after the match

        Parameters:
            context - represents the amount of lines to be included in the context. Default is 1
        """
        pass

    def search(self, string: str, file_paths: List[str], output_file_paths: List[str]):
        """
        Searches for `string` in the files located at `file_paths`.
        A match is defined the following way: if `string` is seen as a substring in a line of the file,
            e.g. the string "own" will match with "the quick brown fox".
        
        Splits the input file into N parts and searches in parallel in those N parts.
        Searches in parallel in each of the files.

        Saves the matches (represented as Result objects) into separate files, located at output_file_paths

        Parameters:
            string - the string to search for
            file_paths - the paths to the files to search into
            output_file_path - the paths to the files that will contain the matches

        Exceptions:
            If one of `file_path` does not exist, raise FileNotFoundError
        """ 

        pass