from constants import URL, PATHS


def test_random_programing(get_json):
    random_response = get_json(URL, PATHS['random_path'])
    assert random_response.status_code, "Code 200 does not match"
    for response in random_response.json():
        assert response['type'] == "programming", "Type is not equal to programming"


def test_ten_jokes(get_json):
    programming_response = get_json(URL, PATHS['programming_path'])
    assert programming_response.status_code, "Code 200 does not match"
    assert len(programming_response.json()) == 10, "Jokes returned are not equal to 10"


def test_ten_programing(get_json):
    programming_response = get_json(URL, PATHS['programming_path'])
    assert programming_response.status_code, "Code 200 does not match"
    for response in programming_response.json():
        assert response['type'] == "programming", "Type is not equal to programming"
