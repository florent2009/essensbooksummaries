import streamlit as st
from streamlit_option_menu import option_menu
import requests
import json


st.title("Essens Book Summaries")

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Categories", ["Bios", 'Science','Literature','Sci-Fi','Philosophy'], 
        icons=[], menu_icon="book", default_index=1)
    

# Main content based on selection
if selected == "Bios":
    st.write("# Bios Section")
    st.write("This is where you can put details related to biographies.")
elif selected == "Science":
    st.write("# Science Section")
    st.write("This section covers all things related to science.")
elif selected == "Literature":
    st.write("# Literature Section")
    st.write("Here you can explore various literary works.")
elif selected == "Sci-Fi":
    st.write("# Sci-Fi Section")
    st.write("Dive into the world of science fiction here.")
elif selected == "Philosophy":
    st.write("# Philosophy Section")
    st.write("Philosophical discussions and ideas can be found here.")




# URL of your JSON data on the server
url = 'http://www.essensbooksummaries.com/asin.json'

# Fetching the JSON data from the server
@st.cache_data
def load_data():
    response = requests.get(url)
    data = response.json()
    return data

data = load_data()

# Single search bar UI
st.title('Search Books')
query = st.text_input('Search by Title or Author')

# Function to filter data based on query
def filter_data(data, query):
    query = query.lower()
    filtered = [
        item for item in data
        if query in item['title'].lower() or query in item['author'].lower()
    ]
    return filtered

# Displaying the filtered results
if query:
    results = filter_data(data, query)
    if results:
        for item in results:
            st.write(f"**Title:** {item['title']} - **Author:** {item['author']} - **Category:** {item['category']}")
    else:
        st.write("No results found")
else:
    st.write("Start typing to search for books...")

