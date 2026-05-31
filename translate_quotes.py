import json
import time
from deep_translator import GoogleTranslator

# Expanded to cover the vast majority of global Android users
target_languages = [
    'hi', 'ru', 'de', 'es', 'fr', 'it', 'pt', 'zh-CN', 'ja', 'ko',
    'ar', 'bn', 'ur', 'tr', 'vi', 'th', 'id', 'nl', 'pl', 'uk', 
    'ta', 'te', 'mr', 'gu', 'kn', 'ml', 'pa', 'fa', 'sw', 'ms'
]

def main():
    with open('quotes_source.json', 'r', encoding='utf-8') as f:
        source_data = json.load(f)

    master_data = {}

    for date, en_quotes in source_data.items():
        print(f"Translating quotes for {date}...")
        master_data[date] = {'en': en_quotes}
        
        for lang in target_languages:
            translator = GoogleTranslator(source='en', target=lang)
            translated_quotes = []
            
            for quote in en_quotes:
                try:
                    translated = translator.translate(quote)
                    translated_quotes.append(translated)
                except Exception as e:
                    print(f"Translation failed for '{quote}' to {lang}: {e}")
                    # If it fails, fallback to English so the app doesn't crash or show empty text
                    translated_quotes.append(quote)
            
            master_data[date][lang] = translated_quotes
            # A tiny pause to ensure Google's free translation API doesn't block us
            time.sleep(0.2)

    with open('quotes_master.json', 'w', encoding='utf-8') as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)
        
    print("Translation complete! Global quotes_master.json generated.")

if __name__ == "__main__":
    main()
