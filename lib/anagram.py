# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        anagrams = []
        for mt in words:
            if sorted(mt.lower()) == sorted(self.word)and mt.lower() != self.word:
                anagrams.append(mt)
        return anagrams

listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])



print("matches")