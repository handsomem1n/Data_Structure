l1 = [3, 5, 7, 9]
l2 = ['a', 'b', 'c', 'd']

print(l1[1]) # 5 출력

l2[2] = 'f' # 3번째에 f값으로 덮어버림
print(l2) 

l1.append(11) # 맨 뒤에 '11' 추가

l2.extend(l1) #l2 뒤에 l1을 추가한다.
print(l2)

print(l2.count('a')) #l2 리스트에서 'a'의 갯수를 반환
