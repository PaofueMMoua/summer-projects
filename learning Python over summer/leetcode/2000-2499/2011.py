class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ops = {"--X": -1, "X--": -1, "++X": 1, "X++": 1}
        return sum(ops[op] for op in operations)