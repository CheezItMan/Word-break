from word_break.word_break import word_break


def test_example_one():
    # Arrange
    s = "adadevelopersacademy"
    word_dict = set(["ada", "developers", "academy"])
    # Act
    answer = word_break(s, word_dict)

    # Assert
    assert answer


def test_example_two():
    # Arrange
    s = "applepenapple"
    word_dict = set(["apple", "pen"])
    # Act
    answer = word_break(s, word_dict)

    # Assert
    assert answer


def test_example_three():
    # Arrange
    s = "catsandog"
    word_dict = set(["cats", "dog", "sand", "and", "cat"])
    # Act
    answer = word_break(s, word_dict)

    # Assert
    assert not answer
