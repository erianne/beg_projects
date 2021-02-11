import streamlit as st

import projs.odd_even 
import projs.about

# This struture of pages was copied from awesome Strealit app
# maintead by Marc Skov Madsen 
# it can be found at https://github.com/MarcSkovMadsen/awesome-streamlit


PAGES = {
    "About": projs.about,
    "Odd or Even": projs.odd_even
}


st.sidebar.title("Menu")
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
page = PAGES[selection]

st.write(f"you selected {page}")



