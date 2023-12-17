# Data Processing

This section explains how the code processes and formats the retrieved data from the API.

**Function:** `process_data(data)`

* This function converts the JSON data returned by the API into a pandas DataFrame.
* It handles cleaning and manipulating the data for further analysis.
* The function returns a formatted pandas DataFrame ready for further processing or saving.

**Function:** `format_data(data_frame)`

* This function formats specific columns like "Quantidade" and "Valor" for better presentation.
* It adds commas for thousands separators and currency symbols.
* Additionally, this function saves the formatted data to a CSV file with a unique filename based on the current date.

**Example Usage:**

```python
df = process_data(data)

formatted_df = format_data(df)

print(formatted_df)