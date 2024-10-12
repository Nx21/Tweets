import pandas as pd
try:
    df_negative = pd.read_csv('../data/processedNegative.csv')
    print("Loaded processedNegative.csv successfully.")
    df_neutral = pd.read_csv('../data/processedNeutral.csv')
    print("Loaded processedNeutral.csv successfully.")
    df_positive = pd.read_csv('../data/processedPositive.csv')
    print("Loaded processedPositive.csv successfully.")
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit(1)
print(df_negative)