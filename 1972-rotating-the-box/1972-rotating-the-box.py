class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        new_col,new_row=len(box),len(box[0])
        res=[[None for _ in range(new_col)]for _ in range(new_row)]
        for i in range(new_col):
            for j in range(new_row):
                res[j][i]=box[i][j]
        for i in range(new_row):
            res[i]=res[i][::-1]
        for j in range(new_col):
            for i in range(new_row-1,-1,-1):
                if res[i][j]=='.':
                    stone_to_fall=-1
                    k=i-1
                    while k>=0:
                        if res[k][j]=='*':
                            break
                        elif res[k][j]=='#':
                            stone_to_fall=k
                            res[k][j]='.'
                            break
                        k-=1
                    if stone_to_fall!=-1:
                        res[i][j]='#'
        return res