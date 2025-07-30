import random
import configparser
import csv

class Password:
    def __init__(self, config, sectionTitle):
        self.config = config
        self.sectionTitle = sectionTitle

# this function is to change the words into new words that include numbers and character swaps.

    def _changing_Words_New_Words(self, nums):

# getting the words from the CSV File using a random number from the CSV File

        words = self._getting_Word_From_CSV(nums)

# swapping the letters for numbers and symbols
        print(" ".join(words))
        for i in range(len(words)):
            words[i] = words[i].capitalize()
            words[i] = words[i].replace("i", "!")
            words[i] = words[i].replace("l", "1")
            words[i] = words[i].replace("s", "$")
            words[i] = words[i].replace("a", "@")
            words[i] = words[i].replace("e", "3")
            words[i] = words[i].replace("o", "0")
        return "".join(words)

# this function is going to read the CSV file and get the number within the file

    def _getting_Word_From_CSV(self, num):
        words = []

        with open("password.csv", mode="r") as file:
            csvFile = csv.reader(file)

            for line in csvFile:
                total_words_in_line = len(line)

                for _ in range(num):
                    word_number = random.randint(0, total_words_in_line)
                    word = line[word_number]
                    words.append(word)

            return words

# main function getting called and calls all other functions

    def run(self):
        numOfWords = int(self.config[self.sectionTitle]['numOfWords'])
        return(self._changing_Words_New_Words(numOfWords))

# getting the numbers from the config to put into the function.

configName = 'passwordConfig2.ini'
sectionTitle = 'Numbers'
config = configparser.ConfigParser()
config.read(configName)

passGen = Password(config, sectionTitle)
print(passGen.run())