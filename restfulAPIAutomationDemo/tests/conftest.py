from pytest import fixture

url = "https://api.football-data.org/v4"
url2 = "http://universities.hipolabs.com"
url3 = "https://jsonplaceholder.typicode.com"


@fixture(scope='function')
def area_resource():
    return f"{url}/areas"


@fixture(scope='function')
def player_resource():
    return f"@{url}/players"


@fixture(scope='function')
def header():
    return {"X-Auth-Token": "1234"}


@fixture(scope='function')
def united_kingdom_university_list_resource():
    return f"{url2}/search?country=United+Kingdom"


@fixture(scope='function')
def json_typicode_resource():
    return f"{url3}/posts"


@fixture(scope='function')
def body():
    return {"userID": 1,
            "id": 1,
            "title": "Making a POST request",
            "body": "This is the data we created."}
