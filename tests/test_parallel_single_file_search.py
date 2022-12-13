import os
import time
from src.parallel_single_file_search import ParallelSingleFileSearch
from src.result import Result

def test_functionality():
    # Arrange
    search = ParallelSingleFileSearch(1)

    file_path = os.path.join('tests', 'input.txt')
    string_to_search = 'time'

    expected_line_numbers = [10, 11]
    expected_columns = [20, 7]
    expected_lines = [
        "We'll have a super time.",
        "Every time you practice, you learn more."
    ]

    output_file_path = os.path.join('tests', 'output.txt')

    expected_results = [Result(file_path, line_number, column, line, [], [])
        for line_number, column, line in zip(expected_line_numbers, expected_columns, expected_lines)
    ]

    # Act 
    search.search(string_to_search, file_path, output_file_path)

    with open(output_file_path) as file_descriptor:
        content = file_descriptor.readlines()

    content = [line.strip() for line in content]

    # Assert

    for expected_result in expected_results:
        assert str(expected_result) in content


def test_substring_search():
    # Arrange
    search = ParallelSingleFileSearch(1)

    file_path = os.path.join('tests', 'input.txt')
    string_to_search = 'ti'

    expected_line_numbers = [3, 7, 10, 11, 11]
    expected_columns = [16, 18, 20, 7, 20]
    expected_lines = [
        "Isn't it fantastic that you can change your mind and create all these happy things?",
        "Isn't that fantastic?",
        "We'll have a super time.",
        "Every time you practice, you learn more.",
        "Every time you practice, you learn more."
    ]

    output_file_path = os.path.join('tests', 'output.txt')

    expected_results = [Result(file_path, line_number, column, line, [], [])
        for line_number, column, line in zip(expected_line_numbers, expected_columns, expected_lines)
    ]

    # Act 
    search.search(string_to_search, file_path, output_file_path)

    with open(output_file_path) as file_descriptor:
        content = file_descriptor.readlines()

    content = [line.strip() for line in content]
    
    print(content)
    # Assert

    for expected_result in expected_results:
        assert str(expected_result) in content
    

def test_non_existing_file():
    # Arrange
    search = ParallelSingleFileSearch(1)
    is_exception_thrown = False

    # Act
    non_existing_file_path = 'non_existing_file_path.txt'
    string_to_search = 'ti'
    try:
        search.search(string_to_search, non_existing_file_path, 'output.txt')
    except FileNotFoundError as ex:
        is_exception_thrown = True

    # Assert
    assert is_exception_thrown


def test_parallelism():
    # Arrange
    single_search = ParallelSingleFileSearch(1)
    two_search = ParallelSingleFileSearch(2)
    four_search = ParallelSingleFileSearch(4)

    file_path = os.path.join('tests', 'input3.txt')
    string_to_search = 'violence'


    # Act
    single_start = time.time()
    single_search.search(string_to_search, file_path, 'output3.txt')
    single_end = time.time()
    single_duration = single_end - single_start

    two_start = time.time()
    two_search.search(string_to_search, file_path, 'output3.txt')
    two_end = time.time()
    two_duration = two_end - two_start

    four_start = time.time()
    four_search.search(string_to_search, file_path, 'output3.txt')
    four_end = time.time()
    four_duration = four_end - four_start

    # Assert
    assert single_duration > two_duration
    assert two_duration > four_duration
