class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_into_bst(root, val):
    if root is None:
        return Node(val)
    else:
        if val < root.val:
            root.left = insert_into_bst(root.left, val)
        else:
            root.right = insert_into_bst(root.right, val)
    return root

def count_permutations(arr):
    if not arr:
        return 1
    root = None
    for num in arr:
        root = insert_into_bst(root, num)
    return factorial(len(set(arr))) // (factorial(count_nodes(root.left)) * factorial(count_nodes(root.right)))

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

while True:
    N = int(input())
    if N == 0:
        break
    values = list(map(int, input().split()))
    print(count_permutations(values))