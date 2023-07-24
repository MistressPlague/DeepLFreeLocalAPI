# DeepL Free Local API
A workaround way to get a DeepL translation API locally while not needing a API key at all. Emulates chromium headlessly and makes a local web api.

# Expected Input JSON
[POST, http://127.0.0.1:5000/translate]
```json
{
  "lang": "French",
  "text": "hello!"
}
```

# Expected Output JSON
```json
{
    "translated_text": "Bonjour !"
}
```
# Note
First request of a different language will take up to 2 seconds, any after with the same language will be fast.
Changing language has significant delay.
