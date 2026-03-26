import streamlit as st

st.title("RBI CA / CC / OD Decision Tool")

total_exp = st.number_input("Total Exposure (₹ Cr)", min_value=0.0)
total_fb = st.number_input("Total Fund-Based Exposure (₹ Cr)", min_value=0.0)
bank_exp = st.number_input("Your Bank Exposure (₹ Cr)", min_value=0.0)
bank_fb = st.number_input("Your Bank FB Exposure (₹ Cr)", min_value=0.0)

lending = st.selectbox("Are you a Lending Bank?", ["Yes", "No"])
nfb = st.selectbox("Only NFB Exposure?", ["Yes", "No"])

if st.button("Get Decision"):

    if total_exp < 10:
        result = "CA: YES | CC: YES | OD: YES"
        reason = "Exposure < ₹10 Cr"

    elif nfb == "Yes":
        result = "CA: YES | CC: YES | OD: YES"
        reason = "Only NFB Exposure"

    elif lending != "Yes":
        result = "CA: NO | CC: NO | OD: NO"
        reason = "Not a Lending Bank"

    else:
        total_share = bank_exp / total_exp if total_exp > 0 else 0
        fb_share = bank_fb / total_fb if total_fb > 0 else 0

        if total_share >= 0.10 or fb_share >= 0.10:
            result = "CA: YES | CC: YES | OD: YES"
            reason = "≥10% Exposure"
        else:
            result = "CA: NO | OD: NO | CC: YES"
            reason = "<10% Exposure (Use Collection A/c)"

    st.success(result)
    st.info("Reason: " + reason)
