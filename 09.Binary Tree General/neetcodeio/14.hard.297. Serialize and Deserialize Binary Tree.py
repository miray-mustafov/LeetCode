from utils.tree.tree import TreeNode, make_tree_from_list


class Codec:
    SEPARATOR = ','

    @staticmethod
    def is_integer(s):
        if s.isdigit():
            return True
        if s.startswith('-') and s[1:].isdigit():
            return True
        return False

    def serialize(self, root):
        if not root:
            return ''

        from collections import deque
        str_list, queue = [], deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    str_list.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    str_list.append('N')

        last_seq_Ns_start_idx = len(str_list)
        for i in range(len(str_list) - 1, -1, -1):
            if Codec.is_integer(str_list[i]):
                last_seq_Ns_start_idx = i + 1
                break

        return Codec.SEPARATOR.join(str_list[:last_seq_Ns_start_idx])

    def deserialize(self, data):
        if not data:
            return None

        from collections import deque
        data = data.split(Codec.SEPARATOR)
        n = len(data)
        root = TreeNode(data[0])
        queue = deque([root])

        i = 0
        while queue:
            node = queue.popleft()
            lidx = i * 2 + 1
            ridx = i * 2 + 2
            if lidx < n and data[lidx] is not 'N':
                node.left = TreeNode(data[lidx])
                queue.append(node.left)
            if ridx < n and data[ridx] is not 'N':
                node.right = TreeNode(data[ridx])
                queue.append(node.right)
            i += 1
        return root


root = make_tree_from_list([1, -2, 3, None, None, 4, 5], stringified=str)
ser = Codec().serialize(root)
deser = Codec().deserialize(ser)

ans = Codec().serialize(deser) == ser
print(ans)
