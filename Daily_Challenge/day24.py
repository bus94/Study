# 20240930 day24.py

# day24 조건문 활용


'''
팀의 막내인 철수는 아메리카노와 카페 라테만 판매하는 카페에서 팀원들의 커피를 사려고 합니다. 
아메리카노와 카페 라테의 가격은 차가운 것과 뜨거운 것 상관없이 각각 4500, 5000원입니다. 
각 팀원에게 마실 메뉴를 적어달라고 하였고, 그 중에서 메뉴만 적은 팀원의 것은 차가운 것으로 통일하고 "아무거나"를 적은 팀원의 것은 차가운 아메리카노로 통일하기로 하였습니다.
각 직원이 적은 메뉴가 문자열 배열 order로 주어질 때, 카페에서 결제하게 될 금액을 return 하는 solution 함수를 작성해주세요. 
order의 원소는 아래의 것들만 들어오고, 각각의 의미는 다음과 같습니다.

order	                                                    result
["cafelatte", "americanoice", "hotcafelatte", "anything"]	19000
["americanoice", "americano", "iceamericano"]	            13500
'''
def solution(order):
    result = 0
    for o in order:
        if o == 'anything' or 'americano' in o:
            result += 4500
        elif 'cafelatte' in o:
            result += 5000
    return result
# print(solution(["cafelatte", "americanoice", "hotcafelatte", "anything"]))
# print(solution(["americanoice", "americano", "iceamericano"]))


'''
직사각형 형태의 그림 파일이 있고, 이 그림 파일은 1 × 1 크기의 정사각형 크기의 픽셀로 이루어져 있습니다. 
이 그림 파일을 나타낸 문자열 배열 picture과 정수 k가 매개변수로 주어질 때, 
이 그림 파일을 가로 세로로 k배 늘린 그림 파일을 나타내도록 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

picture	                                                                                    k	result
[".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."]	2	["..xxxx......xxxx..", "..xxxx......xxxx..", "xx....xx..xx....xx", "xx....xx..xx....xx", "xx......xx......xx", "xx......xx......xx", "..xx..........xx..", "..xx..........xx..", "....xx......xx....", "....xx......xx....", "......xx..xx......", "......xx..xx......", "........xx........", "........xx........"]
["x.x", ".x.", "x.x"]	                                                                    3	["xxx...xxx", "xxx...xxx", "xxx...xxx", "...xxx...", "...xxx...", "...xxx...", "xxx...xxx", "xxx...xxx", "xxx...xxx"]
'''
def solution(picture, k):
    result = []
    for p in picture:
        new_p = ""
        for i in range(len(p)):
            new_p += p[i] * k
        for j in range(k):
            result.append(new_p)
    return result
# print(solution([".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."], 2))
# print(solution(["x.x", ".x.", "x.x"], 3))
## 다른 풀이
# def solution(picture, k):
#     answer = []
#     for i in range(len(picture)):
#         for _ in range(k):
#             answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
#     return answer
# replace를 이용하여 각각의 문자열을 k번 반복하여 리스트에 넣어 반환한다.


'''
정수 배열 arr와 자연수 k가 주어집니다.
만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고, k가 짝수라면 arr의 모든 원소에 k를 더합니다.
이러한 변환을 마친 후의 arr를 return 하는 solution 함수를 완성해 주세요.

arr	                    k	result
[1, 2, 3, 100, 99, 98]	3	[3, 6, 9, 300, 297, 294]
[1, 2, 3, 100, 99, 98]	2	[3, 4, 5, 102, 101, 100]
'''
def solution(arr, k):
    result = []
    for a in arr:
        if k % 2:
            result.append(a * k)
        elif not k % 2:
            result.append(a + k)
    return result
# print(solution([1, 2, 3, 100, 99, 98], 3))
# print(solution([1, 2, 3, 100, 99, 98], 2))


'''
알파벳 소문자로 이루어진 문자열 myString이 주어집니다. 
알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return 하는 solution 함수를 완성해 주세요.

myString	    result
"abcdevwxyz"	"lllllvwxyz"
"jjnnllkkmm"	"llnnllllmm"
'''
def solution(myString):
    result = ""
    for i, m in enumerate(myString):
        if m < "l":
            result += "l"
        else:
            result += m
    return result
# print(solution("abcdevwxyz"))
# print(solution("jjnnllkkmm"))


'''
정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.
arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.

n	result
3	[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
6	[[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
1	[[1]]
'''
def solution(n):
    result = []
    for i in range(n):
        r = []
        for j in range(n):
            p = 0
            if i == j:
                p = 1
            r.append(p)
        result.append(r)
    return result
# print(solution(3))
# print(solution(6))
# print(solution(1))
## 다른 풀이
# def solution(n):
#     result = [[0] * n for i in range(n)]
#     for i in range(n): result[i][i] = 1
#     return result
# 2차원 배열의 0으로 n x n 크기의 리스트를 생성한 후, result[i][j]에서 i == j인 경우의 리스트 요소값은 1로 지정한 후 반환한다.