# for basic plot
# Responsible for data visualization — the graphical representation of data.
# Uses libraries like Matplotlib and Seaborn.
# Can generate:
# Histograms
# Bar charts
# Scatter plots
# Correlation heatmaps

# 📦 Importing necessary libraries
import pandas as pd                 # For handling data in DataFrame format
import matplotlib.pyplot as plt     # For creating visual plots
import seaborn as sns               # For advanced and attractive visualizations

# 🎨 Setting a visual style for plots (makes graphs look cleaner)
plt.style.use('ggplot')


# ============================
# 📊 1. HISTOGRAM FUNCTION
# ============================
def plot_histogram(df, column, bins=10, title=None):
    """
    Generates a histogram for a single numeric column to visualize its distribution.
    
    Parameters:
        df (DataFrame): The dataset.
        column (str): The column to plot.
        bins (int): Number of bins (default=10).
        title (str): Optional custom title for the plot.
    """
    # ✅ Error handling — checks if DataFrame or column is invalid
    if df is None or column not in df.columns:
        print(f"Error: DataFrame is None or column '{column}' not found.")
        return

    # Create a new figure
    plt.figure(figsize=(8, 6))
    # Plot histogram with density curve (KDE)
    sns.histplot(df[column].dropna(), bins=bins, kde=True)
    
    # Add title and labels
    plt.title(title if title else f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    
    print(f"Visualizing: Displaying histogram for '{column}'.")
    plt.show()


# ============================
# 📦 2. BOX PLOT FUNCTION
# ============================
def plot_boxplot(df, column, by_column=None, title=None):
    """
    Generates a box plot to visualize data distribution and detect outliers.
    
    Parameters:
        df (DataFrame): The dataset.
        column (str): Numeric column for the y-axis.
        by_column (str): Optional — group by another column (e.g., gender, category).
        title (str): Optional custom title.
    """
    # ✅ Validate input
    if df is None or column not in df.columns:
        print(f"Error: DataFrame is None or column '{column}' not found.")
        return

    plt.figure(figsize=(8, 6))
    
    # If grouping column exists → create grouped boxplot
    if by_column and by_column in df.columns:
        sns.boxplot(x=by_column, y=column, data=df)
        plt.title(title if title else f'{column} Distribution by {by_column}')
        plt.xlabel(by_column)
    else:
        # Single column boxplot
        sns.boxplot(y=df[column].dropna())
        plt.title(title if title else f'Box Plot of {column}')
        plt.xlabel('')  # Empty label for cleaner look
        
    plt.ylabel(column)
    
    print(f"Visualizing: Displaying box plot for '{column}'.")
    plt.show()


# ============================
# 🔵 3. SCATTER PLOT FUNCTION
# ============================
def plot_scatterplot(df, x_column, y_column, title=None):
    """
    Generates a scatter plot to visualize the relationship between two numeric columns.
    
    Parameters:
        df (DataFrame): The dataset.
        x_column (str): Column for X-axis.
        y_column (str): Column for Y-axis.
        title (str): Optional title.
    """
    # ✅ Validation
    if df is None or x_column not in df.columns or y_column not in df.columns:
        print(f"Error: DataFrame is None or required columns not found.")
        return

    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df[x_column], y=df[y_column])
    
    # Add labels and title
    plt.title(title if title else f'Relationship between {x_column} and {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    
    print(f"Visualizing: Displaying scatter plot for '{x_column}' vs '{y_column}'.")
    plt.show()
