# Banco Central Money Data Collector
Welcome!

This repository houses a Python script that facilitates the collection and processing of money circulation data from the Banco Central do Brasil API.

**Project Goals:**

* Provide a user-friendly tool for accessing and analyzing Brazilian money circulation data.
* Enhance the data retrieval process with features like date range selection and data formatting.
* Offer a straightforward command-line interface for effortless script execution.

**Key Functionalities:**

* Retrieve data for specified date ranges: pinpoint the desired timeframe for your analysis.
* Process and format data for enhanced analysis: manage data cleaning, formatting, and preparation for further manipulation.
* Save processed data to CSV files: export the data to a readily accessible format for analysis outside the script.
* Command-line interface for convenient execution: utilize date range and other options as arguments for effortless script execution.

**Getting Started:**

1. Clone or download this repository.
2. Install the required libraries: `requests`, `pandas`, `logging`, `coloredlogs`, and `datetime`.
3. Open a terminal and navigate to the project directory.
4. Execute the script with your desired date range:
*Bash:  python main.py --start_date 2023-01-01 --end_date 2023-02-28*

**Documentation:**

* API Usage: provides detailed information on interacting with the Banco Central API.
* Data Processing: explains how retrieved data is processed and formatted.
* Output: describes the generated data format and saving options.
* Command-line Arguments: guides you through utilizing the command-line interface.

**Additional Resources:**

* Banco Central API Documentation: https://dadosabertos.bcb.gov.br/dataset/dinheiro-em-circulao/resource/03906f0c-6c5e-4fda-aa03-6b571cbc9753
* Operators - $Filter: https://olinda.bcb.gov.br/olinda/servico/ajuda
* Python Pandas Documentation: https://pandas.pydata.org/docs/

**Contribution:**

We welcome contributions to this project by:

Reporting any bugs or issues encountered.
Suggesting new features or improvements.
Contributing code changes or pull requests.
We hope this tool assists you in analyzing Brazilian money circulation data with ease and efficiency. Please reach out if you have any questions or feedback.