# 모스코드
'''
1. 테이블
2. 인코딩
    index를 계산해서 -> 변환 -> 리스트로 저장
3. 디코딩
3-1. sequential navigation
    리스트에서 하나씩 꺼내서 변환한다.
3-2. decision tree
    tree
'''

# 1. table (일차원 배열임)
table =[ ('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
        ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
        ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
        ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
        ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
        ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
        ('Y', '-.--'),  ('Z', '--..') ]

# 2. encoding
def encode(str) :
    encoded_list = []
    for i in str :
        index = ord(i) - ord('A')
        encoding_result = table[index][1]
        encoded_list.append(encoding_result)
    return encoded_list 

def sequential_decode(encoded_list):
    decoding_list = []  # 디코딩된 결과를 저장할 리스트
    for morses in encoded_list :
        found = False
        for j in range(len(table)):
            if morses == table[j][1]:
                decoding_result = table[j][0]
                decoding_list.append(decoding_result)
                found = True
                break  # 일치하는 값이 있으면 루프를 중단
        if not found:
            decoding_list.append(None)  # 해당 코드에 일치하는 값이 없으면 None을 추가
    return decoding_list

# 3-2. decoding(decision tree)
class TNode :
    def __init__ (self, e, left, right) :
        self.data = e
        self.left = left
        self.right = right

def make_morse_tree() :
    root = TNode( None, None, None)
    for tuple in table :
        tuplemorses = tuple[1]
        node = root
        for charmorse in tuplemorses :
            if charmorse =='.' :
                if node.left == None :
                    node.left = TNode(None,None, None)
                node = node.left
            elif charmorse == '-' :
                if node.right == None:
                    node.right = TNode(None,None,None)
                node = node.right
        node.data = tuple[0]
    return root

def decision_tree_decode(encoded_list, morseCodeTree) : # @@@@모르겠음@@@@ 첫번째 parameter : encoded_list, 두번째 Parameter : morseCodeTree
    decoding_list = []
    for morses in encoded_list :
        node = morseCodeTree # @@@@모르겠음@@@@
        for one_bit_morse in morses :
            if one_bit_morse == '.' :
                node = node.left
            elif one_bit_morse == '-' :
                node = node.right
        if node is not None :
            decoding_list.append(node.data) # @@@@@@@모르겠음@@@@ 왜 node.data?
    return decoding_list
    

if __name__ == "__main__" : 
    str = input('대문자로된 알파벳 글자 입력 : ')
    # 2
    str_encoded = encode(str) # encode()의 리턴값인 encoded_list가 반환된다.
    print("encoding 결과 : ",str_encoded)
    
    # 3-1
    sequential_decoded = sequential_decode(str_encoded) # encoding한 결과를 sequential decoding하여, decoding_list라는 변수로 리턴한다.
    print("sequential_decoding : ", sequential_decoded)

    # 3-2
    morseCodeTree = make_morse_tree()
    dt_decoded = decision_tree_decode(str_encoded, morseCodeTree)
    print("decision_tree로의 decoding : ", dt_decoded)





