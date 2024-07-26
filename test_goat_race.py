from goat_race import goat_race

def test_returns_a_dictionary():
    expected = {}
    result = goat_race("")
    assert result == expected