# Your Name: Leonardo Severo Elias  
# Date: 12/07/2023
# Purpose of the Assignment: [Brief description of the assignment's objective]
# Sources Used: [List any external sources or references used in your code]

import requests
import pprint
import pandas as pd
import logging
import coloredlogs
import os
from datetime import datetime

# Set up logging configurationlogging
logging.basicConfig(level=logging.INFO) 
coloredlogs.install(fmt="(levelname)s: %(message)s")

def make_api_request(skip, start_date, end_date):
    """
    Makes a request to the Banco Central API for money circulation data within a specified date range and skip index.

    Args:
        skip: The number of data points to skip for pagination (default = 0).
        start_date: The starting date for data retrieval in YYYY-MM-DD format.
        end_date: The ending date for data retrieval in YYYY-MM-DD format.

    Returns:
        A dictionary containing the retrieved data and metadata, or raises an exception if the request fails.
    """

    # Construct the API request URL with filters and skip index
    link = f"https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$skip={skip}&$orderby=Data%20desc&$format=json&$filter=Data%20ge%20{start_date}%20and%20Data%20le%20{end_date}"
    response = requests.get(link)
    
    # Send the request and handle potential errors
    try:
        response = requests.get(link)
        response.raise_for_status()
        data = response.json()
        logging.info(f"Retrieved data successfully for skip index: {skip}")
    except Exception as e:
        logging.error(f"Error fetching data for skip index: {skip}", exc_info=True)
        raise e
    
    # Return the retrieved data
    return response.json()

def process_data(data):
    """
    Converts the retrieved JSON data into a pandas DataFrame for further processing.

    Args:
        data: The dictionary containing the JSON data from the API response.

    Returns:
        A pandas DataFrame containing the parsed and processed data.
    """

    # Extract the data value from the JSON structure
    data_value = data.get('value', [])

    # Convert the data into a DataFrame
    data_frame = pd.DataFrame(data_value)

    # Return the processed DataFrame
    return data_frame

def format_data(data_frame):
    """
    Formats the "Quantidade" and "Valor" columns for improved readability and presentation.

    Args:
        data_frame: The pandas DataFrame containing the processed data.

    Returns:
        The formatted pandas DataFrame with updated column values.
    """

    # Check if the DataFrame is empty
    if not data_frame.empty:
        # Format "Quantidade" with commas for thousands separators
        data_frame["Quantidade"] = data_frame["Quantidade"].map("{:,}".format)
        
        # Format "Valor" with currency symbol and decimal places
        data_frame["Valor"] = data_frame["Valor"].map("R${:,.2f}".format)

        # Generate a filename with the current date
        today = datetime.today().strftime("%Y-%m-%d")
        filename = f"money_in_circulation_{today}.csv"
        
        # Try saving the formatted data to a CSV file
        try:
            data_frame.to_csv(filename, index=False)
            logging.info(f"Data saved successfully to file: {filename}")
        except Exception as e:
            logging.error(f"Error saving data to file: {filename}", exc_info=True)
            raise e
    
    # Return the formatted DataFrame
    return data_frame

def main():
    """
    Orchestrates the entire data collection and processing process.

    1. Iteratively retrieves data for specified date range with skip indexing.
    2. Processes and concatenates the retrieved data into a single DataFrame.
    3. Formats the final DataFrame with improved column presentation.
    4. Prints the formatted DataFrame to the console.
    5. Saves the formatted data to a CSV file.
    """
    
    # Initialize variables for data accumulation
    table_final = pd.DataFrame()
    skip_index = 0 

    # Loop through data retrieval based on date range
    while True:
        # Make API request
        data = make_api_request(skip_index, start_date, end_date)
                
        # Check if no more data
        if len(data.get('value', [])) < 1:
            break
        
        # Process and concatenate the DataFrame
        table = process_data(data)
        table_final = pd.concat([table_final, table])
        
        # Update skip index for the next iteration
        skip_index += 10000

    # Format the final table
    formatted_table = format_data(table_final)

    # Print the formatted table
    pprint.pprint(formatted_table)

    # Create directory before saving if it doesn't exist
    os.makedirs("data", exist_ok=True)
    formatted_table.to_csv("data/money_in_circulation.csv", index=False)
    logging.info("Data saved successfully to CSV file.")

if __name__ == "__main__":
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    main()
