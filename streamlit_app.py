import streamlit as st

st.title("Chào mừng đến với Website của tôi!")
st.write("Trang web này được tạo bằng Streamlit và lưu trữ trên GitHub.")
import streamlit as st

# 1. Tiêu đề trang web
st.title("Ứng dụng thử nghiệm của Giang")

# 2. Tạo một khung nhập liệu (như khung Prompt)
user_input = st.text_input("Nhập yêu cầu hoặc câu hỏi của bạn vào đây:")

# 3. Tạo một nút bấm
if st.button("Gửi đi"):
    # 4. Xử lý khi người dùng nhấn nút
    st.write(f"Bạn vừa yêu cầu: **{user_input}**")
    st.success("Yêu cầu của bạn đã được ghi nhận thành công!")
