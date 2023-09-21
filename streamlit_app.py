# Streamlitライブラリをインポート
import streamlit as st
import ramdom

st.title("おみくじアプリ")
if st.button("おみくじを引く"):
    results = ["大吉","中吉","小吉","吉","凶","大凶"]
    results = ramdom.choice(results)
    st.write(f"結果:{results}")


