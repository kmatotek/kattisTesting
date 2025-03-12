def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    else:
        root.count += 1
    return root

def num_permutations(root):
    if root is None:
        return factorial(1)
    left_n = count_nodes(root.left)
    right_n = count_nodes(root.right)
    n = left_n + right_n + root.count - 1
    return factorial(n) // (factorial(left_n) * factorial(right_n)) * num_permutations(root.left) * num_permutations(root.right)

def count_nodes(root):
    if root is None:
        return 0
    return count_nodes(root.left) + count_nodes(root.right) + root.count

while True:
    n = int(input().strip())
    if n == 0:
        break
    nums = list(map(int, input().split()))
    root = None
    for num in nums:
        root = insert(root, num)
    print(num_permutations(root))