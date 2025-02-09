import streamlit as st
import pyotp


def generate_totp(secret):
    totp = pyotp.TOTP(secret)
    return totp.now()


def main():
    st.title("TOTP Generator")

    secret = st.text_input("Enter Secret Key")
    if st.button("Generate TOTP"):
        if secret:
            totp_code = generate_totp(secret)
            st.success(f"Your TOTP Code: {totp_code}")
        else:
            st.error("Please enter a secret key.")


if __name__ == "__main__":
    main()
