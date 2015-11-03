import Node from Node

class NaiveBayes:

	def __init__(self):
		self.nodes = {}
		self.count = 0
		self.countNodes = {}

	def training(self, words, tags):
		for tag in tags:
			if(!self.nodes.has_key(tag)): #to new tags
				self.nodes[tag] = Node
				self.countNodes[tag] = 0

			self.nodes[tag].learn(words) 
			self.countNodes[tag] = self.countNodes[tag] + 1
		self.count = self.count + 1

				

	def getTags(self, words, threshold): #threshold = value [0-1] to determine how close each tag could be
		tags = []
		for node in nodes:
			probNode = 1.0*self.countNodes[node]/self.count # P(c)
			probWords = self.nodes[node].validate(words) # P(w|c)
			probTotal = probNode*probWords
			if(probTotal >= threshold): #Tag accepted
				tags.append(node)
		return tags


