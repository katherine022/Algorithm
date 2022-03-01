import sys

def preorder(root) :
    print(root, end='')
    if root in lc.keys() : preorder(lc[root])
    if root in rc.keys() : preorder(rc[root])

def inorder(root) :
    if root in lc.keys() : inorder(lc[root])
    print(root,end='')
    if root in rc.keys() : inorder(rc[root])

def postorder(root) :
    if root in lc.keys() : postorder(lc[root])
    if root in rc.keys() : postorder(rc[root])
    print(root, end='')

input = sys.stdin.readline
lc = dict()
rc = dict()
N = int(input())

for _ in range(N) :
    root, ll, rr = input().split()
    if ll != "." : lc[root] = ll
    if rr != "." : rc[root] = rr

preorder('A')
print()
inorder('A')
print()
postorder('A')
