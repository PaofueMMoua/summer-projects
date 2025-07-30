# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
List = [1,2,3]
joined_numbers = "".join(str(item) for item in List)
# print(joined_numbers)
joined_numbers = int(joined_numbers)
# print(joined_numbers)
joined_numbers += 1
# print(joined_numbers)
# joined_numbers = list(str(joined_numbers))
# print(joined_numbers)
joined_numbers = list(map(int,' '.join(str(joined_numbers)).split()))
# print(joined_numbers)



        # make the list one whole number
        # add one
        # split hte list into segments of 1 and into a list again
        # return that split list 