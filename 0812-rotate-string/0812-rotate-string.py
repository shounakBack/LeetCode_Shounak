class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n1,n2=len(s),len(goal)
        if n1!=n2:
            return False
        for i in range(n1):
            if s[i]==goal[0]:
                temp=s[i:]+s[:i]
                if temp==goal:
                    return True
        return False