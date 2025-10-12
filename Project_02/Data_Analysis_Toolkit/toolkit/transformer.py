# for filtering , selecting and sorting
# Performs data transformations, such as:
# Changing column names
# Converting data types
# Creating new columns or derived metrics
# Encoding categorical variables
# Why Important:

# Import the pandas library for handling DataFrames
import pandas as pd

# --------------------------------------------------------
# Function: filter_by_value
# Purpose: Filter rows in a DataFrame based on a condition
# --------------------------------------------------------
def filter_by_value(df, column, value, operator='=='):
    """
    Filters the DataFrame rows where the specified column matches the given value 
    based on the provided operator (==, >, <, !=, >=, <=).
    """

    # If DataFrame is missing, show an error message
    if df is None:
        print("Error: DataFrame is None.")
        return None

    # Print message showing which column and condition are used
    print(f"Transforming: Filtering '{column}' where value is {operator} {value}")
    
    # Apply filtering condition according to the operator type
    if operator == '==':
        return df[df[column] == value].copy()
    elif operator == '>':
        return df[df[column] > value].copy()
    elif operator == '<':
        return df[df[column] < value].copy()
    elif operator == '!=':
        return df[df[column] != value].copy()
    elif operator == '>=':
        return df[df[column] >= value].copy()
    elif operator == '<=':
        return df[df[column] <= value].copy()
    else:
        # If operator is invalid, show error
        print(f"Error: Invalid operator '{operator}'.")
        return df


# --------------------------------------------------------
# Function: sort_data
# Purpose: Sort DataFrame by a given column
# --------------------------------------------------------
def sort_data(df, column, ascending=True):
    """Sorts the DataFrame by the values in the specified column."""

    # Check if DataFrame exists
    if df is None:
        print("Error: DataFrame is None.")
        return None
        
    # Set sorting order text
    order = "ascending" if ascending else "descending"
    print(f"Transforming: Sorting data by '{column}' in {order} order.")

    # Return a new DataFrame sorted by the chosen column
    return df.sort_values(by=column, ascending=ascending).copy()


# --------------------------------------------------------
# Function: create_derived_column
# Purpose: Create a new column using a custom function
# --------------------------------------------------------
def create_derived_column(df, new_column_name, expression_func):
    """
    Creates a new column using a custom function applied to existing columns.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
        new_column_name (str): Name for the new column.
        expression_func (callable): A function that takes a row (pd.Series) 
                                    and returns the value for the new column.
    """

    # Check if DataFrame exists
    if df is None:
        print("Error: DataFrame is None.")
        return None

    # Print message showing new column creation
    print(f"Transforming: Creating new column '{new_column_name}'.")

    try:
        # Apply user-defined function to each row (axis=1 = row-wise)
        df[new_column_name] = df.apply(expression_func, axis=1)
        return df
    except Exception as e:
        # Catch and display any errors
        print(f"Error creating derived column '{new_column_name}': {e}")
        return df
