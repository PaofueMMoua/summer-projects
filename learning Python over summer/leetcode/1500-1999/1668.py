class Solution:
    def maxRepeating( sequence: str, word: str) -> int:
        
# get the sequence
# get the word
# check for how many times the word comes into the sequence
# check how many times it repeats
        totalTimesRepeated = 0
        # set variable for return
        repeated = word
        while repeated in sequence:
            # make a while loop to repeat through the sequence to check how many times the word repeats
            totalTimesRepeated += 1
            # add one to the variable
            repeated += word
            # change the repeated word to let it be larger to see if it is in sequence but is repeated again.
        return totalTimesRepeated
    # return the result



sequence = "ababc"
word = "ab"
print()
print()
print()
print(Solution.maxRepeating(sequence, word))
print()
print()
print()