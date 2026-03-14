# Simple Web Scraper

A small Python script for parsing web pages. It extracts article titles, links, and brief descriptions (if available) from a page and saves the results to a CSV file.

The script automatically tries to identify articles by analyzing common HTML structures (`article`, `h1`, `h2`, `h3`).

---

## Features

- Extraction of article titles
- Collection of page links
- Attempt to extract brief descriptions (summary)
- Filtering of invalid links (`login`, `mailto`, `javascript`, etc.)
- Saving results to CSV
- Works with most blogs and news websites

---

## Example Result

title,url,summary
Local AI Assistant: Installing OpenClaw with Ollama in 2 Steps,https://example.com/article1,N/A
How Modern Databases Work,https://example.com/article2,This article explains how modern databases handle data...
Building a CLI Tool in Python,https://example.com/article3,N/A

## Installation

Install the required dependencies:

pip install requests beautifulsoup4


## Usage

Run the script and pass the page URL:

python webscraper.py https://yoursite.com

After execution, a file yourname.csv will appear with the results.

## License

This project is distributed under the MIT License. See the LICENSE file for details.
