import os
import openai
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_llm_response(user_text: str, expert_type: str) -> str:
    system_messages = {
        "料理専門家": "あなたは料理の専門家です。",
        "プログラミング専門家": "あなたはプログラミングの専門家です。",
        "旅行専門家": "あなたは旅行の専門家です。"
    }
    prompt = f"{system_messages.get(expert_type)}\nユーザー: {user_text}\nアシスタント:"
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

st.title("専門家チャットアプリ")
st.write("""
このアプリでは、入力したテキストを LangChain 経由で LLM に送信し、  
選択した専門家タイプの観点で回答を生成します。
""")
expert_choice = st.radio("質問する専門家のタイプを選択してください。", ["料理専門家", "プログラミング専門家", "旅行専門家"])
user_input = st.text_input("質問内容を入力してください。")

if st.button("送信"):
    if user_input:
        answer = get_llm_response(user_input, expert_choice)
        st.write("### 回答結果")
        st.write(answer)
    else:
        st.error("質問内容を入力してください。")