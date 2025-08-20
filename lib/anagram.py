# your code goes here!
#!/usr/bin/env python3

class Anagram:
    def __init__(self, word):
        self.word = word.lower() 
    def match(self, words):
        matches = []
        for candidate in words:
            if candidate.lower() != self.word:  
                if sorted(candidate.lower()) == sorted(self.word):
                    matches.append(candidate)
        return matches
