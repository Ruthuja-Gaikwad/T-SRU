class Trie:
    def __init__(self):
        self.c={}
        self.f=-1
    def insert(self,a,j):
        root=self
        for i in a:
            if i not in root.c:
                root.c[i]=Trie()
            root=root.c[i]
        root.f=j
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        a=Trie()
        n=len(board)
        m=len(board[0])
        l=[]
        for i in range(len(words)):
            a.insert(words[i],i)
        d=[(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r,c,root):
            if r<0 or r>=n or c<0 or c>=m or board[r][c] not in root.c:
                return
            t=board[r][c]
            nextr=root.c[t]
            if nextr.f!=-1:
                l.append(words[nextr.f])
                nextr.f=-1
            board[r][c]="#"
            for dr,dc in d:
                dfs(r+dr,c+dc,nextr)
            board[r][c]=t
        for k in range(n):
            for x in range(m):
                dfs(k,x,a)
        return l



            

        
