'''def is_palindrome(s):
    return s == s[::-1]

def find_longest_palindrome_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    longest = ""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y, path):
        nonlocal longest
        if x == rows - 1 and y == cols - 1:
            full_path = path + matrix[x][y]
            if is_palindrome(full_path) and len(full_path) > len(longest):
                longest = full_path
            return

        visited[x][y] = True
        path += matrix[x][y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                dfs(nx, ny, path)
        visited[x][y] = False

    dfs(0, 0, "")
    return longest
matrix=[['a','x','a'],
        ['x','a','x'],
        ['a','x','a']]
res=find_longest_palindrome_path(matrix)
print(res)'''
def cons(arr):
    cnt=0
    for i in range(len(arr)):
        if arr[i]==0:
            break
        else:
            cnt+=1
    return cnt
arr=[1,0,1,1,0]
max_len=-999
for i in range(len(arr)):
    if arr[i]==0:
        arr[i]=1
        n=cons(arr)
        arr[i]=0
        max_len=max(n,max_len)
print(max_len)

