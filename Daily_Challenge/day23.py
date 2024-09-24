# 20240926 day23.py

# day23 조건문 활용


'''
어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 합니다. 예를 들어 문자열 "abc"는 문자열 "aabcc"의 부분 문자열입니다.
문자열 str1과 str2가 주어질 때, str1이 str2의 부분 문자열이라면 1을 부분 문자열이 아니라면 0을 return하도록 solution 함수를 완성해주세요.

str1	str2	    result
"abc"	"aabcc"	    1
"tbt"	"tbbttb"	0
'''
def solution(str1, str2):
    return 1 if str1 in str2 else 0
# print(solution("abc", "aabcc"))
# print(solution("tbt", "tbbttb"))
## 다른 풀이
# def solution(str1, str2):
#     return int(str1 in str2)
# 포함되는지 안되는지 boolean 타입의 결과로 정수 1, 0을 출력하였다.


'''
문자열들이 담긴 리스트가 주어졌을 때, 모든 문자열들을 순서대로 합친 문자열을 꼬리 문자열이라고 합니다. 
꼬리 문자열을 만들 때 특정 문자열을 포함한 문자열은 제외시키려고 합니다. 
예를 들어 문자열 리스트 ["abc", "def", "ghi"]가 있고 문자열 "ef"를 포함한 문자열은 제외하고 꼬리 문자열을 만들면 "abcghi"가 됩니다.
문자열 리스트 str_list와 제외하려는 문자열 ex가 주어질 때, str_list에서 ex를 포함한 문자열을 제외하고 만든 꼬리 문자열을 return하도록 solution 함수를 완성해주세요.

str_list	            ex	    result
["abc", "def", "ghi"]	"ef"	"abcghi"
["abc", "bbc", "cbc"]	"c"	    ""
'''
def solution(str_list, ex):
    result = ""
    for s in str_list:
        if not ex in s:
            result += s
    return result
# print(solution(["abc", "def", "ghi"], "ef"))
# print(solution(["abc", "bbc", "cbc"], "c"))


'''
정수 리스트 num_list와 찾으려는 정수 n이 주어질 때, num_list안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.

num_list	        n	result
[1, 2, 3, 4, 5]	    3	1
[15, 98, 23, 2, 15]	20	0
'''
def solution(num_list, n):
    return int(n in num_list)
# print(solution([1, 2, 3, 4, 5], 3))
# print(solution([15, 98, 23, 2, 15], 20))


'''
1부터 6까지 숫자가 적힌 주사위가 두 개 있습니다. 두 주사위를 굴렸을 때 나온 숫자를 각각 a, b라고 했을 때 얻는 점수는 다음과 같습니다.
a와 b가 모두 홀수라면 a**2 + b**2 점을 얻습니다.
a와 b 중 하나만 홀수라면 2 × (a + b) 점을 얻습니다.
a와 b 모두 홀수가 아니라면 |a - b| 점을 얻습니다.
두 정수 a와 b가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

a	b	result
3	5	34
6	1	14
2	4	2
'''
def solution(a, b):
    result = 0
    if a % 2 and b % 2:
        result = a ** 2 + b ** 2
    elif not a % 2 and not b % 2:
        
print(solution(3, 5))
print(solution(6, 1))
print(solution(2, 4))


'''
정수 배열 date1과 date2가 주어집니다. 
두 배열은 각각 날짜를 나타내며 [year, month, day] 꼴로 주어집니다. 각 배열에서 year는 연도를, month는 월을, day는 날짜를 나타냅니다.
만약 date1이 date2보다 앞서는 날짜라면 1을, 아니면 0을 return 하는 solution 함수를 완성해 주세요.

date1	        date2	        result
[2021, 12, 28]	[2021, 12, 29]	1
[1024, 10, 24]	[1024, 10, 24]	0
'''
def solution(date1, date2):
    answer = 0
    return answer