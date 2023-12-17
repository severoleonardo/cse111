# Output

This section describes the output generated by the data collection and processing steps.

**Data Format:**

* The processed data is stored in a pandas DataFrame object.
* The DataFrame contains columns like "Data", "Quantidade", and "Valor".
* The date format is YYYY-MM-DD.
* The "Quantidade" and "Valor" columns are formatted with commas and currency symbols.

**Data Saving:**

* The formatted data is saved to a CSV file with a unique filename based on the current date.
* This allows for easy access and analysis of the data outside the Python environment.

**Additional Notes:**

* Users can specify a custom output directory for the saved CSV file.
* The script provides options to control the format and decimal places for specific data columns.

**Example Output:**

Date        Quantity  Value
2023-10-26       1000,00 R$10.000,00
2023-10-27       2000,00 R$20.000,00
2023-10-28       3000,00 R$30.000,00