from src.result import Result

def test_result_str_method_no_context():
    # Arrange
    filename = "foo.txt"
    line_number = 7
    column = 5
    line = "The quick brown fox"

    result = Result(filename, line_number, column, line, [], [])

    expected_representation = f'{filename}:{line_number}:{column}:{line}'

    # Act 
    actual_representation = str(result)

    # Assert
    assert actual_representation == expected_representation


def test_result_str_method_context():
    # Arrange
    filename = "foo.txt"
    line_number = 7
    column = 5
    line = "The quick brown fox"
    context_before = ['Foo', 'Bar']
    context_after = ['Bar', 'Baz']
    
    result = Result(filename, line_number, column, line, context_before, context_after)

    expected_representation = f'{filename}:{line_number - 2}:{context_before[0]}\n'
    expected_representation += f'{filename}:{line_number - 1}:{context_before[1]}\n'
    expected_representation += f'{filename}:{line_number}:{column}:{line}\n'
    expected_representation += f'{filename}:{line_number + 1}:{context_after[0]}\n'
    expected_representation += f'{filename}:{line_number + 2}:{context_after[1]}'

    # Act 
    actual_representation = str(result)

    # Assert
    assert actual_representation == expected_representation
    