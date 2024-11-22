import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_metrics(metrics_df):
    """
    Generate visualizations for financial metrics.
    Args:
        metrics_df (pd.DataFrame): DataFrame with calculated metrics.
    """
    # Example 1: Distribution of ROI
    plt.figure(figsize=(10, 6))
    sns.histplot(metrics_df['ROI'], bins=30, kde=True, color='blue')
    plt.title('ROI Distribution')
    plt.xlabel('ROI')
    plt.ylabel('Frequency')
    plt.show()

    # Example 2: Top 20 Accounts by Sharpe Ratio
    top_accounts = metrics_df.nlargest(20, 'Sharpe_Ratio')
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Port_IDs', y='Sharpe_Ratio', data=top_accounts, palette='viridis')
    plt.title('Top 20 Accounts by Sharpe Ratio')
    plt.xlabel('Port IDs')
    plt.ylabel('Sharpe Ratio')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    # Load the calculated metrics
    metrics_file = 'calculated_metrics.csv'
    metrics_df = pd.read_csv(metrics_file)

    # Generate visualizations
    plot_metrics(metrics_df)
