# 20240911 day14.py

# day14 리스트(배열)


'''
정수 리스트 num_list가 주어집니다. 
가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요. 
두 값이 같을 경우 그 값을 return합니다.

num_list	        result
[4, 2, 6, 1, 7, 6]	17
[-1, 2, 5, 6, 3]	8
'''
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))
# print(solution([4, 2, 6, 1, 7, 6]))
# print(solution([-1, 2, 5, 6, 3]))


'''
최대 5명씩 탑승가능한 놀이기구를 타기 위해 줄을 서있는 사람들의 이름이 담긴 문자열 리스트 names가 주어질 때, 
앞에서 부터 5명씩 묶은 그룹의 가장 앞에 서있는 사람들의 이름을 담은 리스트를 return하도록 solution 함수를 완성해주세요. 
마지막 그룹이 5명이 되지 않더라도 가장 앞에 있는 사람의 이름을 포함합니다.

names	                                                    result
["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]	["nami", "vex"]
'''
def solution(names):
    return names[::5]
# print(solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))


'''
오늘 해야 할 일이 담긴 문자열 배열 todo_list와 각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가 매개변수로 주어질 때, 
todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

todo_list	                                                finished	                result
["problemsolving", "practiceguitar", "swim", "studygraph"]	[true, false, true, false]	["practiceguitar", "studygraph"]
'''
def solution(todo_list, finished):
    return [t for t, f in zip(todo_list, finished) if not f]
# print(solution(["problemsolving", "practiceguitar", "swim", "studygraph"], [True, False, True, False]))


'''
정수 배열 numbers와 정수 n이 매개변수로 주어집니다. 
numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 하는 solution 함수를 작성해 주세요.

numbers	                    n	    result
[34, 5, 71, 29, 100, 34]	123	    139
[58, 44, 27, 10, 100]	    139	    239
'''
def solution(numbers, n):
    result = 0
    for num in numbers:
        result += num
        if result > n:
            return result
# print(solution([34, 5, 71, 29, 100, 34], 123))
# print(solution([58, 44, 27, 10, 100], 139))
## 다른 풀이
# def solution(numbers, n):
#     return next(sum(numbers[:i + 1]) for i in range(len(numbers)) if sum(numbers[:i + 1]) > n)
# next() : 반복 가능 객체의 다음 요소를 반환


'''
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e] 꼴입니다.
각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더합니다.
위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.

arr	                queries	                    result
[0, 1, 2, 3, 4]	    [[0, 1],[1, 2],[2, 3]]	    [1, 3, 4, 4, 4]
'''
def solution(arr, queries):
    for s, e in queries:
        for i in range(len(arr)):
            if s <= i <= e:
                arr[i] +=  1
    return arr
# print(solution([0, 1, 2, 3, 4], [[0, 1],[1, 2],[2, 3]]))
## 다른 풀이
# def solution(arr, queries):
#     for (s, e) in queries:
#         arr = [a + 1 if s <= i <= e else a for i, a in enumerate(arr)]
#     return arr
# arr을 s, e 기준으로 1을 더할지 그대로 출력할지 조건을 넣어 출력한다.