import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from prove_milestone import ls_make_api_request, ls_validate_date, ls_process_data, ls_format_data, ls_main

@patch('requests.get')
def test_ls_make_api_request(mock_get):
    mock_get.return_value.json.return_value = {'value': []}
    result = ls_make_api_request(0, '2022-01-01', '2022-01-31')
    assert result == {'value': []}

def test_ls_validate_date():
    assert ls_validate_date('2022-01-01') == True
    assert ls_validate_date('1994-10-03') == True
    with pytest.raises(ValueError):
        ls_validate_date('1994-10-02')
    with pytest.raises(ValueError):
        ls_validate_date('2023-01-01')

def test_ls_process_data():
    data = {'value': [{'Data': '2022-01-01', 'Quantidade': 1000, 'Valor': 5000}]}
    result = ls_process_data(data)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1

def test_ls_format_data():
    data_frame = pd.DataFrame([{'Data': '2022-01-01', 'Quantidade': 1000, 'Valor': 5000}])
    result = ls_format_data(data_frame)
    assert result['Quantidade'][0] == '1,000'
    assert result['Valor'][0] == 'R$5,000.00'

@patch('builtins.input', side_effect=['2022-01-01', '2022-01-31'])
@patch('prove_milestone.ls_make_api_request')
@patch('prove_milestone.ls_process_data')
@patch('prove_milestone.ls_format_data')
def test_ls_main(mock_format_data, mock_process_data, mock_make_api_request, mock_input):
    mock_make_api_request.return_value = {'value': []}
    mock_process_data.return_value = pd.DataFrame()
    mock_format_data.return_value = pd.DataFrame()
    ls_main()
    assert mock_input.call_count == 2
    assert mock_make_api_request.called
    assert mock_process_data.called
    assert mock_format_data.called