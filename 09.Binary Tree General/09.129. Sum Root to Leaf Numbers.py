def sumNumbers(root):
    def dfs(cur, num):
        if not cur:
            return 0
        num = num * 10 + num
        if not cur.left and not cur.right:
            return num
        return dfs(cur.left, num) + dfs(cur.right, num)

    return dfs(root, root.val)
