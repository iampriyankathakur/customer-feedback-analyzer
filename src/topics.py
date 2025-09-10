from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_topics(texts, n_clusters=3):
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(texts)
    model = KMeans(n_clusters=n_clusters, random_state=42)
    model.fit(X)
    return model.labels_
