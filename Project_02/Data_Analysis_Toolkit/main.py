# main.py - Interactive CLI with Graphs (Auto-load + Numbered Columns)

from toolkit.loader import load_csv
from toolkit.cleaner import remove_missing_data
from toolkit.summary import quick_overview
from toolkit.visualizer import plot_histogram, plot_boxplot, plot_scatterplot

DATA_PATH = "data/car-sales.csv"

def select_column(columns, prompt="Select a column: "):
    """Display columns with numbers and let the user pick one."""
    print("\nAvailable columns:")
    for idx, col in enumerate(columns):
        print(f"{idx + 1}. {col}")
    while True:
        choice = input(prompt)
        if choice.isdigit() and 1 <= int(choice) <= len(columns):
            return columns[int(choice) - 1]
        else:
            print("Invalid choice, try again!")

def main():
    """Interactive CLI for PyDataToolkit with visualization"""
    data = None
    cleaned_data = None

    while True:
        print("\n--- PyDataToolkit Menu ---")
        print("1. Load Data")
        print("2. Show Quick Summary (Pre-Cleaning)")
        print("3. Clean Data")
        print("4. Show Quick Summary (Post-Cleaning)")
        print("5. Visualize Data")
        print("6. Exit")

        choice = input("Choose an option: ")

        # Auto-load data if necessary
        if choice in ["2", "3", "4", "5"] and data is None:
            print("Data not loaded yet. Loading automatically...")
            data = load_csv(DATA_PATH)

        if choice == "1":
            data = load_csv(DATA_PATH)
            cleaned_data = None  # Reset cleaned data if new file is loaded
        elif choice == "2":
            quick_overview(data)
        elif choice == "3":
            cleaned_data = remove_missing_data(data)
            print("Data cleaned successfully!")
        elif choice == "4":
            if cleaned_data is None:
                print("Please clean data first!")
            else:
                quick_overview(cleaned_data)
        elif choice == "5":
            if cleaned_data is None:
                print("Please clean data first!")
            else:
                while True:
                    print("\n--- Visualization Options ---")
                    print("1. Histogram")
                    print("2. Box Plot")
                    print("3. Scatter Plot")
                    print("4. Return to Main Menu")
                    viz_choice = input("Choose visualization: ")

                    if viz_choice == "1":
                        column = select_column(cleaned_data.columns, "Select column for histogram: ")
                        plot_histogram(cleaned_data, column)
                    elif viz_choice == "2":
                        column = select_column(cleaned_data.columns, "Select column for box plot: ")
                        by_col = input("Optional - enter column to group by (or press Enter to skip): ")
                        if by_col not in cleaned_data.columns:
                            by_col = None
                        plot_boxplot(cleaned_data, column, by_col)
                    elif viz_choice == "3":
                        x_col = select_column(cleaned_data.columns, "Select X column: ")
                        y_col = select_column(cleaned_data.columns, "Select Y column: ")
                        plot_scatterplot(cleaned_data, x_col, y_col)
                    elif viz_choice == "4":
                        break
                    else:
                        print("Invalid visualization option!")
        elif choice == "6":
            print("Exiting PyDataToolkit. Goodbye!")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
