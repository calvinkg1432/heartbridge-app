import streamlit as st
import openai  # 或者是 google-genai，取決於您用哪家 API

st.title("❤️ 跨越語言的心橋 (HeartBridge)")
st.write("在這裡，無論你用什麼語言，你的心碎都有人傾聽。")

# 初始化對話歷史紀錄 (Streamlit 內建的 Session State)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 顯示之前的對話
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 接收使用者輸入
if user_input := st.chat_input("用你的母語聊聊吧..."):
    # 顯示使用者說的話
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 呼叫 AI (這裡以 OpenAI 為例，您可以換成 Gemini API)
    # 在這裡設定您的 System Prompt 
    system_prompt = "你是溫暖的跨語言情感諮詢師。請完全以使用者的『母語』回覆，給予同理心。回覆末尾用括號附上中文翻譯。"
    
    # 模擬 AI 回應 (實際運作時需串接 openai.chat.completions.create)
    with st.chat_message("assistant"):
        ai_response = "（AI 會自動偵測語言並在這裡給予溫暖的回覆...）"
        st.write(ai_response)
        
    st.session_state.messages.append({"role": "assistant", "content": ai_response})