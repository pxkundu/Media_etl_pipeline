import pandas as pd

def enrich_data(file_path):
    df = pd.read_csv(file_path)
    df["engagement_rate"] = df["likes"] / (df["impressions"] + 1) * 100  # Example metric
    return df

if __name__ == "__main__":
    enriched_df = enrich_data("../data/processed/meta_reshaped.csv")
    enriched_df.to_csv("../data/processed/meta_enriched.csv", index=False)
    print("Data enriched and saved.")
