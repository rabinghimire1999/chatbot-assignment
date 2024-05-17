"""
utils.py

This is the moduels for utils.

Author: Rabin Ghimire
Date: May 17, 2024
"""
from dotenv import dotenv_values
import os

def get_env_variables():
    env_vars = dotenv_values('.env')
    return env_vars

def set_openai_key():
    env_vars = get_env_variables()
    openai_key = env_vars["OPENAI_API_KEY"]
    os.environ["OPENAI_API_KEY"] = openai_key
    return None