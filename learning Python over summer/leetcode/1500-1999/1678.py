class Solution:
    def interpret(self, command: str) -> str:
        # replace all of the () with a o and then remove all perenthesis.
        command = command.replace('()', 'o')
        command = command.replace('(' ')', '')
        return command