import pytest
import pandas as pd
from requests_mock import ANY
from pytest import MonkeyPatch
from datetime import datetime, timedelta
from prove_milestone import ls_make_api_request, ls_validate_date, ls_process_data, ls_format_data, ls_main
import pytest


@pytest.fixture
def sample_api_response():
    # Provide a sample API response for testing ls_process_data function
    return {
        'value': [
            {'Quantidade': 10000, 'Valor': 5000.0, 'Data': '2023-12-01'},
            {'Quantidade': 15000, 'Valor': 7500.0, 'Data': '2023-12-02'}
        ]
    }

def test_ls_make_api_request_success(requests_mock, sample_api_response):
    # Mock the requests library to simulate a successful API response
    requests_mock.get(ANY, json=sample_api_response)
    
    # Perform the API request
    response = ls_make_api_request(0, '2023-12-01', '2023-12-02')
    
    # Check if the response matches the sample data
    assert response == sample_api_response

def test_ls_make_api_request_failure(requests_mock):
    # Mock the requests library to simulate a failed API response
    requests_mock.get(ANY, status_code=500)
    
    # Perform the API request
    response = ls_make_api_request(0, '2023-12-01', '2023-12-02')
    
    # Check if the response is None or an error message, depending on your implementation
    assert response is None
def test_ls_validate_date_valid():
    # Test ls_validate_date with a valid date
    assert ls_validate_date('2023-12-01') == True

def test_ls_validate_date_invalid_format():
    # Test ls_validate_date with an invalid date format
    assert ls_validate_date('12/01/2023') == False

def test_ls_validate_date_invalid_start_date():
    # Test ls_validate_date with a start date before the minimum allowed date
    with pytest.raises(ValueError, match="Invalid start date. Minimum allowed date is 1994-10"):
        ls_validate_date('1994-10-02') == False

def test_ls_validate_date_invalid_end_date():
    # Test ls_validate_date with an end date greater than today
    future_date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    with pytest.raises(ValueError, match="Invalid end date. Maximum allowed date is today."):
        ls_validate_date(future_date) == False

def test_ls_process_data(sample_api_response):
    # Test ls_process_data with a sample API response
    result = ls_process_data(sample_api_response)
    assert result.shape == (2, 3)  # Expecting 2 rows and 3 columns in the DataFrame

def test_ls_format_data(caplog, sample_api_response):
    # Test ls_format_data with a sample API response
    caplog.set_level('INFO')  # Capture log messages at INFO level
    
    # Ensure that the formatted data is saved successfully
    result = ls_format_data(pd.DataFrame(sample_api_response['value']))
    assert 'Data saved successfully to file' in caplog.text

    # Ensure that an error is logged if saving fails
    with pytest.raises(FileNotFoundError):
        ls_format_data(pd.DataFrame(sample_api_response['value']))

def test_ls_main(requests_mock):
    # Mock the requests library to simulate a successful API response
    sample_api_response = {
        'value': [
            {'Quantidade': 10000, 'Valor': 5000.0, 'Data': '2023-12-01'},
            {'Quantidade': 15000, 'Valor': 7500.0, 'Data': '2023-12-02'}
        ]
    }
    requests_mock.get(ANY, json=sample_api_response)

    # Mock user input for ls_main
    input_values = ['2023-12-01', '2023-12-02']
    input_mock = lambda _: input_values.pop(0)
    
    # Perform the ls_main function with mocked user input
    with MonkeyPatch.context() as m:
        m.setattr('builtins.input', input_mock)
        ls_main()

    # Add assertions to check the behavior of ls_main
    # For example, check if data is saved to file, printed to console, etc.

# Run the tests using pytest
if __name__ == '__main__':
    pytest.main()