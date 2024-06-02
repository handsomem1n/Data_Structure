def is_palindrome(input_str):
    # 알파벳과 숫자만 남기고 모든 문자를 소문자로 변환
    cleaned_str = ''.join(char for char in input_str if char.isalnum()).lower()

    stack = []

    # 문자열의 문자들을 스택에 삽입
    for char in cleaned_str:
        stack.append(char)

    # 스택에서 문자들을 꺼내면서 원래의 문자열과 비교
    for char in cleaned_str:
        if char != stack.pop():
            return False

    return True

# 테스트
test_strings = ["eye", "madam, Im Adam", "race car", "hello", "A man, a plan, a canal, Panama!"]

for s in test_strings:
    if is_palindrome(s):
        print(f" '{s}' is a palindrome. ")
    else:
        print(f" '{s}' is NOT a palindrome. ")
