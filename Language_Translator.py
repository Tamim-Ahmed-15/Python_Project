#importing module
from deep_translator import GoogleTranslator


def translate_text():
    print("Type 'end' at any point to exit.")

    while True:
        source_lang = input("Enter source language code (e.g., 'en' for English, 'fr' for French): ").strip().lower()
        if source_lang == "end":
            print("Translation session ended.")
            return

        target_lang = input("Enter target language code (e.g., 'es' for Spanish, 'de' for German): ").strip().lower()
        if target_lang == "end":
            print("Translation session ended.")
            return

        while True:
            text = input("Enter text to translate (or type 'end' to exit): ")
            if text.lower() == "end":
                print("Translation session ended.")
                return

            translation = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
            print(f"\nTranslated Text ({source_lang} -> {target_lang}): {translation}")


if __name__ == "__main__":
    translate_text()
