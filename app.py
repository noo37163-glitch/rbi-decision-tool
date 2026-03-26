import streamlit as st

st.title("RBI CA / CC / OD Decision Tool (Fully Compliant Version)")

# Inputs
total_exp = st.number_input("Total Exposure (₹ Cr)", min_value=0.0)
total_fb = st.number_input("Total Fund-Based Exposure (₹ Cr)", min_value=0.0)
bank_exp = st.number_input("Your Bank Exposure (₹ Cr)", min_value=0.0)
bank_fb = st.number_input("Your Bank FB Exposure (₹ Cr)", min_value=0.0)

nfb = st.selectbox("Only NFB Exposure?", ["Yes", "No"])

if st.button("Get Decision"):

    # -------------------------
    # CASE 1: < ₹10 Cr
    # -------------------------
    if total_exp < 10:
        st.success("✅ CA: YES | CC: YES | OD: YES")

        st.info("Reason: Total Exposure < ₹10 Cr (No restriction as per RBI)")

        st.warning("""
Compliance Advisory:
- Verify KYC and customer profile
- Check internal bank onboarding policy
""")

    else:

        # -------------------------
        # CASE 2: Only NFB
        # -------------------------
        if nfb == "Yes":
            st.success("✅ CA: YES | CC: YES | OD: YES")

            st.info("Reason: Only Non-Fund Based Exposure")

            st.warning("""
Compliance Advisory:
- Ensure no hidden fund-based exposure
- Monitor if borrower avails FB limits later
""")

        else:

            # -------------------------
            # Calculate Shares
            # -------------------------
            total_share = (bank_exp / total_exp * 100) if total_exp > 0 else 0
            fb_share = (bank_fb / total_fb * 100) if total_fb > 0 else 0

            total_flag = total_share >= 10
            fb_flag = fb_share >= 10

            # -------------------------
            # CASE 3: Eligible (≥10%)
            # -------------------------
            if total_flag or fb_flag:

                st.success("✅ CA: YES | CC: YES | OD: YES")

                st.info(f"""
Reason:

✔ Total Exposure Share: {total_share:.2f}% {'(≥10%)' if total_flag else '(<10%)'}
✔ Fund-Based Share: {fb_share:.2f}% {'(≥10%)' if fb_flag else '(<10%)'}

Rule: ≥10% in Total OR Fund-Based Exposure
""")

                st.warning("""
Compliance Advisory:
- Check consortium / multiple banking arrangement
- Obtain lender confirmation if required
- Ensure proper cash flow routing
- Follow internal credit policy
""")

            # -------------------------
            # CASE 4: Not Eligible (<10%)
            # -------------------------
            else:

                st.error("❌ CA: NOT ALLOWED | OD: NOT ALLOWED | CC: YES")

                st.info(f"""
Reason:

✘ Total Exposure Share: {total_share:.2f}% (<10%)
✘ Fund-Based Share: {fb_share:.2f}% (<10%)

Rule: Less than 10% → Cannot maintain CA/OD
""")

                st.warning("""
Conditional Possibility:
- CA may be opened ONLY with NOC from existing lenders
- Subject to bank internal approval

Else:
- Open Collection Account only
- No free debit allowed
- Funds to be routed to main lending bank (typically within 2 days)

Compliance Advisory:
- Mandatory to check lender structure
- Confirm arrangement before onboarding
- Follow RBI cash flow discipline strictly
""")
