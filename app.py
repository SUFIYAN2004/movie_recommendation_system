import streamlit as st
import pickle

# Load precomputed data (fast - no model needed at runtime since vectors are precomputed)
with open('movie_data.pkl', 'rb') as f:
    data = pickle.load(f)

titles = data['titles']
genres = data['genres']
similarity_matrix = data['similarity_matrix']

title_to_idx = {title: i for i, title in enumerate(titles)}

st.title("🎬 Movie Recommender")
st.caption("Content-based recommendations using embeddings + attention")

selected_title = st.selectbox("Pick a movie:", sorted(titles))

if st.button("Recommend"):
    idx = title_to_idx[selected_title]
    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    scores = [s for s in scores if s[0] != idx][:5]

    st.subheader(f"Because you liked '{selected_title}' ({genres[idx]}):")
    for i, score in scores:
        st.write(f"**{titles[i]}**  —  similarity: {score:.2f}  ({genres[i]})")