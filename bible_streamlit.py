import streamlit as st
import requests


st.set_page_config(page_title="Bible Search", page_icon="☻", layout="centered")

st.title("Search a Bible Verse (KJV)")

with st.sidebar:
    st.header("Search Instructions ☻")
    st.markdown("""
    
    - `John 3` for an entire chapter
    - `John 3:16` for a single verse
    - `John 3:16-20` for a range of verses
    - `John 3:16-4:10` for multiple chapters
    """)

col1, col2, col3 = st.columns([1, 0.5, 0.5])

with col1:
    book = st.text_input("Book Name", placeholder="Genesis")
    
with col2:
    verse = st.text_input("Chapter + Verse", placeholder="1:1")

with col3:
    st.markdown("<br>", unsafe_allow_html=True)
    search_button = st.button("Search", type="primary")


def get_verse(book, verse):
    url = f'https://bible-api.com/{book}+{verse}?translation=kjv'
    try:
        response = requests.get(url)
        if response.status_code == 404:
            st.error("Error! Please enter a valid book and verse.")
            return
        elif response.status_code == 200: # if successful
            bible_content = response.json()
            st.markdown("---")
            st.badge(f"{bible_content['reference']}:")
            verses = bible_content["verses"]
            
            for v in verses:
                # thsi makes sections which is not good i dont want
                with st.container():
                    # st.markdown(v{['verse']})
                    # what is difference between markdown and write
                    st.write(f':red[{v['verse']}] {v['text']}')
                    # st.markdown("") 
        
        else:
            st.warning(f"Unexpected error. (Status code: {response.status_code})")
            # wha does this do?
            # like catching the errors
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# searching stuff
if search_button:
    if book and verse:
        with st.spinner("Searching..."):
            get_verse(book, verse)
    elif book and not verse:
        st.warning("Please enter a chapter and verse.")
    else:
        st.warning("Please enter both a book name and verse.")



st.markdown("""
<div style='text-align: center; color: gray;'>
    <small>Made with ❤️ by Fay</small>
</div>
""", unsafe_allow_html=True)