# 20240912 day15.py

# day15 리스트(배열), 문자열


'''
정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱합니다. 
그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.

arr	                    result
[1, 2, 3, 100, 99, 98]	[2, 2, 6, 50, 99, 49]
'''
def solution(arr):
    result = []
    for a in arr:
        if a >= 50 and a % 2 == 0:
            a //= 2
        elif a < 50 and a % 2 != 0:
            a *= 2
        result.append(a)
    return result
# print(solution([1, 2, 3, 100, 99, 98]))


'''
정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.
이러한 작업을 x번 반복한 결과인 배열을 arr(x)라고 표현했을 때, arr(x) = arr(x + 1)인 x가 항상 존재합니다. 
이러한 x 중 가장 작은 값을 return 하는 solution 함수를 완성해 주세요.
단, 두 배열에 대한 "="는 두 배열의 크기가 서로 같으며, 같은 인덱스의 원소가 각각 서로 같음을 의미합니다.

arr	                    result
[1, 2, 3, 100, 99, 98]	5
'''
def solution(arr):
    arrx = arr
    x = 0
    while True:
        result = []
        for a in arrx:
            if a >= 50 and a % 2 == 0:
                a //= 2
            elif a < 50 and a % 2 != 0:
                a = a * 2 + 1
            result.append(a)
        if arrx == result:
            return x
        arrx = result
        x += 1
# print(solution([1, 2, 3, 100, 99, 98]))


'''
정수가 있을 때, 짝수라면 반으로 나누고, 홀수라면 1을 뺀 뒤 반으로 나누면, 마지막엔 1이 됩니다. 예를 들어 10이 있다면 다음과 같은 과정으로 1이 됩니다.
10 / 2 = 5
(5 - 1) / 2 = 2
2 / 2 = 1
위와 같이 3번의 나누기 연산으로 1이 되었습니다
정수들이 담긴 리스트 num_list가 주어질 때, num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 return하도록 solution 함수를 완성해주세요.

num_list	        result
[12, 4, 15, 1, 14]	11
'''
def solution(num_list):
    count = 0
    for n in num_list:
        while not n == 1:
            if not n % 2:
                n //= 2
            else:
                n = (n-1) / 2
            count += 1
    return count
# print(solution([12, 4, 15, 1, 14]))


'''
정수가 담긴 리스트 num_list가 주어질 때, 
리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.

num_list	                                result
[3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]	    51
[2, 3, 4, 5]	                            120
'''
def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        result= 1
        for n in num_list:
            result *= n
        return result
# print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
# print(solution([2, 3, 4, 5]))
## 다른 풀이
# def solution(num_list):
#     if len(num_list) >= 11:
#         return eval('+'.join(list(map(str, num_list))))
#     else:
#         return eval('*'.join(list(map(str, num_list))))
# 정수 리스트를 하나의 문자열로 표현할 때 모든 문자들의 합 또는 곱의 형태로 정리한 후 eval 함수를 써서 리스트의 길이에 따라 각각의 결과값으로 리턴한다.


'''
알파벳으로 이루어진 문자열 myString과 pat이 주어집니다. 
myString의 연속된 부분 문자열 중 pat이 존재하면 1을 그렇지 않으면 0을 return 하는 solution 함수를 완성해 주세요.
단, 알파벳 대문자와 소문자는 구분하지 않습니다.

myString	pat	        return
"AbCdEfG"	"aBc"	    1
"aaAA"	    "aaaaa"	    0
'''
def solution(myString, pat):
    return 1 if pat.upper() in myString.upper() else 0
# print(solution("AbCdEfG", "aBc"))
# print(solution("aaAA", "aaaaa"))
## 다른 풀이
# def solution(myString, pat):
#     return int(pat.lower() in myString.lower())
# boolean을 이용하여 True이면 1, False이면 0을 리턴시킨다.