import streamlit as st

from src.scraper import scrape_website
from src.brochure_generator import generate_brochure


st.set_page_config(
    page_title="AI Brochure Generator",
    page_icon="📄",
    layout="wide"
)


st.title("AI Brochure Generator")

st.write(
    """
    This app generates a professional company brochure by reading and analyzing
    content from a company website.
    """
)


company_name = st.text_input("Company name", placeholder="Example: Hugging Face")
company_url = st.text_input("Company website URL", placeholder="https://www.example.com")


if st.button("Generate Brochure"):
    if not company_name or not company_url:
        st.warning("Please enter both the company name and website URL.")
    else:
        try:
            with st.spinner("Scraping website..."):
                website_text = scrape_website(company_url)

            st.success("Website scraped successfully.")

            with st.spinner("Generating brochure..."):
                brochure = generate_brochure(
                    company_name=company_name,
                    website_url=company_url,
                    website_text=website_text
                )

            st.success("Brochure generated successfully.")

            st.markdown("## Generated Brochure")
            st.markdown(brochure)

            st.download_button(
                label="Download Brochure as Markdown",
                data=brochure,
                file_name=f"{company_name.lower().replace(' ', '_')}_brochure.md",
                mime="text/markdown"
            )

        except Exception as error:
            st.error(f"Something went wrong: {error}")