import streamlit as st


st.set_page_config(
    page_title="AI Brochure Generator",
    page_icon="📄",
    layout="wide"
)


st.title("AI Brochure Generator")

st.write(
    """
    This app will generate a professional company brochure by reading and
    analyzing content from a company website.
    """
)


company_name = st.text_input("Company name", placeholder="Example: Hugging Face")
company_url = st.text_input("Company website URL", placeholder="https://www.example.com")


if st.button("Generate Brochure"):
    if not company_name or not company_url:
        st.warning("Please enter both the company name and website URL.")
    else:
        st.info("Brochure generation logic will be added soon.")
        st.write(f"Company: {company_name}")
        st.write(f"Website: {company_url}")
