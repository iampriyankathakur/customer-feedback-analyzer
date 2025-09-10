# Project layout
```
customer-feedback-analyzer/
├── README.md
├── requirements.txt
├── src/
│   ├── sentiment.py
│   ├── topics.py
│   ├── entities.py
│   └── pipeline.py
├── data/
│   ├── sample_reviews.csv
│   └── analysis_output.csv
├── notebooks/
│   └── experiments.ipynb
├── dashboards/
│   └── tableau_demo.twb
└── tests/
    └── test_pipeline.py
```

# 📊 Customer Feedback Analyzer

Turn raw customer feedback (reviews, surveys, support tickets) into **actionable insights**.  
Automatically performs:
- ✅ Sentiment analysis (positive, negative, neutral)
- ✅ Topic clustering (what customers talk about most)
- ✅ Named entity recognition (brands, products, features)
- ✅ Export of insights for dashboards (CSV, Tableau, Streamlit)


## 🚀 Features
- Analyze text data with NLP
- Summarize insights with clustering and visualizations
- Export results for BI dashboards
- Easy to extend with new datasets


## ⚙️ Installation
git clone https://github.com/yourusername/customer-feedback-analyzer.git
cd customer-feedback-analyzer
pip install -r requirements.txt

## ▶️ Usage
python src/pipeline.py --input data/sample_reviews.csv --output data/analysis_output.csv

## 📊 Tech Stack

Python

NLP: spaCy, scikit-learn

Clustering: scikit-learn (KMeans, LDA)

Visualization: matplotlib / seaborn, Tableau

Optional UI: Streamlit

## 📌 Roadmap

 Add multilingual support

 Integrate Hugging Face sentiment model

 Add Streamlit dashboard

## 📄 License

MIT License

---
