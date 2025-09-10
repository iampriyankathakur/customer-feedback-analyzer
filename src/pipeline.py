import argparse
import pandas as pd
from sentiment import get_sentiment
from topics import cluster_topics
from entities import extract_entities

def run_pipeline(input_path, output_path):
    df = pd.read_csv(input_path)
    
    # Sentiment
    df["sentiment"] = df["review_text"].apply(get_sentiment)
    
    # Topic clusters
    df["topic_cluster"] = cluster_topics(df["review_text"].tolist())
    
    # Extract entities (example: first entity found per review)
    df["entities"] = df["review_text"].apply(lambda x: extract_entities(x))
    
    df.to_csv(output_path, index=False)
    print(f"Analysis saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    run_pipeline(args.input, args.output)
