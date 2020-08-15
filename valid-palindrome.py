from collections import deque
import re

class Solution:

    # ############ Sol1 ############# 
    # def isPalindrome(self, s: str) -> bool:
    #     #문자와 숫자만 리스트에 넣기
    #     alpha = []
    #     for i in s:
    #         if i.isalpha():
    #             alpha.append(i.lower())
    #         elif i.isdigit():
    #             alpha.append(i)
        
    #     #팰린드롬 검사하기
    #     half = int(len(alpha)/2)
    #     length = len(alpha)
    #     for i in range(half):
    #         if alpha[i] != alpha[length-1-i]:
    #             return False
        
    #     return True

    ############# Sol2 #############
    # #내장 함수와 pop을 이용한 방법
    # def isPalindrome(self, s: str) -> bool:
    #     #전처리를 간결한 코드로
    #     alpha = []
    #     for char in s:
    #         if char.isalnum():
    #             alpha.append(char.lower())

    #     #팰린드롬 판별 : 0번째와 마지막번째를 pop하며 비교
    #     while len(alpha) > 1:
    #         if alpha.pop(0) != alpha.pop():
    #             return False
        
    #     return True  

    # ############# Sol3 #############
    # # Deque를 이용한 최적화
    # def isPalindrome(self, s: str) -> bool:
    #     # 자료형 데크로 선언
    #     strs: Deque = collections.deque()

    #     for char in s:
    #         if char.isalnum():
    #             strs.append(char.lower())

    #     # 데크의 앞과 뒤에서 pop하면서 비교한다.
    #     while len(strs) > 1:
    #         if strs.popleft() != strs.pop():
    #             return False
        
    #     return True


    ############# Sol4 #############
    # 슬라이싱을 사용한 풀이
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규표현식으로 문자, 숫자 제외 필터링
        s = re.sub('[^a-z0-9]', '', s)

        #배열을 뒤집어서 같은지 비교
        return s == s[::-1]
    


    