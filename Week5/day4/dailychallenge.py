from collections import Counter
from string import punctuation
import nltk


class Text():
    with open("dailychallenge.txt", "r") as f:
        text = f.read()

    def __init__(self, string):
        self.string = string

    def word_freq(self, word):
        freq = self.text.count(word)
        return f'{word} has {freq} appearances in the text'

    def most_common_word(self):
        occurence_count = Counter(self.text.split())
        return occurence_count.most_common()[0][0]

    def unique_words(self):
        unique_words = list(set(self.text.split()))
        return unique_words

    @classmethod
    def from_file(cls, text_file):
        with open(text_file, "r") as f:
            word_list = f.readlines()
            word_list = [word.replace("\n", "") for word in word_list]
            return cls(" ".join(word_list))


class TextModification(Text):
    def __init__(self, string):
        super().__init__(string)

    def de_punc(self):
        return "".join([word for word in self.text if punctuation.count(word) == 0])

    def de_stopwords(self):
        return " ".join([word for word in self.text.split(" ") if stopwords.words('english').count(word) == 0])
