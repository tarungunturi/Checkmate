
import streamlit as st
from textblob import TextBlob
from gingerit.gingerit import GingerIt


st.set_page_config(page_title='Check mate ',page_icon="🔎")

st.title("Welcome to Check mate!")
st.sidebar.title("Made by")
st.sidebar.subheader("Balaji 181B069")
st.sidebar.subheader("Tarun 181B228")
st.sidebar.subheader("Vibhum 181B237")


st.write("Checkmate is a web app that detects spelling mistakes and performs corrections automatically. This can also serve as a Spell checker along with correcting grammatical errors. 🔎")

user_input= st.text_input("Enter your input") #input box

if not user_input:
  st.warning("Expected output will be displayed here ")





#a = "wasi releasede in 2000 refrenece "
# incorrect spelling
#print("original text: "+str(a))

b = TextBlob(user_input)
b1=str(b.correct())
corrected_text = GingerIt().parse(b1)
final_ans=corrected_text['result']

st.info(final_ans)



