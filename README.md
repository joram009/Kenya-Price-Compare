# Kenya Price Comparison Tool 🛒

An AI-powered price comparison tool that automatically scrapes 
multiple Kenyan shopping sites and uses AI to analyse prices 
and recommend the best value products.

## Features
- Scrapes product names, prices and links automatically
- Supports multiple Kenyan shopping sites
  - Jumia Kenya
  - Kilimall
- AI powered analysis using local Ollama models
- Recommends cheapest and best value products
- Clean formatted results

## How It Works
1. User enters a product name
2. Scraper fetches results from all supported sites
3. Data saved to local file
4. AI analyses prices and recommends best value
5. Results printed to terminal

## Installation

1. Clone the repository:
git clone https://github.com/joram009/kenya-price-compare.git

2. Install dependencies:
pip install -r requirements.txt

3. Install Playwright browsers:
playwright install

4. Install and run Ollama:
Download from ollama.com
ollama pull phi3:mini

## Usage
python jumia_seo.py

## Project Structure
- jumia_seo.py - Main entry point
- the_scarper.py - Web scraping modules
- main.py - AI summariser
- config.py - Configuration and file paths

## Technologies Used
- Python
- BeautifulSoup
- Playwright
- Ollama (phi3:mini)
- Requests

## Author
Joram Onsoti
Nairobi, Kenya
github.com/joram009
