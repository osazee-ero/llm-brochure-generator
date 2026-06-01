# AI Brochure Generator

An AI-powered brochure generator that scrapes and navigates company websites, extracts useful information, and generates a professional company brochure using Large Language Models.

## Project Overview

This project is part of my LLM Engineering portfolio. The goal is to build an application that can visit a company website, understand the important pages, extract relevant content, and generate a clean brochure-style summary.

## Problem

Companies often have useful information spread across many website pages, such as About, Careers, Products, Services, and Contact pages. Manually collecting and rewriting this information into a brochure can be slow.

## Solution

This app uses web scraping and LLMs to:

1. Visit a company website
2. Identify useful links
3. Extract relevant text from selected pages
4. Generate a professional brochure
5. Display the result in a simple app interface

## Planned Features

- Website scraping
- Intelligent link selection
- Brochure generation using LLMs
- Streamlit user interface
- Markdown brochure output
- Error handling for invalid websites
- Optional export to text or PDF

## Tech Stack

- Python
- OpenAI API
- BeautifulSoup
- Requests
- Streamlit
- GitHub
- GitHub Pages

## Project Structure

```text
llm-brochure-generator/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── src/
│   ├── scraper.py
│   ├── brochure_generator.py
│   └── utils.py
├── notebooks/
├── screenshots/
└── examples/

```

## How to Run
git clone https://github.com/ememosazee19991990/llm-brochure-generator.git
cd llm-brochure-generator
pip install -r requirements.txt
streamlit run app.py


## Status

Core version completed.

Current features:

- Scrapes a company homepage
- Finds relevant internal links such as About, Products, Services, Careers, and Contact pages
- Extracts clean website text
- Uses an LLM to generate a professional brochure
- Displays the brochure in a Streamlit app
- Allows the brochure to be downloaded as a Markdown file

## What I Learned

Through this project, I practiced:

- Building an LLM-powered application with Python
- Scraping and cleaning website content
- Selecting useful internal links from a company website
- Using environment variables safely for API keys
- Creating a simple Streamlit user interface
- Structuring a project for GitHub and portfolio presentation
- Adding downloadable AI-generated output

## Application Workflow

```text
User enters company name and website URL
        ↓
App scrapes the homepage
        ↓
App finds useful internal links
        ↓
App extracts clean text from selected pages
        ↓
LLM generates a company brochure
        ↓
User views and downloads the brochure
