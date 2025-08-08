import streamlit as st
from backend.explain import explain_code

st.set_page_config(page_title="AI Code Explainer")
st.title("🤖 AI Code Explainer")

language = st.selectbox("Select Language", ["python", "javascript", "c", "java", "cpp"])
code = st.text_area("Paste your code here:", height=300)

if st.button("Explain Code"):
    if code.strip():
        with st.spinner("Explaining..."):
            explanation = explain_code(code, language)
            st.markdown("### 📝 Explanation:")
            st.success(explanation)
    else:
        st.warning("Please paste some code first.")
