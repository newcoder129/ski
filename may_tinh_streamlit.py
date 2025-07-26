
import streamlit as st

st.title("🧮 Máy Tính Mini")

# Nhập dữ liệu từ người dùng
so1 = st.number_input("Chọn số thứ nhất:", format="%.2f")
phep_tinh = st.selectbox("Chọn phép tính:", ["+", "-", "*", "/"])
so2 = st.number_input("Chọn số thứ hai:", format="%.2f")

# Tính toán khi người dùng bấm nút
if st.button("Tính kết quả"):
    if phep_tinh == "+":
        ket_qua = so1 + so2
        st.success(f"Kết quả là: {ket_qua}")
    elif phep_tinh == "-":
        ket_qua = so1 - so2
        st.success(f"Kết quả là: {ket_qua}")
    elif phep_tinh == "*":
        ket_qua = so1 * so2
        st.success(f"Kết quả là: {ket_qua}")
    elif phep_tinh == "/":
        if so2 != 0:
            ket_qua = so1 / so2
            st.success(f"Kết quả là: {ket_qua}")
        else:
            st.error("Không thể chia cho 0!")
