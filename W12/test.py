import requests_mock
import pandas as pd
import pytest
from datetime import datetime
from unittest import mock
import os
from prove_milestone import ls_main
from prove_milestone import (
    ls_make_api_request,
    ls_validate_date,
    ls_process_data,
    ls_format_data,
)


def test_ls_make_api_request_success():
    # Mock successful API response
    data = {
        "value": [
            {"Data": "2023-12-08", "Quantidade": 10000, "Valor": 100000.00}
        ]
    }
    skip = 0
    start_date = "2023-12-08"
    end_date = "2023-12-08"

    # Mock requests.get
    with requests_mock.fixture() as mock_get:
        mock_get.get(
            "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$skip={}&$orderby=Data%20desc&$format=json&$filter=Data%20ge%20{}%20and%20Data%20le%20{}"
            .format(skip, start_date, end_date),
            json=data,
            status_code=200,
        )

        # Call the function and assert response
        response = ls_make_api_request(skip, start_date, end_date)
        assert response == data


def test_ls_make_api_request_error():
    # Mock error response
    skip = 0
    start_date = "2023-12-08"
    end_date = "2023-12-08"

    # Mock requests.get
    with requests_mock.fix() as mock_get:
        mock_get.get(
            "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$skip={}&$orderby=Data%20desc&$format=json&$filter=Data%20ge%20{}%20and%20Data%20le%20{}"
            .format(skip, start_date, end_date),
            status_code=404,
        )

        # Expect exception with message
        with pytest.raises(Exception) as e:
            ls_make_api_request(skip, start_date, end_date)
        assert "API request failed: 404" in str(e.value)


def test_ls_validate_date_valid():
    # Valid dates within range
    valid_dates = ["1994-11-01", "2023-12-09", datetime.today().strftime("%Y-%m-%d")]

    for date in valid_dates:
        assert ls_validate_date(date) is True


def test_ls_validate_date_invalid():
    # Invalid dates
    invalid_dates = ["2023-12-32", "1994-09-10", "invalid format"]

    for date in invalid_dates:
        assert ls_validate_date(date) is False


def test_ls_process_data_valid():
    # Mock data
    data = {
        "value": [
            {"Data": "2023-12-08", "Quantidade": 10000, "Valor": 100000.00}
        ]
    }

    # Call the function and assert DataFrame
    df = ls_process_data(data)
    assert list(df.columns) == ["Data", "Quantidade", "Valor"]
    assert df.iloc[0]["Data"] == "2023-12-08"
    assert df.iloc[0]["Quantidade"] == 10000
    assert df.iloc[0]["Valor"] == 100000.00


def test_ls_process_data_empty():
    # Mock empty data
    data = {"value": []}

    # Call the function and check for empty DataFrame
    df = ls_process_data(data)
    assert df.empty


def test_ls_format_data_success():
    # Mock data with valid values
    data = {
        "Data": ["2023-12-08"],
        "Quantidade": [10000],
        "Valor": [100000.00],
    }
    df = pd.DataFrame(data)

    # Call the function and assert formatted values
    formatted_df = ls_format_data(df)
    assert formatted_df["Data"].iloc[0] == "2023-12-08"
    assert formatted_df["Quantidade"].iloc[0] == "10.000"
    assert formatted_df["Valor"].iloc[0] == "R$100.000,00"


def test_ls_format_data_empty():
    # Mock empty DataFrame
    df = pd.DataFrame()

    # Call the function and expect same empty DataFrame
    formatted_df = ls_format_data(df)
    assert df.empty
    assert formatted_df.empty


def test_ls_main_success():
    # Mock user input with valid dates
    with mock.patch("builtins.input", side_effect=["1994-11-01", "2023-12-09"]):
        # Call the main function
        ls_main()

    # Assert file creation and data saving
    assert os.path.exists("data/money_in_circulation.csv")
    assert os.path.getsize("data/money_in_circulation.csv") > 0


def test_ls_main_error_invalid_date():
    # Mock user input with invalid date
    with mock.patch("builtins.input", side_effect=["invalid date"]):
        # Call the main function and expect ValueError
        with pytest.raises(ValueError):
            ls_main()

if __name__ == '__main__':
    pytest.main()


