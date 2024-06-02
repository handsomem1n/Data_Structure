'''
중위 순회 inorder
왼루오 방식
응용 :
    sorting
'''

def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.data, end = '')
        inorder(n.right)
        