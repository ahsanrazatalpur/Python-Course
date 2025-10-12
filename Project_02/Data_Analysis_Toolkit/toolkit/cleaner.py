# For cleaning and missing data
# Handles data cleaning tasks such as:
# Removing duplicates
# Handling missing values (NaN)
# Fixing inconsistent data (e.g., lowercase column names)
# Ensures your dataset is ready for analysis.

# Function to remove missing (NaN) data from a DataFrame
def remove_missing_data(df, subset=None):
    """Removes rows with any missing values (NaN) in the DataFrame."""
    # Check if DataFrame exists (not None)
    if df is not None:
        print("Cleaning: Removing rows with missing data.")
        # Drop rows that have NaN values (only in 'subset' columns if specified)
        return df.dropna(subset=subset)
    # If no DataFrame provided, return None
    return None


# Function to fill missing (NaN) values in a specific column
def fill_missing_data(df, column, value):
    """Fills missing values in a specific column with a given value."""
    # Check if DataFrame exists
    if df is not None:
        print(f"Cleaning: Filling missing values in '{column}' with {value}.")
        # Replace NaN values in that column with the given 'value'
        return df.fillna({column: value})
    # If no DataFrame provided, return None
    return None
