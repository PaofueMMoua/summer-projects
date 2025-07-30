class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # take the array of lists
        # make a for loop that cycles through each instance
        # get the second instance of and then find the matching first index and so on untill you reach the end where you dont find another result
        source_cities = set()
        for path in paths:
            source_cities.add(path[0])
        for path in paths:
            if path[1] not in source_cities:
                return path[1]