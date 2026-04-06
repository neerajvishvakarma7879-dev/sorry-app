import streamlit as st
import time
import random

st.set_page_config(page_title="For My Love 💖 My Sunshine ❤️", page_icon="💖")

# Page state
if "page" not in st.session_state:
    st.session_state.page = 0

def next_page():
    st.session_state.page += 1

# Typing effect
def type_text(text):
    display = st.empty()
    typed = ""
    for char in text:
        typed += char
        display.markdown(f"<h3 style='text-align:center;'>{typed}</h3>", unsafe_allow_html=True)
        time.sleep(0.02)

# Function for right corner button
def next_button():
    st.write("")
    st.write("")
    col1, col2, col3 = st.columns([6, 1, 1])
    with col3:
        st.button("Next ➡️", on_click=next_page)

# ---------------- PAGE 0 ----------------
if st.session_state.page == 0:
    st.markdown("<h1 style='text-align:center; color:red;'>Hii mera betuuu ❤️</h1>", unsafe_allow_html=True)
    
    type_text("I made something special just for you... 💖")
    time.sleep(1)
    type_text("Please go through this till the end 🥺")

    next_button()

# ---------------- PAGE 1 ----------------
elif st.session_state.page == 1:
    st.title("I Am Sorry My baby 💔")

    type_text("I never wanted to hurt you...")
    time.sleep(2)

    st.write("""
    🥺 I made a mistake  
    💔 I hurt you for little things 
    😔 I Forgot your likes
 

    But You mean everything to me ❤️
    """)

    next_button()

# ---------------- PAGE 2 ----------------
elif st.session_state.page == 2:
    st.title("I Promises I Will 💖")

    promises = [
        "Listen to you more 💞",
        "Respect your feelings 🌸",
        "Never repeat this mistake 🙏",
        "Always try to make you smile 😊"
    ]

    for p in promises:
        type_text(p)
        time.sleep(0.5)

    st.balloons()
    next_button()

# ---------------- PAGE 3 ----------------
elif st.session_state.page == 3:
    st.title("Sachhi dil se bolu toh 💌")

    type_text("You are my happiness 😊")
    time.sleep(1)
    type_text("My peace 💖")
    time.sleep(1)
    type_text("My everything ❤️")

    next_button()

# ---------------- PAGE 4 ----------------
elif st.session_state.page == 4:
    st.title("please maaf kar de betuuu🥺")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Kar diya  💕"):
            st.balloons()
            type_text("Thank you so much bachha 😭❤️")
            time.sleep(1)
            type_text("I love you so much my sunshine my love love so muchhhh 😘😘😘 💖")
            
            st.balloons()
            next_button()

    with col2:
        if st.button("Nahi 😢"):
            msgs = [
                "Please kar dena 🥺",
                "maan ja betuu mera pyara bachhha   🙏",
                "aage se hamesha dhyan rakhunga ❤️",
                "please kar de betuuu you are my everything  💕"
                "😭😭😭😭😭😭😭😭🥺"
            ]
            st.warning(random.choice(msgs))