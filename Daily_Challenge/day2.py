# 20240828 day2.py

# day2 출력, 연산


# 두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.
# 4 5
a, b = map(int, input().strip().split(' '))
print(f"{a} + {b} = {a + b}")


# 두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다. 입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.
# apple pen / Hello World!
str1, str2 = input().strip().split(' ')
print(str1 + str2)


# 문자열 str이 주어집니다. 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.
# abcde
str = input()
for i in str:
    print(i)
## 다른 풀이
# print('\n'.join(input()))


# 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.
# 100
n = int(input())
if n % 2 == 0:
    print(f"{n} is even")
else :
    print(f"{n} is odd")
# print(f"{n} is {'odd' if n % 2 else 'even'}")


# 문자열 my_string, overwrite_string과 정수 s가 주어집니다. 
# 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
# my_string	        overwrite_string	s	result
# "He11oWor1d"	    "lloWorl"	        2	"HelloWorld"
# "Program29b8UYP"	"merS123"	        7	"ProgrammerS123"
# 수정 답:
def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer
my_string, overwrite_string, s = input().strip().split(' ')
s = int(s)
print(solution(my_string, overwrite_string, s))

# 처음 쓴 답:
# def solution(my_string, overwrite_string, s):
#     repStr = my_string[s:s+len(overwrite_string)]
#     answer = my_string.replace(repStr, overwrite_string)
#     return answer
# my_string, overwrite_string, s = input().strip().split(' ')
# s = int(s)
# print(solution(my_string, overwrite_string, s))