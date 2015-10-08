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

				

	def getTags(self, words, threshold):
		tags = []
		for node in nodes:
			probNode = 1.0*self.countNodes[node]/self.count
			probWords = self.nodes[node].validate(words)
			probTotal = probNode*probWords
			if(probTotal >= threshold):
				tags.append(node)
		return tags


