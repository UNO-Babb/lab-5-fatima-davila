#LetterFrequency.py
#Name: Fatima Davila
#Date:2/22/2024
#Assignment:letter frequency

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

from pyparsing import alphas

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #loop through each letter
    for letter in message:
        spot = alpha.find(letter)
        if spot >= 0:
            freq[spot]=freq[spot] + 1
output_core = ["letter, Count"]
for i in range(26):
        print (alphas[i] , ":", freq[i])
        output_core.append("{alpha[i]}, {"{freq[i]}")
        line = alphas[i] + "," + str(freq[i]) + "\n"
        output = output + line
    writeTofile("\n".join(output_core))

    #Find the position in the alphabet
    #Increase the frequency at that position. If position was 5, then frequencies[5] = frequencies[5] + 1

 



    #Create the output text in the format A,5\n if there were 5 letter A in the message.
    #Remember that the \n is the symbol for a new line.

    

    writeToFile(output)

def new_func(freq):
    spot = 5 
    freq[spot] = freq[spot] + 1


def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    freqFile = open("frq.csv", 'w')
    freqFile.write(fileText)

    freqFile.close()


def main():
    msg = input("Enter a message: ")
    countLetters(msg)



if __name__ == '__main__':
  main()
