"""pdfreader.py

This is the modules to read pdf documents.

Author: Rabin Ghimire
Date: May 17, 2024
"""

from PyPDF2 import PdfReader
import re

class PDFTextExtractor:
    def __init__ (self, pdf_docs):
        self.pdf_docs = pdf_docs
        
    def extract_text(self):
        text = ""
        for pdf in self.pdf_docs:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
    
    def clean_text(self, text):
        text = re.sub(r'\s+',' ',text)   # Remove multiple spaces
        text = re.sub(r'[^\x00-\x7F]+','', text)  # Remove special characters
        text = re.sub(r'[^\w\s]','',text)  # Remove special characters
        return text.strip()
    
    def extract_metadata(self, pdf):
        pdf_reader = PdfReader(pdf)
        return pdf_reader.metadata
    
    def chunk_text(self, text, chunk_size=1000):
        return [text[i:1 + chunk_size] for i in range (0, len(text), chunk_size)]
    
    def process_pdfs(self):
        data = []
        for pdf in self.pdf_docs:
            text = self.extract_text()
            cleaned_text = self.clean_text(text)
            metadata = self.extract_metadata(pdf)
            all_text += cleaned_text
            chunks = self.chunk_text(all_text)
            data.append({
                'chunks': chunks,
                'metadata':metadata
            })
        return data
        