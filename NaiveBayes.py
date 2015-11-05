from nltk.corpus import reuters
from Node import Node
from math import log
import sys
import re
import timeit

class NaiveBayes:

    def __init__(self):
        self.nodes = {}
        self.count = 0
        self.count_nodes = {}
        self.tag_names = []

    def training(self, words, tags):
        for tag in tags:
            if not self.nodes.has_key(tag): #to new tags
                self.tag_names.append(tag)
                self.nodes[tag] = Node()
                self.count_nodes[tag] = 0

            self.nodes[tag].learn(words) 
            self.count_nodes[tag] = self.count_nodes[tag] + 1
        self.count = self.count + 1

    def get_tags(self, words, threshold): #threshold = value [0-1] to determine how close each tag could be
        predicted_tags = []
        final_probability = {}
        threshold = 1 - threshold
        for tag in self.tag_names:
            tag_probability = - log(1.0*self.count_nodes[tag]/self.count) # P(c)
            document_probability = self.nodes[tag].validate(words) # P(w|c)
            final_probability[tag] = tag_probability + document_probability
        
        #normalizar as probabilidades
        minimum_tag_probability = min(final_probability.values())
        maximum_tag_probability = max(final_probability.values())
        
        
        for tag in self.tag_names:
            normalized_final_probability = (final_probability[tag] - minimum_tag_probability) / (maximum_tag_probability - minimum_tag_probability)
            if(normalized_final_probability <= threshold): # Tag accepted
                predicted_tags.append(tag)
        return predicted_tags

# If the file is executed, perform the main task.
if __name__ == '__main__':
    try:
        threshold = float(sys.argv[1])
    except IndexError:
        threshold = 0.93
    
    # Initialize some variables
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    
    training_time = 0
    testing_time = 0
    total_time = 0
    
    debug_message_interval = 500
    
    nb = NaiveBayes()
    
    # Specific tags to use
    tags = ['earn', 'acq','money-fx' ,'grain' ,'crude' ,'trade' ,'interest' ,'ship' ,'wheat', 'corn']
    
    # Get the documents from the base
    all = reuters.fileids(tags)
    training = [file_id for file_id in all if 'training' in file_id]
    test = [file_id for file_id in all if 'test' in file_id]
    
    # Training
    training_time = timeit.default_timer()
    print "[TRAINING] Started training with %d documents." % len(training)
    
    for i, file_id in enumerate(training):
        if i % debug_message_interval == 0:
           print " - Training document #%d" % i
        nb.training(reuters.words(file_id), [tag for tag in reuters.categories(file_id) if tag in tags])
    
    print "[TRAINING] Ended training."
    training_time = timeit.default_timer() - training_time
    
    # Testing
    testing_time = timeit.default_timer()
    print "\n[TESTING] Started testing with %d documents." % len(test)
    
    for i, file_id in enumerate(test):
        if i % debug_message_interval == 0:
           print " - Testing document #%d" % i
        
        predicted_tags = nb.get_tags(reuters.words(file_id), threshold)
        real_tags = reuters.categories(file_id)
        
        tp += len([tag for tag in predicted_tags if tag in real_tags])
        fp += len([tag for tag in predicted_tags if tag not in real_tags])
        tn += len([tag for tag in [tag for tag in tags if tag not in real_tags] if tag in [tag for tag in tags if tag not in predicted_tags]])
        fn += len([tag for tag in real_tags if tag not in predicted_tags])
        
    print "[TESTING] Ended testing."
    testing_time = timeit.default_timer() - testing_time
    
    total_time = training_time + testing_time
    
    # Calculate the metrics
    precision = float(tp) / (tp + fp)
    recall = float(tp) / (tp + fn)
    accuracy = float(tp + tn) / (tp + fp + tn + fn)
    f1 = 2 * ((precision * recall) / (precision + recall))
    
    # Output
    print "\n[RESULTS] The results are in!"
    print " - Precision: %f" % precision
    print " - Recall: %f" % recall
    print " - Accuracy: %f" % accuracy
    print " - F1: %f" % f1
    
    print "\n[INFO] For this execution:"
    print " - User defined threshold: %f" % threshold
    
    print " - Training time: %.2f s" % training_time
    print " - Testing time: %.2f s" % testing_time
    print " - Total time: %.2f s" % total_time
    
    print "\n[THANK YOU] The authors thank you for your time!"
    print " - Alexandre Cisneiros (acaf)"
    print " - Pedro Diniz (phrd)"
    print " - Rubens Lopes (rlfs)"