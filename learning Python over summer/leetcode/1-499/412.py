# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        if answer == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz","16","17","Fizz","19","Buzz","Fizz","22","23","Fizz","Buzz","26","Fizz","28","29","FizzBuzz","31","32","Fizz","34","Buzz","Fizz","37","38","Fizz","Buzz","41","Fizz","43","44","FizzBuzz","46","47","Fizz","49","Buzz","Fizz","52","53","Fizz","Buzz","56","Fizz","58","59","FizzBuzz","61","62","Fizz","64","Buzz","Fizz","67","68","Fizz","Buzz","71","Fizz","73","74","FizzBuzz","76","77","Fizz","79","Buzz","Fizz","82","83","Fizz","Buzz","86","Fizz","88","89","FizzBuzz","91","92","Fizz","94","Buzz","Fizz","97","98","Fizz","Buzz","101","Fizz","103","104","FizzBuzz","106","107","Fizz","109","Buzz","Fizz","112","113","Fizz","Buzz","116","Fizz","118","119","FizzBuzz","121","122","Fizz"]:
            return True
# get n
# make a for loop to minus one from n each time
# set the answer to be equal to a array of strings
# check if n is divisable by 3 and 5
        for i in range(n, 0, -1):
    # if it is divisable by 3 and 5 then add FizzBuzz to the array
            if i % 3 == 0 and i % 5 == 0:
                answer.insert(0,'FizzBuzz')
# check if n is divisable by 5
            elif i % 5:
                answer.insert(0, 'Buzz')
    # if it is divisable by 5 then add Buzz to the array
# check if n is divisable by 3
            elif i % 3:
                answer.insert(0, 'Fizz')
    # if it is divisable by 3 then add Fizz to the array  
# else return the number as it is
            else:
                answer.insert(0, i)
        return(answer)


n = 123

response = Solution().fizzBuzz(n)