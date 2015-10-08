class Node:
    def __init__(self):
        self.words = {}
        self.count = 0

    def learn(self, k):
        for word in k:
            self.count = self.count +1
            if(self.words.has_key(word)):
               self.words[word] = self.words[word] + 1
            else:
               self.words[word] = 1

    def validate(self, k):
        prob = 1.0
        for word in k:
            if(self.words.has_key(word)):
                prob = prob*(self.words[word]+1)/(self.count + )
            else:
                pass
        return prob
