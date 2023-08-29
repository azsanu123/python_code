import requests
from pytest import mark


@mark.player
class PlayerTests:

    """test returning a 404 NotFound as the header/token/auth-key is invalid"""

    def test_get_player_information(self):
        url = "https://api.football-data.org/v4/players/44"
        header = {"X-Auth-Token": "1234"}
        response = requests.get(url, headers=header)
        assert response.status_code == 404

    def test_make_a_get_player_request_with_no_authorization(self):
        url = "https://api.football-data.org/v4/players/44"
        response = requests.get(url)
        assert response.status_code == 404

    def test_verify_player_information(self):
        url = "https://api.football-data.org/v4/players/44"
        header = {"X-Auth-Token": "1234"}
        response = requests.get(url, headers=header)
        actual_response_body = response.json()
        expected_response = dict({

        })
        assert actual_response_body == expected_response

