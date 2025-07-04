import streamlit as st
import pickle
import pandas as pd

# Recommendation function
def recommend(book):
    book_index = books[books['title'] == book].index[0]
    distances = similarity[book_index]
    books_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_books = []
    for i in books_list:
        recommended_books.append(books.iloc[i[0]].title)

    return recommended_books

# Load data and similarity matrix
books_dict = pickle.load(open('books_dict.pkl', 'rb'))
books = pd.DataFrame(books_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit interface
st.title('Smart Book Recommender')

# Dropdown to select a book
option = st.selectbox(
    'Select a book for recommendations:',
    books['title'].values
)

st.write(f'You selected: {option}')

# Show recommendations when the button is clicked
if st.button('Show Recommendation'):
    recommendations = recommend(option)
    st.write("Recommended Books:")
    for i in recommendations:
        st.write(i)
