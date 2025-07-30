t = 'aa'
s = 'a'

for character in s:
    print(t.find(character))
    t =  t.replace(character, '', 1)
print(t)
# return(t)
    
