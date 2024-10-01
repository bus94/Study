# 20240925 day22.py

# day22 함수(메서드), 조건문 활용


'''
정수로 이루어진 문자열 n_str이 주어질 때, n_str의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록 solution 함수를 완성해주세요.

n_str	    result
"0010"	    "10"
"854020"	"854020"
'''
def solution(n_str):
    check_index = -1
    for i in range(len(n_str)):
        if n_str[i] == '0':
            check_index = i
            print("check_index:", check_index)
        else:
            return n_str[check_index + 1:]
# print(solution("0010"))
# print(solution("854020"))
## 다른 풀이
# def solution(n_str):
#     return n_str.lstrip('0')
# lstrip : 문자열에 왼쪽 공백이나 인자가된 문자열의 모든 조합을 제거
# rstrip : 문자열에 오른쪽 공백이나 인자가된 문자열의 모든 조합을 제거
# strip : 양쪽 문자열에 공백이나 인자가된 문자열의 모든 조합을 제거


'''
0 이상의 두 정수가 문자열 a, b로 주어질 때, a + b의 값을 문자열로 return 하는 solution 함수를 작성해 주세요.

a	                    b	                    result
"582"	                "734"	                "1316"
"18446744073709551615"	"287346502836570928366"	"305793246910280479981"
"0"	                    "0"	                    "0"
'''
def solution(a, b):
    return str(eval(a + '+' + b))
# print(solution("582", "734"))
# print(solution("18446744073709551615", "287346502836570928366"))
# print(solution("0", "0"))


'''
정수 n이 주어질 때, n을 문자열로 변환하여 return하도록 solution 함수를 완성해주세요.

n	    result
123	    "123"
2573	"2573"
'''
def solution(n):
    return str(n)
# print(solution(123))
# print(solution(2573))


'''
정수 배열 arr과 delete_list가 있습니다. 
arr의 원소 중 delete_list의 원소를 모두 삭제하고 남은 원소들은 기존의 arr에 있던 순서를 유지한 배열을 return 하는 solution 함수를 작성해 주세요.

arr	                        delete_list	                result
[293, 1000, 395, 678, 94]	[94, 777, 104, 1000, 1, 12]	[293, 395, 678]
[110, 66, 439, 785, 1]	    [377, 823, 119, 43]	        [110, 66, 439, 785, 1]
'''
def solution(arr, delete_list):
    for d in delete_list:
        if d in arr:
            arr.remove(d)
    return arr
# print(solution([293, 1000, 395, 678, 94], [94, 777, 104, 1000, 1, 12]))
# print(solution([110, 66, 439, 785, 1], [377, 823, 119, 43]))
## 다른 풀이
# def solution(arr, delete_list):
#     return [i for i in arr if i not in delete_list]
# 삭제하지 않고, delete_list의 원소가 아닌 arr의 원소만 출력될 수 있도록 작성하였다.


'''
부분 문자열이란 문자열에서 연속된 일부분에 해당하는 문자열을 의미합니다. 
예를 들어, 문자열 "ana", "ban", "anana", "banana", "n"는 모두 문자열 "banana"의 부분 문자열이지만, "aaa", "bnana", "wxyz"는 모두 "banana"의 부분 문자열이 아닙니다.
문자열 my_string과 target이 매개변수로 주어질 때, target이 문자열 my_string의 부분 문자열이라면 1을, 아니라면 0을 return 하는 solution 함수를 작성해 주세요.

my_string	target	result
"banana"	"ana"	1
"banana"	"wxyz"	0
'''
def solution(my_string, target):
    return int(target in my_string)
# print(solution("banana", "ana"))
# print(solution("banana", "wxyz"))