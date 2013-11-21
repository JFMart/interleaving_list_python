
## Author: Jose F. Martinez Rivera
## Student Number: 802-10-4088
## Course: ICOM4036 - 040
## Professor: Dr. Wilson Rivera
## Hand-In Date: March 12, 2013

# 1. Write a program that counts the frequencies of each word in a text,
# and output each word with its count and line numbers where it appears. 
# We define a word as a contiguous sequence of non-white-space characters. 
# Different capitalizations of the same character sequence should be 
# considered same word (e.g. Python and python). The output is formatted as 
# follows: each line begins with a number indicating the frequency of the word,
# a white space, then the word itself, and a list of line numbers containing this
# word. You should output from the most frequent word to the least frequent. In case 
# two words have the same frequency, the lexicographically smaller one comes first. 
# All words are in lower case in the output.

import re

#Stores tuples that contain the frequency of a word, the word itself and the line
#in which the number appears.
wordDictionary = []


def main():
     
     #Text File location
     fileInput = 'textfile.txt'

     file = read(fileInput)

     #We count line numbers from 1
     lineNumber = 1


     while True:
     	text = file.readline()


     	if text == "": #Marks if the file has ended
     		break

     	else:
     		wordsInText = match(text)
     		addToDictionary(wordsInText, lineNumber)
     		lineNumber += 1
    
    
     file.close()	
     sort()
     printOut()
     
#Opens the file at the given file location   
def read(input):
	file = open(input, 'r')
	return file


#Matches all the words (sequences of non-whitespace characters)
def match(text):
	wordMatches = re.findall('[\S]+', text)
	return wordMatches

#Adds all the words found in the text file to the dictionary
def addToDictionary(wordList, lineNumber):

	
	smallDictionary = []
	
	for i in range(0, len(wordList)):

		
		boolTuple = False
		for j in range(0, len(wordDictionary)):

			#If the word is already in the list, we make a new tuple, increase the frecuency and add the line number
			
			if wordDictionary[j][1].lower() == wordList[i].lower():
				
				replacementLines = wordDictionary[j][2]
				replacementLines.append(lineNumber)
				replacementTuple = wordDictionary[j][0] + 1, wordDictionary[j][1].lower(), replacementLines
				wordDictionary[j] = replacementTuple
				boolTuple = True
				break
			
	
		if boolTuple == False:
			newTuple =  1, wordList[i].lower(), [lineNumber]
			wordDictionary.append(newTuple)
			

	
		





#Prints out the words found, their frequency and line position.
def printOut():

	output = open('output.txt', 'w')

	for k in range(0, len(wordDictionary)):
		output.write("{: <5}{: <20}{: <25}".format(str(wordDictionary[k][0]), wordDictionary[k][1], str(wordDictionary[k][2])))
		output.write("\n") #Prints out a newline

	output.close()

#Bubblesort algorithm
def sort():

	for i in range(0, len(wordDictionary)-1):

		for j in range(0, len(wordDictionary)-1):

			if wordDictionary[j][0] < wordDictionary[j+1][0]:
				temp = wordDictionary[j]
				wordDictionary[j] = wordDictionary[j+1]
				wordDictionary[j+1] = temp
			
			elif wordDictionary[j][0] == wordDictionary[j+1][0]:
				if wordDictionary[j][1] > wordDictionary[j+1][1]:
					temp = wordDictionary[j]
					wordDictionary[j] = wordDictionary[j+1]
					wordDictionary[j+1] = temp



main()
