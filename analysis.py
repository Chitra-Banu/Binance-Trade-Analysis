import pandas as pd

def calculate_metrics(df):
    """
    Calculate financial metrics for each account.
    Args:
        df (pd.DataFrame): Cleaned DataFrame with Trade_History parsed.
    Returns:
        pd.DataFrame: DataFrame with calculated metrics.
    """
    # Initialize metrics columns
    metrics = []

    for _, row in df.iterrows():
        port_id = row['Port_IDs']
        trades = row['Trade_History']

        # Calculate financial metrics (e.g., ROI, PnL, Sharpe Ratio, etc.)
        # Placeholder calculations (replace with actual formulas):
        total_positions = len(trades)
        win_positions = sum(1 for trade in trades if trade['realizedProfit'] > 0)
        win_rate = win_positions / total_positions if total_positions > 0 else 0
        roi = sum(trade['realizedProfit'] for trade in trades)
        pnl = roi
        sharpe_ratio = roi / (total_positions ** 0.5) if total_positions > 0 else 0

        metrics.append({
            'Port_IDs': port_id,
            'ROI': roi,
            'PnL': pnl,
            'Sharpe_Ratio': sharpe_ratio,
            'Win_Rate': win_rate,
            'Win_Positions': win_positions,
            'Total_Positions': total_positions
        })

    return pd.DataFrame(metrics)

if __name__ == "__main__":
    from data_cleaning import load_and_clean_data

    # Load and clean data
    file_path = 'dataset/TRADES_CopyTr_90D_ROI.csv'
    df = load_and_clean_data(file_path)

    # Calculate metrics
    metrics_df = calculate_metrics(df)
    print("Metrics calculated successfully:")
    print(metrics_df.head())

    # Save metrics to a CSV file
    metrics_df.to_csv('calculated_metrics.csv', index=False)
    print("Metrics saved to calculated_metrics.csv")
