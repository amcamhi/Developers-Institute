from translate import Translator

translator = Translator(to_lang="he")
text = "Hello, my name is Andres"

translation = translator.translate(text)

print(translation)
