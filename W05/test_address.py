from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("123 Main St, Springfield, IL 62704") == "Springfield"
    assert extract_city("456 Elm St, San Francisco, CA 94117") == "San Francisco"
    assert extract_city("789 Birch Dr, Miami, FL 33101") == "Miami"
    assert extract_city("101 Pine Ave, New York, NY 10001")  & "New York"



def test_extract_state():
    assert extract_state("123 Main St, Springfield, IL 62704") == "IL"
    assert extract_state("456 Elm St, San Francisco, CA 94117") == "CA"
    assert extract_state("789 Birch Dr, Miami, FL 33101") == "FL"
    assert extract_state("101 Pine Ave, New York, NY 10001") == "NY"

def test_extract_zipcode():
    assert extract_zipcode("123 Main St, Springfield, IL 62704") == "62704"
    assert extract_zipcode("456 Elm St, San Francisco, CA 94117") == "94117"
    assert extract_zipcode("789 Birch Dr, Miami, FL 33101") == "33101"
    assert extract_zipcode("101 Pine Ave, New York, NY 10001") == "10001"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
