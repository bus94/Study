# 20240924 day21.py

# day21 함수(메서드)


'''
정수로 이루어진 리스트 num_list가 주어집니다. 
num_list에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

num_list	                            result
[12, 4, 15, 46, 38, 1, 14, 56, 32, 10]	[15, 32, 38, 46, 56]
'''
def solution(num_list):
    return sorted(num_list)[5:]
# print(solution([12, 4, 15, 46, 38, 1, 14, 56, 32, 10]))


'''
0번부터 n - 1번까지 n명의 학생 중 3명을 선발하는 전국 대회 선발 고사를 보았습니다. 
등수가 높은 3명을 선발해야 하지만, 개인 사정으로 전국 대회에 참여하지 못하는 학생들이 있어 참여가 가능한 학생 중 등수가 높은 3명을 선발하기로 했습니다.
각 학생들의 선발 고사 등수를 담은 정수 배열 rank와 전국 대회 참여 가능 여부가 담긴 boolean 배열 attendance가 매개변수로 주어집니다. 
전국 대회에 선발된 학생 번호들을 등수가 높은 순서대로 각각 a, b, c번이라고 할 때 10000 × a + 100 × b + c를 return 하는 solution 함수를 작성해 주세요.

rank	                attendance	                                    result
[3, 7, 2, 5, 4, 6, 1]	[false, true, true, true, true, false, false]	20403
[1, 2, 3]	            [true, true, true]	                            102
[6, 1, 5, 2, 3, 4]	    [true, false, true, false, false, true]	        50200
'''
def solution(rank, attendance):
    attend_rank = []
    for i, r in enumerate(rank):
        if attendance[i]:
            attend_rank.append(r)
    select_rank = sorted(attend_rank)[:3]
    return 10000 * rank.index(select_rank[0]) + 100 * rank.index(select_rank[1]) + rank.index(select_rank[2])
# print(solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False]))
# print(solution([1, 2, 3], [True, True, True]))
# print(solution([6, 1, 5, 2, 3, 4], [True, False, True, False, False, True]))
## 다른 풀이
# def solution(rank, attendance):
#     arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
#     return 10000 * arr[0][1] + 100 * arr[1][1] + arr[2][1]
# 튜플을 이용하여 rank의 인덱스마다 attendance를 검사하여 참일 때 해당 데이터 x와 인덱스 i를 가지고 정렬해서 리스트로 arr에 저장한다.
# ** 여기서 sorted는 튜플의 앞에 있는 값을 기준으로 정렬한다. (if. (i, x)로 저장했다면 i를 기준으로 정렬하기 때문에 원하는 정렬의 값이 나오지 않는다.)
# 이후 리스트의 0, 1, 2번째(등수가 높은 순서)의 인덱스값 arr[][1]로 값을 가져온다. (arr[][0]이면 데이터 x를 가져올 수 있다.)


'''
실수 flo가 매개 변수로 주어질 때, flo의 정수 부분을 return하도록 solution 함수를 완성해주세요.

flo	    result
1.42	1
69.32	69
'''
def solution(flo):
    return int(flo)
# print(solution(1.42))
# print(solution(69.32))


'''
한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.

num_str	        result
"123456789"	    45
"1000000"	    1
'''
def solution(num_str):
    return sum(list(map(int, num_str)))
# print(solution("123456789"))
# print(solution("1000000"))


'''
숫자로만 이루어진 문자열 n_str이 주어질 때, n_str을 정수로 변환하여 return하도록 solution 함수를 완성해주세요.

n_str	result
"10"	10
"8542"	8542
'''
def solution(n_str):
    return int(n_str)
# print(solution("10"))
# print(solution("8542"))