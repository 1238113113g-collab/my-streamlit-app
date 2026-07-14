import streamlit as st
# Lưu ý: Để chạy thực tế, bạn sẽ cần import thêm thư viện của Google:
# import google.generativeai as genai

# =========================================================================
# 1. CẤU HÌNH GIAO DIỆN CHÍNH
# =========================================================================
st.set_page_config(page_title="Trợ lý Báo cáo Đầu tư AI", layout="wide")

st.title("📊 Trợ lý Lập Báo cáo Đầu tư Tự động")
st.subheader("Tích hợp Trí tuệ Nhân tạo phân tích và trích xuất số liệu từ tài liệu")

# Chia giao diện làm 2 cột: Cột trái để tải tài liệu, Cột phải để ra lệnh và xem báo cáo
col1, col2 = st.columns([1, 2])

# =========================================================================
# 2. CỘT TRÁI: KHU VỰC TẬP HỢP TÀI LIỆU (Giống nguồn tài liệu trong NotebookLM)
# =========================================================================
with col1:
    st.header("📂 Nguồn tài liệu")
    
    # Cho phép tải lên nhiều định dạng tài liệu khác nhau
    uploaded_files = st.file_uploader(
        "Tải lên các tài liệu liên quan (PDF, Word, Excel, TXT):", 
        type=["pdf", "docx", "xlsx", "txt"], 
        accept_multiple_files=True
    )
    
    if uploaded_files:
        st.success(f"Đã nhận {len(uploaded_files)} tài liệu thành công!")
        # Hiển thị danh sách file đã tải lên để kiểm tra
        for file in uploaded_files:
            st.write(f"📄 {file.name} ({round(file.size/1024, 1)} KB)")

# =========================================================================
# 3. CỘT PHẢI: KHUNG ĐIỀU KHIỂN & KẾT QUẢ BÁO CÁO
# =========================================================================
with col2:
    st.header("✍️ Yêu cầu lập báo cáo")
    
    # Khung Prompt để bạn nhập yêu cầu lấy số liệu
    user_prompt = st.text_area(
        "Nhập yêu cầu phân tích của bạn:",
        placeholder="Ví dụ: Hãy tổng hợp doanh thu, lợi nhuận gộp qua các năm dưới dạng bảng. Sau đó đánh giá xu hướng tăng trưởng của dự án này...",
        height=150
    )
    
    # Nút bấm kích hoạt xử lý
    generate_button = st.button("🚀 Bắt đầu lập báo cáo tự động")
    
    # =========================================================================
    # 4. LOGIC XỬ LÝ KHI BẤM NÚT (Gửi tài liệu + Prompt sang AI)
    # =========================================================================
    if generate_button:
        if not uploaded_files:
            st.warning("Vui lòng tải lên ít nhất một tài liệu ở cột bên trái!")
        elif not user_prompt:
            st.warning("Vui lòng nhập yêu cầu lập báo cáo vào khung!")
        else:
            with st.spinner("Đang đọc tài liệu và phân tích số liệu... Vui lòng đợi trong giây lát..."):
                
                # CHỖ NÀY LÀ NƠI KẾT NỐI VỚI AI (BẰNG GEMINI API)
                # Hệ thống sẽ:
                # 1. Đọc nội dung từ các file trong `uploaded_files`
                # 2. Gộp nội dung file chung với câu lệnh `user_prompt` của bạn.
                # 3. Gửi sang Gemini và nhận kết quả phản hồi về.
                
                # Đoạn text giả định kết quả trả về từ AI để bạn hình dung giao diện:
                ket_qua_gia_dinh = f"""
                ### 📈 KẾT QUẢ PHÂN TÍCH ĐẦU TƯ TỰ ĐỘNG
                
                Dựa trên các tài liệu bạn đã cung cấp, dưới đây là báo cáo trích xuất theo yêu cầu:
                
                #### 1. Bảng số liệu trích xuất:
                | Năm | Doanh thu (Tỷ VND) | Lợi nhuận (Tỷ VND) | Biên lợi nhuận |
                |---|---|---|---|
                | 2023 | 120 | 18 | 15% |
                | 2024 | 150 | 25 | 16.7% |
                | 2025 (Dự kiến) | 200 | 36 | 18% |
                
                #### 2. Đánh giá xu hướng:
                * **Tăng trưởng bền vững:** Doanh thu duy trì mức tăng trưởng trung bình trên 25%/năm.
                * **Cải thiện hiệu quả:** Biên lợi nhuận gộp cải thiện rõ rệt nhờ tối ưu hóa chi phí vận hành.
                
                *Nội dung được phân tích tự động dựa trên yêu cầu: "{user_prompt}"*
                """
                
                # Hiển thị kết quả ra màn hình web
                st.markdown("---")
                st.markdown(ket_qua_gia_dinh)
                st.balloons() # Hiệu ứng bóng bay chúc mừng khi hoàn thành
