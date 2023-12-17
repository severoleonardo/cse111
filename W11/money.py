import requests
import pandas as pd
from datetime import date

# Function to get daily circulation data
def get_daily_circulation_data(date=None):
    """
    Retrieves daily money in circulation data from the Central Bank API.

    Args:
        date (str): Date for which data is requested (YYYY-MM-DD format).
                    If not specified, current date is used.

    Returns:
        dict: Dictionary containing daily money in circulation data.
    """
    # Define API endpoint
    url = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$skip=0&$orderby=Data%20desc&$format=json"

    # Add date parameter if specified
    if date:
        url += f"&dataIni={date}"

    # Make API request
    response = requests.get(url)

    # Check for successful response
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}")

    # Parse JSON response
    data = response.json()

    # Return daily circulation data
    return data["dados"][0]

# Function to format and process data
def format_data(data):
    """
    Formats and cleans raw data from the API.

    Args:
        data (dict): Dictionary containing raw daily circulation data.

    Returns:
        pd.DataFrame: Pandas DataFrame with formatted data.
    """
    # Extract relevant data
    formatted_data = []
    for item in data:
        formatted_data.append({
            "date": pd.to_datetime(item["data"]),
            "circulation": float(item["valor"].replace(",", "")),
        })

    # Create Pandas DataFrame
    df = pd.DataFrame(formatted_data)

    # Add additional calculations
    df["change_from_previous"] = df["circulation"].diff()
    df["percentage_change"] = (df["change_from_previous"] / df["circulation"]).fillna(0) * 100

    # Return formatted data
    return df

# Function to save data to CSV
def save_data_to_csv(data, filename):
    """
    Saves formatted data to a CSV file.

    Args:
        data (pd.DataFrame): Pandas DataFrame with formatted data.
        filename (str): Filename for the CSV file.
    """
    data.to_csv(filename, index=False)

# Get today's date
today = date.today().strftime("%Y-%m-%d")

# Get daily circulation data
daily_data = get_daily_circulation_data(today)

# Format and process data
formatted_data = format_data(daily_data)

# Save data to CSV file
save_data_to_csv(formatted_data, f"daily_circulation_{today}.csv")

# Print confirmation message
print("Daily money in circulation data retrieved and saved successfully.")
