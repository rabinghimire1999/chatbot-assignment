"""
app.py

This modules is for the UI interface to chat with pdf.

Author: Rabin Ghimire
Date: May 16, 2024
"""
import streamlit as st
from htmlTemplates import css
from chain import Chain
from pdfreader import PDFTextExtractor
from vectordatabase import VectorStore

def main():
    st.set_page_config(page_title="CHATBOT")
    st.write(css, unsafe_allow_html=True)
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "conversation" not in st.session_state:
        st.session_state.chat_history = None
    
    st.header("CHATBOT")
    user_question = st.text_input("Ask Your questions")
    if user_question:
        Chain.handle_userinput(user_question)
        
    with st.sidebar:
        st.subheader("Enter documents")
        pdf_docs = st.file_uploader("Upload PDFs to Context", accept_multiple_files=True)
        
        if st.button("Process"):
            with st.spinner("Processing"):
                text = PDFTextExtractor.process_pdfs(pdf_docs)
                vectorstore = VectorStore.get_vector_store(text)
                
                st.session_state.conversation = Chain.get_conversation_chain(vectorstore)
                
if __name__ == '__main__':
    main()
    