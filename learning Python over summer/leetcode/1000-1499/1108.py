class Solution:
    def defangIPaddr(address: str) -> str:
        # get the address
        # replace each . with a [.]
        # address = address.replace('.', '[.]')
        return(address.replace('.','[.]'))


address = '255.100.50.0'

response = Solution.defangIPaddr( address)
print()
print()
print()
print(response)