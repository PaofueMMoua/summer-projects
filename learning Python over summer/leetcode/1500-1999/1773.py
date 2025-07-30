class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
# if rule key is equal to type then its index 0
# if rule key is equal to color then it is index 1
# if rule key is equal to name then it is index 2
# get a count that would get the index of type and check if it is the rule value and ext.
        count=0
        for item in items:
            if ruleKey=="type" and item[0]==ruleValue:
                count+=1
            elif ruleKey=="color" and item[1]==ruleValue:
                count+=1
            elif ruleKey=="name" and item[2]==ruleValue:
                count+=1
        return count

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
print()
print()
print()
print(Solution.countMatches(items, ruleKey, ruleValue))
print()
print()
print()