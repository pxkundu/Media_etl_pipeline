import pandas as pd

def clean_data(file_path):
    df = pd.read_json(file_path)
    df.dropna(inplace=True)
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df

if __name__ == "__main__":
    df = clean_data("../data/raw/meta_data.json")
    df.to_csv("../data/processed/meta_cleaned.csv", index=False)
    print("Data cleaned and saved.")
