class TreeNode:
    def _init_(self, name):
        self.name = name
        self.children = []
        self.parent = None
        self.locked_by = None  # None means not locked
        self.locked_descendants = 0  # To quickly check if any descendant is locked

def build_tree(node_names, m):
    nodes = {name: TreeNode(name) for name in node_names}
    root = nodes[node_names[0]]
    queue = [root]
    idx = 1
    while idx < len(node_names):
        current = queue.pop(0)
        for _ in range(m):
            if idx < len(node_names):
                child = nodes[node_names[idx]]
                child.parent = current
                current.children.append(child)
                queue.append(child)
                idx += 1
    return nodes

def can_lock_or_unlock(node):
    # Check all ancestors
    curr = node.parent
    while curr:
        if curr.locked_by is not None:
            return False
        curr = curr.parent
    # Check all descendants using locked_descendants
    return node.locked_descendants == 0

def lock(node, uid):
    if node.locked_by is not None or not can_lock_or_unlock(node):
        return False
    node.locked_by = uid
    # Update all ancestors' locked_descendants count
    curr = node.parent
    while curr:
        curr.locked_descendants += 1
        curr = curr.parent
    return True

def unlock(node, uid):
    if node.locked_by != uid:
        return False
    node.locked_by = None
    curr = node.parent
    while curr:
        curr.locked_descendants -= 1
        curr = curr.parent
    return True

def upgrade_lock(node, uid):
    # All descendants must be locked and by the same uid, and node itself must be unlocked
    locked_nodes = []
    def find_locked(node):
        if node.locked_by is not None:
            locked_nodes.append(node)
        for child in node.children:
            find_locked(child)
    find_locked(node)
    if not locked_nodes or node.locked_by is not None:
        return False
    for ln in locked_nodes:
        if ln.locked_by != uid:
            return False
    # Unlock all locked descendants
    for ln in locked_nodes:
        unlock(ln, uid)
    # Now, lock this node
    return lock(node, uid)

# Main input and processing logic
import sys

N = int(input())
m = int(input())
Q = int(input())
node_names = [input().strip() for _ in range(N)]
queries = [input().strip().split() for _ in range(Q)]
nodes = build_tree(node_names, m)

for q in queries:
    opt, name, uid = int(q[0]), q[1], int(q[2])
    node = nodes[name]
    if opt == 1:
        print(1 if lock(node, uid) else 0)
    elif opt == 2:
        print(1 if unlock(node, uid) else 0)
    elif opt == 3:
        print(1 if upgrade_lock(node, uid) else 0)
