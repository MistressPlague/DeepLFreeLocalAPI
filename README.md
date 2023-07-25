# DeepL Free Local API
A workaround way to get a DeepL translation API locally while not needing a API key at all. Emulates chromium headlessly and makes a local web api.

Due to this, you can rest assured this will likely never break, and basically can't be detected, as it is quite literally running a headless web browser for it.

# Expected Input JSON
[POST, application/json, http://127.0.0.1:5000/translate]
```json
{
  "lang": "fr",
  "text": "hello!"
}
```

# Expected Output JSON
```json
{
    "translated_text": "Bonjour !",
    "error": ""
}
```

# Example Library
See [DeepL.cs](https://github.com/MistressPlague/DeepLFreeLocalAPI/blob/master/DeepL.cs) for an example of a library, which also gives an example of all of the supported target language strings.

# Note
First request of a different language will take up to 2 seconds, any after with the same language will be fast.
Changing language has significant delay.
