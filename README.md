# Binance Trade Data Analysis

## Overview
This project analyzes historical trade data from Binance accounts over a 90-day period to calculate performance metrics, rank accounts, and identify the top 20 performers.

## Objective
1. Calculate financial metrics (ROI, PnL, Sharpe Ratio, etc.) for each account.
2. Rank accounts based on a weighted scoring system.
3. Provide insights through visualizations and detailed outputs.

## Execute Scripts
Data Cleaning: Run data_cleaning.py to clean the dataset => python data_cleaning.py
Output: Cleaned data saved for analysis.

Metrics Calculation: Run analysis.py to calculate metrics => python analysis.py
Output: calculated_metrics.csv and top_20_accounts.csv.

Visualization: Run visualization.py to generate visualizations = >python visualization.py

## Dependencies
pandas
matplotlib
seaborn
numpy
Install these packages using: pip install -r requirements.txt
