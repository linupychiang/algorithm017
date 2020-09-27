class Solution:
    def modifyString(self, s: str) -> str:
        s = list("?" + s + "?")
        for i in range(1, len(s) - 1):
            if s[i] == "?":
                s[i] = {"a", "b", "c"}.difference({s[i - 1], s[i + 1]}).pop()
        return "".join(s[1:-1])
