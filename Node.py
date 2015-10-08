class Node:
    def __init__(self):
        self.words = {}
        self.count = 0

    def learn(self, words):
        for word in words:
            self.count = self.count +1
            if(self.words.has_key(word)):
               self.words[word] = self.words[word] + 1
            else:
               self.words[word] = 1

    def validate(self, words):
        prob = 1.0
        for word in words:
            if(self.words.has_key(word)):
                prob = prob*(self.words[word])/(self.count)
            else:
                pass
        return prob
