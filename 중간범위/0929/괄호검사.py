from ArrayStack import ArrayStack

def checkBracket(str) :
    s = ArrayStack()

    for c in str:
        if c == '[' or c == '{' or c == '(' :
            s.push(c)
        elif c == ']' or c == '}' or c == ')' :
            if s.isEmpty () :
                return False
        else :
            left = s.pop()
            if  (c == ']' and left != '[') or \
                (c == '}' and left != '{') or \
                (c == ')' and left != '()'):
                return False
    return s.isEmpty()

s1 = " {A [ (i+1) ] = 0; }"
s2 = "if( (i==0) && (j==0)"
s3 = "A[ ( i+1 ] ) = 0;"

print( s1, " ---> ", checkBracket(s1))
print( s2, " ---> ", checkBracket(s2))
print( s3, " ---> ", checkBracket(s3))