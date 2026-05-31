import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

MODEL = "gpt-5.5"


def generate_brochure(company_name: str, website_url: str, website_text: str) -> str:
    """
    Generate a professional brochure from company website text.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY was not found. Please check your .env file.")

    client = OpenAI(api_key=api_key)

    prompt = f"""
    You are a professional marketing writer.

    Create a clear, polished company brochure for the company below.

    Company name: {company_name}
    Website: {website_url}

    Use the website content below to write the brochure.

    The brochure should include:
    - A strong title
    - A short company overview
    - Main products or services
    - Target customers
    - Key strengths
    - Why someone should choose this company
    - A short closing paragraph

    Write in markdown format.

    Website content:
    {website_text[:12000]}
    """

    response = client.responses.create(
        model=MODEL,
        input=prompt,
    )

    return response.output_text