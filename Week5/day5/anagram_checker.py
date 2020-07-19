class AnagramChecker():
    def __init__(self):
        with open('file.txt', 'r') as f:
            self.words = f.read()
            self.lista = self.words.split()

    def is_valid_word(self, word):
        for i in self.lista:
            if word in self.lista:
                return True
            else:
                return False

    def get_anagrams(self, word):
        for i in self.lista:
            if self.is_anagram(i, word):
                print(i)

    def is_anagram(self, word1, word2):
      # the sorted strings are checked
        if(sorted(word1) == sorted(word2)):
            return True
        else:
            return False
