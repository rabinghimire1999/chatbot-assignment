"""chain.py

This is the moduels to create chain.

Author: Rabin Ghimire
Date: May 17, 2024
"""
from vectordatabase import VectorStore
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationRetrievalChain
import os   
import streamlit as st
from htmlTemplates import css, bot_template, user_template


class Chain:
    def __init__(self):
        super().__init__()
        self.vectorstore = VectorStore()
               
    def get_conversation_chain(self):
        llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.environ["OPENAI_API_KEY"])
        memory = ConversationBufferMemory(
            memory_key='chat_history',
            return_messages=True
        )
        conversation_chain = ConversationRetrievalChain.from_llm(
            llm=llm,
            retriever=self.vectorstore.as_retriever(),
            memory=memory
        )
        return conversation_chain
    
    def handle_userinput(user_question):
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat history']
        
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(user_template.replace(
                    "{{MSG}}", message.content
                ), unsafe_allow_html=True
               )
            else:
                st.write(bot_template.replace(
                    "{{MSG}}", message.content
                ), unsafe_allow_html=True
            )
        
    