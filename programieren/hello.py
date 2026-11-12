

import pip
import nltk

nltk.download() 
sentence = "Cut down a tree with a herring? It can't be done." 
print(nltk.word_tokenize(sentence))