# For reading files
# Responsible for loading data from different sources like CSV, Excel, or JSON.
# It creates and returns a Pandas DataFrame.


# Import the pandas library (used for data handling and analysis)
import pandas as pd


# Function: load_csv
def load_csv(filepath):
    """Loads a CSV file into a pandas DataFrame."""
    try:
        # Print message showing which file is being loaded
        print(f"Loading data from: {filepath}")
        
        # Read the CSV file and store it as a DataFrame
        df = pd.read_csv(filepath)
        
        # Return the loaded DataFrame
        return df
    
    # If the file is not found, handle the error gracefully
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
