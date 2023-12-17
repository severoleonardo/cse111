# Banco Central Money Data Collector

This documentation provides an overview of the Python code used to collect and process money circulation data from the Banco Central do Brasil API.

**Features:**

* Retrieves data for specified date ranges.
* Processes and formats the data for better analysis.
* Saves the processed data to CSV files.
* Offers command-line interface for easy execution.

**Getting Started:**

1. Install required libraries: `requests`, `pandas`, `logging`, `coloredlogs`, `datetime`
2. Clone or download this repository.
3. Open a terminal and navigate to the project directory.
4. Run the script with the desired date range: `python main.py --start_date 2023-01-01 --end_date 2023-02-28`

**Documentation:**

* README: [Code Documentation](README.md)
* API Usage: [API Documentation](api/make_api_request.md)
* Data Processing: [Data Processing](processing/data_processing.md)
* Output: [Output](output/data_saving.md)

