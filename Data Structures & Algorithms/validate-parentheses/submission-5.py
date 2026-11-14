class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        for bracket in s:
            if bracket == "{" or bracket == "[" or bracket == "(":
                opened.append(bracket)
            elif len(opened) > 0:
                other = opened.pop()
                if (bracket == "}" and other == "{") or (bracket == "]" and other == "[") or (bracket == ")" and other == "("):
                    continue
                else:
                    return False
            else:
                return False
        return len(opened) == 0
                

