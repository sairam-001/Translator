from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

def translate_text(text, target_language="hi"):
    translator = Translator()
    
    # Translate text (no need for asyncio)
    translation = translator.translate(text, src='en', dest=target_language)
    
    return translation.text  # Extract translated text

@app.route("/", methods=["GET", "POST"])
def translate():
    translated_text = ""
    input_text = ""

    if request.method == "POST":
        input_text = request.form.get("input_text")
        target_language = request.form.get("target_language", "hi")  # Default: Hindi
        if input_text:
            translated_text = translate_text(input_text, target_language)

    return render_template("index.html", input_text=input_text, translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
