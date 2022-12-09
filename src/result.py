"""
The result.py module contains the Result class, used for representing search results
"""

class Result:
    """
    Class representing the result from a search.
    Contains the file name, the line number of the match, the column from which the match starts, the line itself, and N amount of lines before and after the match.
    """

    def __init__(self) -> None:
        """
        Initializer of the Result class. 
        Arguments should be passed in the following order:
            filename, line number, column, line, context before and context after
        """
        pass

    def __str__(self) -> str:
        """
        Returns the string representation of the result, in the following format:
            For the lines before the match (if any): `<file_name>:<line_number>:<line>`
            For the match itself: `<file_name>:<line_number>:<column_number>:<line>`
            For the lines after the match (if any): `<file_name>:<line_number>:<line>`

        Example:
            tests/input.txt:4:Don't be afraid to make these big decisions.
            tests/input.txt:5:Once you start, they sort of just make themselves.
            tests/input.txt:6:11:Isn't that fantastic?
            tests/input.txt:7:You can just push a little tree out of your brush like that.
            tests/input.txt:8:Even the worst thing we can do here is good.
        """
        pass