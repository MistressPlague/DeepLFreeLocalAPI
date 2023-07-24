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
