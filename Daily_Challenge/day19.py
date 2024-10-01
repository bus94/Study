# 20240920 day19.py

# day19 문자열, 리스트(배열)


'''
임의의 문자열이 주어졌을 때 문자 "a", "b", "c"를 구분자로 사용해 문자열을 나누고자 합니다.
예를 들어 주어진 문자열이 "baconlettucetomato"라면 나눠진 문자열 목록은 ["onlettu", "etom", "to"] 가 됩니다.
문자열 myStr이 주어졌을 때 위 예시와 같이 "a", "b", "c"를 사용해 나눠진 문자열을 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
단, 두 구분자 사이에 다른 문자가 없을 경우에는 아무것도 저장하지 않으며, return할 배열이 빈 배열이라면 ["EMPTY"]를 return 합니다.

myStr	                result
"baconlettucetomato"	["onlettu", "etom", "to"]
"abcd"	                ["d"]
"cabab"	                ["EMPTY"]
'''
def solution(myStr):
    myStr = myStr.replace("a", " ").replace("b", " ").replace("c", " ")
    result = myStr.strip().split()
    return result if result else ["EMPTY"]
# print(solution("baconlettucetomato"))
# print(solution("abcd"))
# print(solution("cabab"))
## 다른 풀이
# def solution(myStr):
#     answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
#     return answer if answer else ['EMPTY']
# 같은 알고리즘의 코드


'''
아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 
양의 정수 배열 arr가 매개변수로 주어질 때, 
arr의 앞에서부터 차례대로 원소를 보면서 원소가 a라면 X의 맨 뒤에 a를 a번 추가하는 일을 반복한 뒤의 배열 X를 return 하는 solution 함수를 작성해 주세요.

arr	        result
[5, 1, 4]	[5, 5, 5, 5, 5, 1, 4, 4, 4, 4]
[6, 6]	    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[1]	        [1]
'''
def solution(arr):
    x = []
    for a in arr:
        for i in range(a):
            x.append(a)
    return x
# print(solution([5, 1, 4]))
# print(solution([6, 6]))
# print(solution([1]))
## 다른 풀이
# def solution(arr):
#     return [i for i in arr for j in range(i)]
# 같은 알고리즘의 코드


'''
아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 
길이가 같은 정수 배열 arr과 boolean 배열 flag가 매개변수로 주어질 때, 
flag를 차례대로 순회하며 flag[i]가 true라면 X의 뒤에 arr[i]를 arr[i] × 2 번 추가하고, 
flag[i]가 false라면 X에서 마지막 arr[i]개의 원소를 제거한 뒤 X를 return 하는 solution 함수를 작성해 주세요.

arr	            flag	                            result
[3, 2, 4, 1, 3]	[true, false, true, false, false]	[3, 3, 3, 3, 4, 4, 4, 4]
'''
def solution(arr, flag):
    x = []
    for i, f in enumerate(flag):
        if f:
            for j in range(arr[i] * 2):
                x.append(arr[i])
        else:
            for j in range(arr[i]):
                del x[-1]
    return x
# print(solution([3, 2, 4, 1, 3], [True, False, True, False, False]))
## 다른 풀이
# def solution(arr, flag):
#     X = []
#     for i, f in enumerate(flag):
#         if f:
#             X += [arr[i]] * (arr[i] * 2)
#         else:
#             for _ in range(arr[i]):
#                 X.pop()
#     return X
# arr에 대한 반복문을 따로 작성하지 않고 실행한다. 그리고 만약 flag가 False라면 맨 뒤의 값을 삭제한다.


'''
0과 1로만 이루어진 정수 배열 arr가 주어집니다. arr를 이용해 새로운 배열 stk을 만드려고 합니다.
i의 초기값을 0으로 설정하고 i가 arr의 길이보다 작으면 다음을 반복합니다.
만약 stk이 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
stk에 원소가 있고, stk의 마지막 원소가 arr[i]와 같으면 stk의 마지막 원소를 stk에서 제거하고 i에 1을 더합니다.
stk에 원소가 있는데 stk의 마지막 원소가 arr[i]와 다르면 stk의 맨 마지막에 arr[i]를 추가하고 i에 1을 더합니다.
위 작업을 마친 후 만들어진 stk을 return 하는 solution 함수를 완성해 주세요.
단, 만약 빈 배열을 return 해야한다면 [-1]을 return 합니다.

arr	            result
[0, 1, 1, 1, 0]	[0, 1, 0]
[0, 1, 0, 1, 0]	[0, 1, 0, 1, 0]
[0, 1, 1, 0]	[-1]
'''
def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            stk.pop()
        elif stk[-1] != arr[i]:
            stk.append(arr[i])
        i += 1
    return stk if stk else [-1]
# print(solution([0, 1, 1, 1, 0]))
# print(solution([0, 1, 0, 1, 0]))
# print(solution([0, 1, 1, 0]))


'''
랜덤으로 서로 다른 k개의 수를 저장한 배열을 만드려고 합니다. 
적절한 방법이 떠오르지 않기 때문에 일정한 범위 내에서 무작위로 수를 뽑은 후, 지금까지 나온적이 없는 수이면 배열 맨 뒤에 추가하는 방식으로 만들기로 합니다.
이미 어떤 수가 무작위로 주어질지 알고 있다고 가정하고, 실제 만들어질 길이 k의 배열을 예상해봅시다.
정수 배열 arr가 주어집니다. 문제에서의 무작위의 수는 arr에 저장된 순서대로 주어질 예정이라고 했을 때, 완성될 배열을 return 하는 solution 함수를 완성해 주세요.
단, 완성될 배열의 길이가 k보다 작으면 나머지 값을 전부 -1로 채워서 return 합니다.

arr	                k	result
[0, 1, 1, 2, 2, 3]	3	[0, 1, 2]
[0, 1, 1, 1, 1]	    4	[0, 1, -1, -1]
'''
def solution(arr, k):
    result = []
    for i in range(len(arr)):
        if not result or not arr[i] in result:
            result.append(arr[i])
        if len(result) == k:
            break
    while len(result) < k:
        result.append(-1)
    return result
# print(solution([0, 1, 1, 2, 2, 3], 3))
# print(solution([0, 1, 1, 1, 1], 4))
## 다른 풀이
# def solution(arr, k):
#     result = []
#     for i in arr:
#         if i not in result:
#             result.append(i)
#         if len(result) == k:
#             break
#     return result + [-1] * (k - len(result))
# 같은 알고리즘의 코드
# if문에서 line 134에서 result가 비어있는 경우의 조건이 있는데, 어차피 arr[i]가 result 안에 없다는 조건에 들어가게 되므로 코드를 줄일 수 있다.