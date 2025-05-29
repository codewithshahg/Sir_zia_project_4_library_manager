import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Library Manager",
    page_icon="📚",
    layout="wide"  # optional: 'centered' or 'wide'
)

# App title
st.title("Welcome to the Library Manager")

# Example sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Books", "Authors"])

# Simple navigation logic
if page == "Home":
    st.write("This is the home page of your library manager.")
elif page == "Books":
    st.write("Here you can add, edit, or delete books.")
elif page == "Authors":
    st.write("Manage authors here.")

# Example input and output
book_name = st.text_input("Enter book name:")
author_name = st.text_input("Enter author name:")

if st.button("Add Book"):
    if book_name and author_name:
        st.success(f"Book '{book_name}' by '{author_name}' added successfully!")
    else:
        st.error("Please enter both book name and author name.")

# Footer or other content
st.markdown("---")
st.write("© 2025 My Library Manager")
