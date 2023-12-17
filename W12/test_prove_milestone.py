import pytest
import pandas as pd
from datetime import datetime, timedelta
from prove_milestone import ls_make_api_request, ls_validate_date, ls_process_data, ls_format_data
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
    requests_mock.get(requests_mock.ANY, json=sample_api_response)
    
    # Perform the API request
    response = ls_make_api_request(0, '2023-12-01', '2023-12-02')
    
    # Check if the response matches the sample data
    assert response == sample_api_response

def test_ls_make_api_request_failure(requests_mock):
    # Mock the requests library to simulate a failed API response
    requests_mock.get(requests_mock.ANY, status_code=404)
    
    # Check if ls_make_api_request raises an exception on failure
    with pytest.raises(Exception):
        ls_make_api_request(0, '2023-12-01', '2023-12-02')

def test_ls_validate_date_valid():
    # Test ls_validate_date with a valid date
    assert ls_validate_date('2023-12-01') == True

def test_ls_validate_date_invalid_format():
    # Test ls_validate_date with an invalid date format
    assert ls_validate_date('12/01/2023') == False

def test_ls_validate_date_invalid_start_date():
    # Test ls_validate_date with a start date before the minimum allowed date
    assert ls_validate_date('1994-10-02') == False

def test_ls_validate_date_invalid_end_date():
    # Test ls_validate_date with an end date greater than today
    future_date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    assert ls_validate_date(future_date) == False

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
    with pytest.raises(Exception):
        ls_format_data(pd.DataFrame(sample_api_response['value']))

# Add more tests as needed for other functions and edge cases