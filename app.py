import streamlit as st

st.title("💵 Ứng dụng tính Thuế Thu nhập cá nhân")

# Nhập dữ liệu
thu_nhap = st.number_input(
    "Nhập thu nhập hàng tháng (triệu đồng)",
    min_value=0.0,
    value=20.0
)

nguoi_phu_thuoc = st.number_input(
    "Số người phụ thuộc",
    min_value=0,
    value=0
)

if st.button("Tính thuế"):

    # ===== BẢO HIỂM =====
    bhxh = thu_nhap * 0.08
    bhyt = thu_nhap * 0.015
    bhtn = thu_nhap * 0.01

    tong_bao_hiem = bhxh + bhyt + bhtn

    # ===== GIẢM TRỪ GIA CẢNH =====
    giam_tru_ban_than = 11
    giam_tru_phu_thuoc = 4.4 * nguoi_phu_thuoc

    # ===== THU NHẬP TÍNH THUẾ =====
    thu_nhap_tinh_thue = (
        thu_nhap
        - tong_bao_hiem
        - giam_tru_ban_than
        - giam_tru_phu_thuoc
    )

    if thu_nhap_tinh_thue <= 0:
        thue = 0

    elif thu_nhap_tinh_thue <= 5:
        thue = thu_nhap_tinh_thue * 0.05

    elif thu_nhap_tinh_thue <= 10:
        thue = 5 * 0.05 + (thu_nhap_tinh_thue - 5) * 0.10

    elif thu_nhap_tinh_thue <= 18:
        thue = (
            5 * 0.05
            + 5 * 0.10
            + (thu_nhap_tinh_thue - 10) * 0.15
        )

    elif thu_nhap_tinh_thue <= 32:
        thue = (
            5 * 0.05
            + 5 * 0.10
            + 8 * 0.15
            + (thu_nhap_tinh_thue - 18) * 0.20
        )

    elif thu_nhap_tinh_thue <= 52:
        thue = (
            5 * 0.05
            + 5 * 0.10
            + 8 * 0.15
            + 14 * 0.20
            + (thu_nhap_tinh_thue - 32) * 0.25
        )

    elif thu_nhap_tinh_thue <= 80:
        thue = (
            5 * 0.05
            + 5 * 0.10
            + 8 * 0.15
            + 14 * 0.20
            + 20 * 0.25
            + (thu_nhap_tinh_thue - 52) * 0.30
        )

    else:
        thue = (
            5 * 0.05
            + 5 * 0.10
            + 8 * 0.15
            + 14 * 0.20
            + 20 * 0.25
            + 28 * 0.30
            + (thu_nhap_tinh_thue - 80) * 0.35
        )

    # ===== LƯƠNG THỰC NHẬN =====
    luong_net = thu_nhap - tong_bao_hiem - thue

    st.success("Kết quả tính thuế")

    st.write(f"📌 BHXH (8%): {bhxh:.2f} triệu đồng")
    st.write(f"📌 BHYT (1.5%): {bhyt:.2f} triệu đồng")
    st.write(f"📌 BHTN (1%): {bhtn:.2f} triệu đồng")
    st.write(f"📌 Tổng bảo hiểm: {tong_bao_hiem:.2f} triệu đồng")

    st.write(
        f"📌 Thu nhập tính thuế: **{thu_nhap_tinh_thue:.2f} triệu đồng**"
    )

    st.write(
        f"📌 Thuế TNCN phải nộp: **{thue:.2f} triệu đồng/tháng**"
    )

    st.write(
        f"📌 Lương thực nhận (NET): **{luong_net:.2f} triệu đồng/tháng**"
    )
