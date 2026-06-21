import streamlit as st

# Tiêu đề ứng dụng
st.title("💵 Ứng dụng tính Thuế Thu nhập cá nhân")
st.subheader("Nguyễn Ngọc Thanh Trúc")

# Nhập dữ liệu
thu_nhap = st.number_input(
    "Nhập tổng thu nhập hàng tháng (đồng)",
    min_value=0,
    value=30000000,
    step=100000
)

luong_bhxh = st.number_input(
    "Nhập mức lương đóng BHXH (đồng)",
    min_value=0,
    value=10000000,
    step=100000
)

nguoi_phu_thuoc = st.number_input(
    "Số người phụ thuộc",
    min_value=0,
    value=0,
    step=1
)

# Nút tính thuế
if st.button("Tính thuế"):

    # Bảo hiểm người lao động đóng (10,5%)
    bao_hiem = luong_bhxh * 0.105

    # Giảm trừ gia cảnh
    giam_tru_ban_than = 15500000
    giam_tru_phu_thuoc = 6200000 * nguoi_phu_thuoc

    # Thu nhập tính thuế
    thu_nhap_tinh_thue = (
        thu_nhap
        - bao_hiem
        - giam_tru_ban_than
        - giam_tru_phu_thuoc
    )

    if thu_nhap_tinh_thue < 0:
        thu_nhap_tinh_thue = 0

    # Thuế TNCN lũy tiến từng phần (theo biểu 5 bậc trong slide)
    if thu_nhap_tinh_thue <= 10000000:
        thue = thu_nhap_tinh_thue * 0.05

    elif thu_nhap_tinh_thue <= 30000000:
        thue = (
            10000000 * 0.05
            + (thu_nhap_tinh_thue - 10000000) * 0.10
        )

    elif thu_nhap_tinh_thue <= 60000000:
        thue = (
            10000000 * 0.05
            + 20000000 * 0.10
            + (thu_nhap_tinh_thue - 30000000) * 0.20
        )

    elif thu_nhap_tinh_thue <= 100000000:
        thue = (
            10000000 * 0.05
            + 20000000 * 0.10
            + 30000000 * 0.20
            + (thu_nhap_tinh_thue - 60000000) * 0.30
        )

    else:
        thue = (
            10000000 * 0.05
            + 20000000 * 0.10
            + 30000000 * 0.20
            + 40000000 * 0.30
            + (thu_nhap_tinh_thue - 100000000) * 0.35
        )

    # Thu nhập thực nhận
    thu_nhap_net = thu_nhap - bao_hiem - thue

    # Hiển thị kết quả
    st.success("KẾT QUẢ TÍNH TOÁN")

    st.write(f"📌 Tổng thu nhập: {thu_nhap:,.0f} đồng")

    st.write(
        f"📌 Bảo hiểm người lao động (10,5%): {bao_hiem:,.0f} đồng"
    )

    st.write(
        f"📌 Giảm trừ bản thân: {giam_tru_ban_than:,.0f} đồng"
    )

    st.write(
        f"📌 Giảm trừ người phụ thuộc: {giam_tru_phu_thuoc:,.0f} đồng"
    )

    st.write(
        f"📌 Thu nhập tính thuế: {thu_nhap_tinh_thue:,.0f} đồng"
    )

    st.write(
        f"📌 Thuế TNCN phải nộp: {thue:,.0f} đồng"
    )

    st.write(
        f"📌 Thu nhập thực nhận (NET): {thu_nhap_net:,.0f} đồng"
    )
