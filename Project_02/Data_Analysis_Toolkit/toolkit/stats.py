# for statistical calculation
# Handles statistical analysis.
# Common tasks:
# Compute descriptive statistics (mean, median, std, etc.)
# Find correlations between numeric columns
# Detect outliers or patterns

# Import pandas library for data manipulation and statistical functions
import pandas as pd


# -------------------------------------------------------------
# Function 1: get_column_mean
# -------------------------------------------------------------
def get_column_mean(df, column):
    """Calculates and returns the mean (average) of a specified numeric column."""
    # Check if DataFrame exists and column is valid
    if df is not None and column in df.columns:
        try:
            # Calculate the mean (average) of the column
            mean_val = df[column].mean()
            print(f"Stats: Mean of '{column}' is {mean_val:.2f}")
            return mean_val
        except TypeError:
            # Handles error if column is not numeric
            print(f"Error: Column '{column}' is not numeric and cannot be averaged.")
            return None
    elif df is None:
        # Error if no DataFrame is passed
        print("Error: DataFrame is None.")
        return None
    else:
        # Error if column name doesn't exist
        print(f"Error: Column '{column}' not found in the DataFrame.")
        return None


# -------------------------------------------------------------
# Function 2: get_column_median
# -------------------------------------------------------------
def get_column_median(df, column):
    """Calculates and returns the median (middle value) of a specified numeric column."""
    # Check if DataFrame exists and column is valid
    if df is not None and column in df.columns:
        try:
            # Calculate the median (middle value)
            median_val = df[column].median()
            print(f"Stats: Median of '{column}' is {median_val:.2f}")
            return median_val
        except TypeError:
            # Handles non-numeric columns
            print(f"Error: Column '{column}' is not numeric.")
            return None
    elif df is None:
        # No DataFrame provided
        return None
    else:
        # Column not found
        return None


# -------------------------------------------------------------
# Function 3: get_descriptive_stats
# -------------------------------------------------------------
def get_descriptive_stats(df, column):
    """Returns the full descriptive statistics (count, mean, std, min, max, quartiles) for a column."""
    # Check if DataFrame and column are valid
    if df is not None and column in df.columns:
        try:
            # Get summary statistics using describe()
            stats = df[column].describe()
            print(f"\nStats: Descriptive Statistics for '{column}':")
            print(stats)
            return stats
        except Exception as e:
            # Handles unexpected errors
            print(f"Error calculating descriptive statistics for '{column}': {e}")
            return None
    return None
