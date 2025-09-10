from src.pipeline import run_pipeline
from pathlib import Path
import pandas as pd

def test_pipeline_creates_output(tmp_path):
    inp = tmp_path / "reviews.csv"
    out = tmp_path / "output.csv"
    inp.write_text("review_id,review_text\n1,This is great!\n")
    run_pipeline(str(inp), str(out))
    assert out.exists()
    df = pd.read_csv(out)
    assert "sentiment" in df.columns
