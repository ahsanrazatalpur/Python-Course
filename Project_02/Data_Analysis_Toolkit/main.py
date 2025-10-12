# Demo Cli runner

# main.py - Demo / CLI runner
# It’s the entry point of your project — the file you run first (python main.py).
# It connects all modules together and defines the analysis workflow.


# 📦 Importing functions from other toolkit modules
from toolkit.loader import load_csv                  # For loading CSV files
from toolkit.cleaner import remove_missing_data      # For cleaning data (handling missing values)
from toolkit.summary import quick_overview           # For getting summary info of the DataFrame
# from toolkit.transformer import (...)              # Placeholder for future data transformation functions
# from toolkit.stats import (...)                    # Placeholder for statistical analysis functions
# from toolkit.visualizer import (...)               # Placeholder for visualization functions


# 🗂️ Define the path to your dataset
# NOTE: Make sure 'car-sales.csv' exists inside the 'data' folder
DATA_PATH = "data/car-sales.csv"


# ============================
# 🚀 MAIN FUNCTION
# ============================
def main():
    """Main function to demonstrate the PyDataToolkit workflow."""
    print("--- PyDataToolkit Demo Start ---")

    # 1️⃣ Load the dataset
    data = load_csv(DATA_PATH)
    if data is None:     # If file not found or load failed → exit early
        return

    # 2️⃣ Show data summary BEFORE cleaning
    quick_overview(data)

    # 3️⃣ Clean the dataset (e.g., remove missing/null values)
    cleaned_data = remove_missing_data(data)

    # 4️⃣ Show data summary AFTER cleaning
    quick_overview(cleaned_data)

    # 5️⃣ Future Steps (to be implemented later)
    #     - Transformation (filtering, aggregation, etc.)
    #     - Statistical analysis
    #     - Visualization (plots, charts, etc.)

    print("\n--- PyDataToolkit Demo Complete ---")


# 🧠 Entry Point
# Ensures that 'main()' runs only when this file is executed directly
if __name__ == "__main__":
    main()
