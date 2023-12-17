import pytest
import pandas as pd
from prove_milestone import make_api_request, process_data, format_data

def test_make_api_request(mocker):
    # Mocking the requests.get function using pytest-mock
    mocker.patch('requests.get').return_value.json.return_value = {'value': [{'Quantidade': 1000, 'Valor': 2000}]}

    # Testing the function
    result = make_api_request(0)

    # Assertions
    assert result == {'value': [{'Quantidade': 1000, 'Valor': 2000}]}

def test_process_data():
    # Creating a sample JSON data
    sample_data = {'value': [{'Quantidade': 1000, 'Valor': 2000}, {'Quantidade': 1500, 'Valor': 2500}]}

    # Testing the function
    result = process_data(sample_data)

    # Assertions
    assert len(result) == 2
    assert result.iloc[0]['Quantidade'] == 1000
    assert result.iloc[1]['Valor'] == 2500

def test_format_data():
    # Creating a sample DataFrame
    data_frame = pd.DataFrame({'Quantidade': [1000, 2000], 'Valor': [3000, 4000]})

    # Testing the function
    result = format_data(data_frame)

    # Assertions
    assert result.iloc[0]['Quantidade'] == '1,000'
    assert result.iloc[1]['Quantidade'] == '2,000'
    assert result.iloc[0]['Valor'] == 'R$3,000.00'
    assert result.iloc[1]['Valor'] == 'R$4,000.00'

if __name__ == '__main__':
    pytest.main()
