import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import streamlit as st

st.title('LLMs Projects')

# test streamlit app with streamlit run text_to_label.py
