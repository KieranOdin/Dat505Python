import random
import time 
import sys
import wikipedia
 #Readfile Function, Reads in, line by line. The string is then split and converted into an array.
	
def readfile():
	line = f.readline() #reads in line from file (string).
	line = line.split(',', line.count(',')) #Split string into an array of strings.
	line[len(line) -1] = line[len(line) -1][:-1] #Removing \n from the line.
	
	#print line
	return line

#Response function, recieves 3 variables (userinput, type of word, corresponding response), if the word is in the word array then choose one of the random responses.

def response(userinput, words, resp):
	for x in range(0,len(words)):
		if words[x] in userinput:
			rand_response = random.choice(resp)
			print rand_response
			return True
	return False


#Writes all words to file.
def writetofile(words):
	userinput = raw_input('ME<#>:  ').lower()
	f = open('DATA.txt', 'w')
	words.append(userinput)
	f.write(','.join(greet) + '\n')
	f.write(','.join(quest) + '\n')
	f.write(','.join(bwords) + '\n')
	f.write(','.join(gwords) + '\n')
	f.write(','.join(bresp) + '\n')
	f.write(','.join(gresp) + '\n')
	f.write(','.join(gyes) + '\n')
	f.write(','.join(bno) + '\n')
	f.write(','.join(thanks) + '\n')
	f.write(','.join(bthanks) + '\n')
	f.close()

def AgeResponse(age): #If you get outer indentation level error, please rewrite corresponding line of code.
	Days = age * 365
	Hours = int(Days) * 24
	Minutes = int(Hours) * 60
    
	
	print('If you are ' + str(age) + ' then you are...')
	print('You are ' + str(Days) + ' old. or,')
	print(str(Hours) + ' hours old. or,')
	print('and ' + str(Minutes) + ' minutes old.')
	

conversation = True #Allows program to stay open

#Assigns each of the lines of the textfile to an individual array item
while conversation:
	f = open('DATA.txt', 'r')
	greet = readfile()
	quest = readfile()
	bwords = readfile()
	gwords = readfile()
	bresp = readfile()
	gresp = readfile()
	gyes = readfile()
	bno = readfile()
	thanks = readfile()
	bthanks = readfile()
	f.close()

	print('Hello')
	userinput = raw_input('ME<#>:  ').lower()
	
	#
	if userinput not in greet: 
		writetofile(greet)
	else:
		rand_greetings = random.choice(greet)
		print rand_greetings
		rand_questions = random.choice(quest)
		print rand_questions
		userinput = raw_input('ME<#>:  ').lower()
		if not response(userinput, bwords, bresp):
			if not response(userinput, gwords, gresp):
				print 'I dont recognise this response, are you feeling good or bad?'
				userinput = raw_input('ME<#>:  ').lower()
				if userinput == 'good':
					print('What word made your sentence positive?')			
					writetofile(gwords)
				elif userinput == 'bad':
					print('What word made your sentence negative?')
					writetofile(bwords)
				else:
					print('Something went wrong')
					
		
		print('How old are you?')
		userinput = raw_input('ME<#>:  ').lower()
		AgeResponse(int(userinput))
		
        print('Would you like to search wikipedia? yes/no')
        userinput = raw_input('ME<#>:  ').lower()
        if userinput == 'yes':
            print('What would you like to search?')
            userinput = raw_input('ME<#>:  ').lower()
            print(wikipedia.summary(userinput))
        
        
		
        print('Did you enjoy our conversation? Yes/No?')
        userinput = raw_input('ME<#>:  ').lower()
        cdif not response(userinput, gyes, thanks):	
			rand_thanks = random.choice(bthanks)
			print rand_thanks
			
	conversation = False