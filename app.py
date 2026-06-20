import streamlit as st

# Tiêu đề ứng dụng

st.title("💵 Ứng dụng tính Thuế Thu nhập cá nhân -  Thanh Tru")

# Nhập dữ liệu
thu_nhap = st.number_input(
    "Nhập thu nhập hàng tháng (triệu đồng)",
    min_value=0.0,
    value=30.0
)

nguoi_phu_thuoc = st.number_input(
    "Số người phụ thuộc",
    min_value=0,
    value=0
)

# Nút tính toán
if st.button("Tính thuế"):

    # Bảo hiểm bắt buộc
    bao_hiem = thu_nhap * 0.105

    # Giảm trừ gia cảnh
    giam_tru_ban_than = 15.5
    giam_tru_phu_thuoc = 6.2 * nguoi_phu_thuoc

    # Thu nhập tính thuế
    thu_nhap_tinh_thue = (
        thu_nhap
        - bao_hiem
        - giam_tru_ban_than
        - giam_tru_phu_thuoc
    )

    if thu_nhap_tinh_thue < 0:
        thu_nhap_tinh_thue = 0

    # Tính thuế lũy tiến từng phần
    if thu_nhap_tinh_thue <= 10:
        thue = thu_nhap_tinh_thue * 0.05

    elif thu_nhap_tinh_thue <= 30:
        thue = (
            10 * 0.05
            + (thu_nhap_tinh_thue - 10) * 0.10
        )

    elif thu_nhap_tinh_thue <= 60:
        thue = (
            10 * 0.05
            + 20 * 0.10
            + (thu_nhap_tinh_thue - 30) * 0.20
        )

    elif thu_nhap_tinh_thue <= 100:
        thue = (
            10 * 0.05
            + 20 * 0.10
            + 30 * 0.20
            + (thu_nhap_tinh_thue - 60) * 0.30
        )

    else:
        thue = (
            10 * 0.05
            + 20 * 0.10
            + 30 * 0.20
            + 40 * 0.30
            + (thu_nhap_tinh_thue - 100) * 0.35
        )

    # Lương thực nhận
    luong_net = thu_nhap - bao_hiem - thue

    # Hiển thị kết quả
    st.success("KẾT QUẢ TÍNH TOÁN")

    st.write(
        f"📌 Bảo hiểm bắt buộc (10,5%): {bao_hiem:.2f} triệu đồng"
    )

    st.write(
        f"📌 Giảm trừ bản thân: {giam_tru_ban_than:.2f} triệu đồng"
    )

    st.write(
        f"📌 Giảm trừ người phụ thuộc: {giam_tru_phu_thuoc:.2f} triệu đồng"
    )

    st.write(
        f"📌 Thu nhập tính thuế: {thu_nhap_tinh_thue:.2f} triệu đồng"
    )

    st.write(
        f"📌 Thuế TNCN phải nộp: {thue:.2f} triệu đồng"
    )

    st.write(
        f"📌 Lương thực nhận (NET): {luong_net:.2f} triệu đồng"
    )
