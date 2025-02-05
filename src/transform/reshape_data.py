import pandas as pd

def reshape_data(file_path):
    df = pd.read_csv(file_path)
    melted_df = df.melt(id_vars=['date', 'account_id'], var_name='metric', value_name='value')
    return melted_df

if __name__ == "__main__":
    reshaped_df = reshape_data("../data/processed/meta_cleaned.csv")
    reshaped_df.to_csv("../data/processed/meta_reshaped.csv", index=False)
    print("Data reshaped and saved.")
