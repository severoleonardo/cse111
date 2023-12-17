import pytest
import pandas as pd
from unittest.mock import MagicMock, patch
from prove_milestone import (
    ls_make_api_request,
    ls_validate_date,
    ls_process_data,
    ls_format_data,
    ls_main,
)

# Replace 'money_circulation' with the actual name of your script without the ".py" extension

@pytest.fixture
def mock_api_response():
    return {
        "value": [
            {"Quantidade": 1000, "Valor": 2000},
            {"Quantidade": 1500, "Valor": 3000},
            # Add more sample data as needed
        ]
    }

@patch('requests.get')
def test_ls_make_api_request(mock_get, mock_api_response):        
    mock_get.reset_mock()
    mock_get.return_value = MagicMock(ok=True, json=lambda: mock_api_response)

    skip_index = 0
    start_date = '2023-01-01'
    end_date = '2023-01-05'

    response = ls_make_api_request(skip_index, start_date, end_date)

    assert response == mock_api_response
    mock_get.assert_called_once_with(
        f"https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?"
        f"$top=10000&$skip={skip_index}&$orderby=Data%20desc&$format=json&$filter=Data%20ge%20{start_date}%20and%20Data%20le%20{end_date}"
    )

def test_ls_validate_date():
    valid_date_str = '2023-01-01'
    invalid_date_str = 'invalid_date'

    assert ls_validate_date(valid_date_str) is True

    with pytest.raises(ValueError, match="Invalid start date. Minimum allowed date is .*"):
        ls_validate_date(invalid_date_str)

def test_ls_process_data(mock_api_response):
    data_frame = ls_process_data(mock_api_response)

    assert 'Quantidade' in data_frame.columns
    assert 'Valor' in data_frame.columns
    assert len(data_frame) == len(mock_api_response['value'])

def test_ls_format_data(tmp_path, mock_api_response):
    data_frame = ls_process_data(mock_api_response)
    formatted_data = ls_format_data(data_frame)

    assert 'Quantidade' in formatted_data.columns
    assert 'Valor' in formatted_data.columns

    csv_path = tmp_path / "test_data.csv"
    formatted_data.to_csv(csv_path, index=False)
    assert csv_path.is_file()
    assert pd.read_csv(csv_path).equals(formatted_data)