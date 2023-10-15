# Cross-Thread Fix
from gevent import monkey
monkey.patch_all()

import re
import time
import json

from playwright.sync_api import sync_playwright
from flask import Flask, request

app = Flask(__name__)

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context()

page = context.new_page()
page.goto("https://www.deepl.com/translator")

def makejson(obj):
    # Serialize the object to a JSON-formatted string
    return json.dumps(obj, ensure_ascii=False, indent=2)

@app.route('/translate', methods=['POST'])
def translate_api():
    # Cache JSON Received
    data = request.json

    # Check JSON Validity
    if 'text' not in data or 'lang' not in data:
        return makejson({'error': 'Invalid JSON data'}), 400
    
    # Cache Values
    input_text = data['text']
    lang = data['lang']

    # Check If Any Text Was Given# Check If Any Text Was Given
    if not input_text:
        return makejson({'error': 'Empty input text'}), 400
    
    # Check If Any Lang Was Given
    if not lang:
        return makejson({'error': 'Empty lang'}), 400
    
    # Translate The Text According To The Provided Lang
    translated_text = translate(input_text, lang)

    # Return The Result Back To The Client
    return makejson({'translated_text': translated_text}), 200

def translate(input_text: str, lang: str) -> str:
    # Cache Translation Output TextBox
    outputbox = page.wait_for_selector(f'[data-testid="translator-target-input"]', timeout=10000, state="visible")

    targetlang = page.wait_for_selector(f'[data-testid="translator-target-lang"]', timeout=10000, state="visible")

    # Select The Target Language
    if targetlang.get_attribute("dl-selected-lang") != lang and targetlang.get_attribute("dl-selected-lang") != "en-EN":
        print("Target Lang: " + lang)
        print("Currently: " + targetlang.get_attribute("dl-selected-lang"))

        page.wait_for_selector(f'[data-testid="translator-target-lang-btn"]', timeout=10000, state="visible").click()

        langbutton = page.wait_for_selector(f'[data-testid="translator-lang-option-{lang}"]', timeout=10000, state="visible")

        print(langbutton.inner_text())

        langbutton.click()

        print("Now: " + targetlang.get_attribute("dl-selected-lang"))

    # Fill In Our Text For Translating, Caching For Optimization, Filling Blank First For While Loop Later To Work
    sourcebox = page.get_by_role("textbox", name="Source text")
    sourcebox.click()
    sourcebox.fill("")

    while outputbox.inner_text() != '\n':
        time.sleep(1)

    sourcebox.fill(input_text)

    # Wait For Translation To Finish By Waiting For Length > 0 And It Not To Be The Empty Newline DeepL Initializes It With
    while outputbox.inner_text() == '\n':
        time.sleep(1)

    # Select The Target Language
    if targetlang.get_attribute("dl-selected-lang") != lang and targetlang.get_attribute("dl-selected-lang") != "en-EN":
        print("Target Lang: " + lang)
        print("Currently: " + targetlang.get_attribute("dl-selected-lang"))

        page.wait_for_selector(f'[data-testid="translator-target-lang-btn"]', timeout=10000, state="visible").click()

        langbutton = page.wait_for_selector(f'[data-testid="translator-lang-option-{lang}"]', timeout=10000, state="visible")

        print(langbutton.inner_text())

        langbutton.click()

        print("Now: " + targetlang.get_attribute("dl-selected-lang"))

        # Wait For Translation To Finish By Waiting For Length > 0 And It Not To Be The Empty Newline DeepL Initializes It With
        while outputbox.inner_text() == '\n':
            time.sleep(1)

    # Return Translation
    print(outputbox.inner_text())
    return outputbox.inner_text()

app.run(host='0.0.0.0')
