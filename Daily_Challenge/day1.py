# 20240827 day1.py

# day1 출력


'''
문자열 str이 주어질 때, str을 출력하는 코드를 작성해 보세요.

HelloWorld!
'''
str = input()
print(str)


'''
정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

4 5
'''
a, b = map(int, input().strip().split(' '))
print(f"a = {a}")
print(f"b = {b}")


'''
문자열 str과 정수 n이 주어집니다. str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

string 5
'''
str, n = input().strip().split(' ')
n = int(n)
print(str * n)


'''
영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

aBcDeFg
'''
str = input()
print(str.swapcase())


'''
다음과 같이 출력하도록 코드를 작성해 주세요.

출력: !@#$%^&*(\'"<>?:;
'''
print('!@#$%^&*(\\\'"<>?:;')
