import streamlit as st
import google.generativeai as genai

st.title("Email Summarizer (Bullet Points)")

# Configure Gemini
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

# Input box
email_body = st.text_area("Paste the email body here")

# Button
if st.button("Summarize"):
    prompt = f"Summarize this email into 3-5 bullet points:\n{email_body}"
    response = model.generate_content(prompt)

    st.write("### Summary:")
    st.write(response.text)   # Gemini already returns bullets nicely
