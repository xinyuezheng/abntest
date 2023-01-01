from unittest.mock import patch
import pytest
from src.part2 import app
import sqlite3


@pytest.mark.parametrize(
    "country_code, expected_resp",
    [("NLD", {"status_code": 200, "response": [{"Age1stCodeYoungest": "Younger than 5 years", "Country Code": "NLD", "Country Name": "Netherlands"}]}),
     ("InvalidCountryCode", {"status_code": 200, "response": []}), ],
)
def test_get_start_coding_age(country_code, expected_resp):
    response = app.test_client().get(f'/startcoding/{country_code}')
    assert response.status_code == expected_resp['status_code']
    assert response.json == expected_resp["response"]


def test_get_start_coding_age_with_exception():
    error_code = "Fake Code"
    with patch('src.part2._query_db', side_effect=sqlite3.Error("DB Exception", error_code)):
        response = app.test_client().get(f'/startcoding/NLD')
        assert response.status_code == 500
        assert error_code in response.json['err_msg']
