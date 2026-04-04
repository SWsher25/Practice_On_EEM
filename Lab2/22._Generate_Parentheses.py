class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        states = [("", 0, 0)]

        while states:
            current, open_count, close_count = states.pop()

            if len(current) == 2 * n:
                combinations.append(current)
                continue

            if open_count < n:
                states.append((current + "(", open_count + 1, close_count))

            if close_count < open_count:
                states.append((current + ")", open_count, close_count + 1))

        return combinations