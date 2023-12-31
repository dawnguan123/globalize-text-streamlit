# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 22:04:14 2023

@author: Gavin
"""
import streamlit as st
from langchain import PromptTemplate
from langchain import OpenAI
import os
#import openai

template = """
    Below is an email that may be poorly worded.
    Your goal is to:
    - Properly format the email
    - Convert the input text to a specified tone
    - Convert the input text to a specified dialect

    Here are some examples different Tones:
    - Formal: We went to Barcelona for the weekend. We have a lot of things to tell you.
    - Informal: Went to Barcelona for the weekend. Lots to tell you.  

    Here are some examples of words in different dialects:
    - American: French Fries, cotton candy, apartment, garbage, cookie, green thumb, parking lot, pants, windshield
    - British: chips, candyfloss, flag, rubbish, biscuit, green fingers, car park, trousers, windscreen

    Example Sentences from each dialect:
    - American: I headed straight for the produce section to grab some fresh vegetables, like bell peppers and zucchini. After that, I made my way to the meat department to pick up some chicken breasts.
    - British: Well, I popped down to the local shop just the other day to pick up a few bits and bobs. As I was perusing the aisles, I noticed that they were fresh out of biscuits, which was a bit of a disappointment, as I do love a good cuppa with a biscuit or two.

    Please start the email with a warm introduction. Add the introduction if you need to.
    
    Below is the email, tone, and dialect:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}
    
    YOUR {dialect} RESPONSE:
"""


# 读取环境变量 "OPENAI_API_KEY"
#openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = PromptTemplate(
	input_variables = ["tone","dialect","email"],
	template = template
)

def load_LLM(openai_api_key):
	"""Logic for loading the chain you want to use should go here."""
	llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
	return llm

#llm = load_LLM(openai_api_key)	


st.set_page_config(page_title="Globalize Email", page_icon=":robot:")
st.header("Globalize Text")

col1, col2 = st.columns(2)

with col1:
	st.markdown("often professionals would like to imporve their email.")
	
with col2:
	st.image(image = "TweetScreenshot.png",width=300,caption="drug")

st.markdown("## Enter Your Email To Convert")

co11, col2 = st.columns(2)

with co11:
	option_tone = st.selectbox(
		'Which tone would you like your email to have?',
		('Formal','Informal'))

with col2:
	option_dialect = st.selectbox(
		'Which English Dialect would you like',
		('American English','British English'))

def get_text():
	input_text = st.text_area(label="",placeholder="Your Email...",key="email_input")
	return input_text

email_input = get_text()

st.markdown("## Your Converted Email:")

if email_input:

    if not st.secrets["openai_api_key"]:
        st.warning('Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', icon="⚠️")
        st.stop()

    llm = load_LLM(openai_api_key=st.secrets["openai_api_key"])

    prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect, email=email_input)

    formatted_email = llm(prompt_with_email)

    st.write(formatted_email)
	
#git clone https://github.com/dawnguan123/REPOSITORY.git





