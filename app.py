# app.py
from flask import Flask, render_template, request
from scraper import scrape_url, summarize_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    error = None
    if request.method == 'POST':
        url = request.form.get('url')
        print("Received POST request with URL:", url)  # Debug print
        if url:
            scraped_text = scrape_url(url)
            print("Scraping complete.")  # Debug print
            if scraped_text.startswith("Error occurred"):
                error = scraped_text
            elif not scraped_text:
                error = "No text found on the page to summarize."
            else:
                summary = summarize_text(scraped_text)
                print("Summarization complete.")  # Debug print
    return render_template('index.html', summary=summary, error=error)

if __name__ == '__main__':
    app.run(debug=True)