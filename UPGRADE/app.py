import streamlit as st
import requests

# タイトルを設定
st.title("🤖 AI面接官")

# 1. 初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. 履歴表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. 入力と履歴追加
if prompt := st.chat_input("メッセージを送信"):
    # ユーザーの入力を保存＆表示
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- 以下、API通信 ---
    api_url = "https://api.dify.ai/v1/chat-messages"
    headers = {
      "Authorization": f"Bearer {api_key}",
      "Content-Type": "application/json"
    }
    data = {
      "inputs": {},
      "query": prompt,
      "user": "my-first-user",
      "response_mode": "blocking"
    }
    response = requests.post(api_url, headers=headers, json=data)
    ai_message = response.json()["answer"]
    # --- ここまで ---

    # AIの返答を保存＆表示（オウム返し→APIレスポンスに変更）
    st.session_state.messages.append({"role": "assistant", "content": ai_message})
    with st.chat_message("assistant"):
        st.markdown(ai_message)
