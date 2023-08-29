import requests
from pytest import mark
from tests.conftest import area_resource


@mark.area
class AreaTests:
    def test_good_request_for_areas(self, area_resource):
        # url = "https://api.football-data.org/v4/areas" - url included in the conftest file
        response = requests.get(area_resource)
        assert response.status_code == 200

    def test_bad_request_for_areas(self, area_resource, header):
        # url = "https://api.football-data.org/v4/areas" - url included in the conftest file
        # header = {"X-Auth-Token": "12356"}
        response = requests.get(area_resource, headers=header)
        assert response.status_code == 400

    def test_verify_area_information(self, area_resource):
        """null = None in a dictionary with null can be set in the method/function"""
        null = None
        url = area_resource + "/2000"
        response = requests.get(url)
        actual_response_body = response.json()
        expected_response = dict({"id": 2000, "name": "Afghanistan", "code": "AFG", "flag": null, "parentAreaId": 2014,
                                  "parentArea": "Asia", "childAreas": []
                                  })
        assert expected_response == actual_response_body

    def test_verify_wrong_area_information(self, area_resource):
        url = area_resource + "/2000"
        null = None
        response = requests.get(url)
        actual_response_body = response.json()
        expected_response = dict({"id": 2000, "name": "Pakistan", "code": "PK", "flag": null, "parentAreaId": 2014,
                                  "parentArea": "Asia", "childAreas": []
                                  })
        assert expected_response != actual_response_body
