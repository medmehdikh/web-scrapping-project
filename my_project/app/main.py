from fastapi import FastAPI
from app.scraper import scrape_peugeot_2008
import json
import os

app = FastAPI()

# Define the file path for the scraped data
DATA_FILE = "data/peugeot_2008_annonces.json"

# Function to load the saved data
def load_annonces():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []  # Return an empty list if file doesn't exist or is empty

# Endpoint to get the scraped data
@app.get("/annonces")
def get_annonces():
    annonces = load_annonces()
    return annonces

# Endpoint to start the scraping process
@app.post("/scrape")
def scrape_data():
    try:
        scrape_peugeot_2008()  # Trigger the scraping function
        return {"message": "Scraping started!"}
    except Exception as e:
        return {"message": f"An error occurred during scraping: {str(e)}"}
