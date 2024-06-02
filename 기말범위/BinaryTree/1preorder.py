'''
preorder 전위 순회
루왼오 방식
응용 :
    레벨 계산
    구조화
'''

def preorder(n) :
    if n is not None : # 빈 게 아니라면
        print(n.data, end = '')
        preorder(n.left)
        preorder(n.right)