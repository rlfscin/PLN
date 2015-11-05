from math import log
import re

stopwords = [line.rstrip('\n') for line in open('stopwords.txt')]

class Node:
    def __init__(self):
        self.words = {}
        self.count = 0
        self.vocabularySize = 0

    def learn(self, words):
        words = Node.clean_words(words)
        for word in words:
            self.count = self.count +1
            if(self.words.has_key(word)):
               self.words[word] = self.words[word] + 1
            else:
               self.words[word] = 1
               self.vocabularySize += 1

    def validate(self, words):
        prob = 0.0
        words = Node.clean_words(words)
        
        for word in words:
            if(self.words.has_key(word)):
                prob = prob - log((self.words[word] + 1.0)/(self.count + self.vocabularySize))
            else:
                prob = prob - log(1.0/(self.count + self.vocabularySize))
        return prob
    
    @classmethod
    def clean_words(cls, words):
        regex = re.compile(r"^[a-z]{3,}$", re.IGNORECASE)
        words = [word.lower() for word in words if regex.match(word)]
        words = [word for word in words if word not in stopwords]
        return words
