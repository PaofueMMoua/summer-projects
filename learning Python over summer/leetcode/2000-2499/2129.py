class Solution:
    def capitalizeTitle( title: str) -> str:
        # set all to lower
        # use the title function?
        # return?
        title = title.lower()
        title = title.title()
        return title
    
        alternative 

        return title.lower().title()
    
        correct alt 
        
        words = title.split(" ")
        for i, w in enumerate(words):
            if len(w) <= 2:
                words[i] = w.lower()
            else:
                words[i] = w[0].upper() + w[1:].lower()
        return " ".join(words)

title = "capiTalIze tHe titLe"
response = Solution.capitalizeTitle(title)
print()
print()
print()
print(response)