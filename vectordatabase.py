"""
vectordatabase.py

This is the modules for vector database.

Author: Rabin Ghimire
Date: May 17, 2024
"""
from pdfreader import PDFTextExtractor
from langchain.embeddings from OpenAIEmbeddings
from langchain.vectorstores import FAISS

class VectorStore:
    def __init__(self, text_chunks):
        self.text_chunks = text_chunks
        self.embeddings = OpenAIEmbeddings()
        
    def get_vector_store(self):
        vectorstore = FAISS.from_texts(texts=self.text_chunks, embedding= self.embeddings)
        return vectorstore
    
    
        


