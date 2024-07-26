from goat_race import first_place


def test_returns_dictionary_with_fastest_time_single() :
    expected = {"long-name": "00:30:00"}
    goats = {"long-name": "00:30:00"}
    result = first_place(goats)
    assert result == expected

def test_returns_dictionary_with_fastest_time_multiple() :
    goats = {"long-name": "00:30:00", "second-goat": "00:27:00"}
    expected = {"second-goat": "00:27:00"}
    result = first_place(goats)
    assert result == expected

def test_returns_dictionary_with_fastest_time_multiple_three() :
    goats = {"long-name": "00:30:00", "second-goat": "00:27:00", "another-goat": "01:50:34"}
    expected = {"second-goat": "00:27:00"}
    result = first_place(goats)
    assert result == expected

def test_returns_a_new_dictionary() :
    goats = {"long-name": "00:30:00"}
    result = first_place(goats)
    assert result is not goats

def test_does_not_mutate_input() :
    goats = {"long-name": "00:30:00", "second-goat": "00:45:00"}
    first_place(goats)
    assert goats == {"long-name": "00:30:00", "second-goat": "00:45:00"}