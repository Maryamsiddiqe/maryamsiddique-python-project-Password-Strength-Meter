import streamlit as st
import re
import random
import string

# Custom Styling for Responsive Design
st.markdown("""
    <style>
        .stApp {
            background-color: #E6E6FA;
        }
        .main {
            background-color: #E6E6FA;
            padding: 20px;
            border-radius: 10px;
        }
        .title {
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
        }
        .weak { color: red; font-weight: bold; }
        .moderate { color: orange; font-weight: bold; }
        .strong { color: green; font-weight: bold; }
        .suggestions {
            background-color: #f8f9fa;
            padding: 10px;
            border-radius: 5px;
        }
        .footer {
            text-align: center;
            font-size: 1.2em;
            font-weight: bold;
            margin-top: 40px;
            color: black;
            font-family: 'Courier New', Courier, monospace;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .title { font-size: 2em; }
            .footer { font-size: 1em; }
        }
        @media (max-width: 480px) {
            .title { font-size: 1.8em; }
            .footer { font-size: 0.9em; }
        }
    </style>
""", unsafe_allow_html=True)

# Password Strength Checker Function
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]", password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")
    
    return score, feedback

# Password Generator
def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+{}[]:;<>,.?~"
    return ''.join(random.choice(characters) for _ in range(12))

# UI Elements
st.markdown('<h1 class="title">🔐 Password Strength Meter</h1>', unsafe_allow_html=True)
st.write("Enter your password below to check its security level. 🔍")
password = st.text_input("Enter your password here:", type="password")

if st.button("Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)

        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Please make your password stronger! ")
        
        if feedback:
            st.markdown('<div class="suggestions"><strong>📢 Improve Your Password :</strong></div>', unsafe_allow_html=True)
            for item in feedback:
                st.write(f"❌ {item}")

if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.markdown(f"<div class='strong'>💡 Try this strong password: `{strong_password}`</div>", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">✨ Developed by Maryam Siddique ✨</div>', unsafe_allow_html=True)
