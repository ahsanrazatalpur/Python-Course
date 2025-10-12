# for quick overview
# Creates a text-based or markdown report summarizing the analysis.
# Includes:
# Dataset size
# Missing values
# Key statistics
# Notes or conclusions

# -------------------------------------------------------------
# Function: quick_overview
# -------------------------------------------------------------
def quick_overview(df):
    """
    Prints a quick summary of the DataFrame — including:
    - Shape (rows × columns)
    - First 5 rows (sample data)
    - Data types & missing values info
    - Descriptive statistics (mean, std, min, max, etc.)
    """

    # Check if DataFrame is not None (i.e., data is loaded successfully)
    if df is not None:
        print("\n--- Quick Data Overview ---")

        # 1️⃣ Show shape → tells how many rows and columns the dataset has
        print("\nShape (Rows, Columns):", df.shape)

        # 2️⃣ Display first 5 rows → helps see the actual data quickly
        print("\nFirst 5 Rows:")
        print(df.head())

        # 3️⃣ Show info → displays column names, data types, and missing values
        print("\nData Types and Nulls:")
        df.info()

        # 4️⃣ Descriptive statistics → numeric summary (mean, std, min, max, etc.)
        print("\nDescriptive Statistics:")
        print(df.describe())

    else:
        # If no DataFrame is passed
        print("Cannot generate summary: DataFrame is None.")
