import pandas as pd
import ast

def load_and_clean_data(file_path):
    """
    Loads the dataset, cleans it by dropping missing values, and parses Trade_History.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Load the dataset
    df = pd.read_csv(file_path)

    # Drop rows with missing Trade_History
    df = df.dropna(subset=['Trade_History'])

    # Parse Trade_History as a list of dictionaries
    df['Trade_History'] = df['Trade_History'].apply(ast.literal_eval)

    return df

if __name__ == "__main__":
    # Test the cleaning function
    file_path = 'dataset/TRADES_CopyTr_90D_ROI.csv'
    cleaned_df = load_and_clean_data(file_path)
    print("Data cleaned successfully:")
    print(cleaned_df.info())
    print(cleaned_df.head())
