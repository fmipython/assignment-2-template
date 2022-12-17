import os
import time
from src.parallel_multiple_files_search import ParallelMultiFileSearch
from src.result import Result

def test_multi_file_functionality_no_context():
    # Arrange
    search = ParallelMultiFileSearch(0)

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
    search.search(string_to_search, [file_path], [output_file_path])

    with open(output_file_path) as file_descriptor:
        content = file_descriptor.readlines()

    content = [line.strip() for line in content]

    # Assert

    for expected_result in expected_results:
        assert str(expected_result) in content


def test_multi_file_substring_search_no_context():
    # Arrange
    search = ParallelMultiFileSearch(0)

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
    search.search(string_to_search, [file_path], [output_file_path])

    with open(output_file_path) as file_descriptor:
        content = file_descriptor.readlines()

    content = [line.strip() for line in content]
    
    # Assert

    for expected_result in expected_results:
        assert str(expected_result) in content
    

def test_multi_file_non_existing_file():
    # Arrange
    search = ParallelMultiFileSearch(0)
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


def test_multi_file_functionality_context():
    # Arrange
    search = ParallelMultiFileSearch(2)

    file_path = os.path.join('tests', 'input.txt')
    string_to_search = 'super'

    expected_line_numbers = [10]
    expected_columns = [14]
    expected_lines = ["We'll have a super time."]

    expected_context_before = [
        ["You can just push a little tree out of your brush like that.", "Even the worst thing we can do here is good."]
    ]

    expected_context_after = [
        ['Every time you practice, you learn more.', "We'll play with clouds today."]
    ]

    output_file_path = os.path.join('tests', 'output_context.txt')

    expected_results = [Result(file_path, line_number, column, line, context_before, context_after)
        for line_number, column, line, context_before, context_after in zip(expected_line_numbers, expected_columns, expected_lines, expected_context_before, expected_context_after)
    ]

    # Act 
    search.search(string_to_search, [file_path], [output_file_path])

    with open(output_file_path) as file_descriptor:
        content = file_descriptor.readlines()

    content = [line.strip() for line in content]

    # Assert

    for expected_result in expected_results:
        for line in str(expected_result).split('\n'):
            assert line in content

def test_multi_file_parallelism():
    # Arrange
    single_search = ParallelMultiFileSearch()
    two_search = ParallelMultiFileSearch()
    four_search = ParallelMultiFileSearch()

    file_path = os.path.join('tests', 'input2.txt')
    string_to_search = 'violence'


    # Act
    single_start = time.time()
    single_search.search(string_to_search, [file_path], ['output2.txt'])
    single_end = time.time()
    single_duration = single_end - single_start

    two_start = time.time()
    two_search.search(string_to_search, [file_path] * 2, ['output2_1_2.txt', 'output2_2_2.txt'])
    two_end = time.time()
    two_duration = two_end - two_start

    four_start = time.time()
    four_search.search(string_to_search, [file_path] * 4, ['output2_1_4.txt', 'output2_2_4.txt', 'output2_3_4.txt', 'output2_4_4.txt'])
    four_end = time.time()
    four_duration = four_end - four_start
    
    with open("output2.txt") as file_descriptor:
        first_lines = file_descriptor.readlines()

    with open("output2_1_2.txt") as file_descriptor:
        second_lines = file_descriptor.readlines()

    with open("output2_1_4.txt") as file_descriptor:
        four_lines = file_descriptor.readlines()

    # Assert
    assert single_duration * 2 > two_duration
    assert two_duration * 2 > four_duration
    assert len(first_lines) == len(second_lines) == len(four_lines) == 547
    assert first_lines == second_lines
    assert first_lines == four_lines