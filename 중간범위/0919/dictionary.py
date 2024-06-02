map = { 'appple' : '사과', 'peach' : '복숭아', 'banana' : '바나나'}
print(map)
for e in map :
    print ("%s => %s" %(e, map[e]))
map['grape'] = '포도'
map.update({'orange' : '오렌지', 'mandarin' : '귤'})
print(map)
print(map.keys())
print(map.values())
