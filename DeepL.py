# Cross-Thread Fix
from gevent import monkey
monkey.patch_all()

import re
import time

from playwright.sync_api import sync_playwright
from flask import Flask, request, jsonify

app = Flask(__name__)

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=True)
context = browser.new_context()

page = context.new_page()
page.goto("https://www.deepl.com/translator")

@app.route('/translate', methods=['POST'])
def translate_api():
    # Cache JSON Received
    data = request.json

    # Check JSON Validity
    if 'text' not in data or 'lang' not in data:
        return jsonify({'error': 'Invalid JSON data'}), 400
    
    # Cache Values
    input_text = data['text']
    lang = data['lang']

    # Check If Any Text Was Given# Check If Any Text Was Given
    if not input_text:
        return jsonify({'error': 'Empty input text'}), 400
    
    # Check If Any Lang Was Given
    if not lang:
        return jsonify({'error': 'Empty lang'}), 400
    
    # Translate The Text According To The Provided Lang
    translated_text = translate(input_text, lang)

    # Return The Result Back To The Client
    return jsonify({'translated_text': translated_text}), 200

def translate(input_text: str, lang: str) -> str:
    # Select The Target Language
    if not page.get_by_test_id("translator-target-lang-btn").inner_text().endswith(lang):
        page.get_by_role("button", name=re.compile("Select target language", re.IGNORECASE)).click()
        page.get_by_role("option", name=lang).click()

    # Fill In Our Text For Translating, Caching For Optimization, Filling Blank First For While Loop Later To Work
    sourcebox = page.get_by_role("textbox", name="Source text")
    sourcebox.click()
    sourcebox.fill("")
    sourcebox.fill(input_text)

    # Cache Translation Output TextBox
    outputbox = page.get_by_test_id("translator-target-input")

    # Wait For Translation To Finish By Waiting For Length > 0 And It Not To Be The Empty Newline DeepL Initializes It With
    while len(outputbox.inner_text()) == 0 or outputbox.inner_text() == '\n':
        time.sleep(1)

    # Return Translation
    return outputbox.inner_text()

app.run()