# Streamlitライブラリをインポート
import streamlit as st
import random
st.title("おみくじアプリ")
if st.button("おみくじを引く"):
    results = ["ロシア","中国","北朝鮮","ソマリア","アゼルバイジャン","アフガニスタン","ブリカス","ミャンマー"]
    result = random.choice(results)
    st.write(f"私の出身地は:{result}です。")
