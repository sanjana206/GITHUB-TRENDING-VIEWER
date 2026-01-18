import streamlit as st
from fetch_data import fetch_trending_repos
from ai_ranking import rank_repositories
from ai_prediction import predict_future_popularity

st.set_page_config(page_title="GitHub Trending Viewer AI", layout="wide")

st.title("🔥 GitHub Trending Viewer with AI (Python)")
st.write("AI-powered analysis of trending GitHub repositories")

if st.button("Fetch Trending Repositories"):
    repos = fetch_trending_repos()

    if not repos:
        st.error("Failed to fetch data")
    else:
        df = rank_repositories(repos)

        st.subheader("📊 Trending Repositories")
        st.dataframe(df[["Repository", "Stars"]].head(10))

        st.subheader("🤖 AI Popularity Prediction")
        stars = df["Stars"].head(5).tolist()
        prediction = predict_future_popularity(stars)

        st.success(f"Predicted future popularity score: {prediction} stars")
