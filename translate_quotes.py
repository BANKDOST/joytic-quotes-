import json
from deep_translator import GoogleTranslator

target_languages = ['hi', 'ru', 'de']

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
                    translated_quotes.append(quote)
            
            master_data[date][lang] = translated_quotes

    with open('quotes_master.json', 'w', encoding='utf-8') as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)
        
    print("Translation complete! quotes_master.json generated.")

if __name__ == "__main__":
    main()