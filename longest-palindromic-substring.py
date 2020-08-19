class Solution:

    # ############# Sol1 #############
    # # 주어진 길이의 모든 sub문자열을 확인한다
    # def longestPalindrome(self, s: str) -> str:
    #     #최대 길이부터 확인한다
    #     for size in range(len(s), 0, -1):
    #         #sublist를 확인한다
    #         start = 0
    #         end = start + size
    #         #size에 대해 한 칸씩 옮겨가면서 확인
    #         while end <= len(s):
    #             sublist = s[start:end]
    #             if sublist == sublist[::-1]:
    #                 return sublist
    #             start += 1
    #             end += 1
        
    #     return s[0]

    ############# Sol2 #############
    # 슬라이딩 윈도우로 투포인터를 이용해 팰린드롬 확인
    def longestPalindrome(self, s: str) -> str:
        #팰린드롬 판별 및 투포인터 확장
        def expand(left: int, right: int) -> str:
            #[left, right)를 같을 때까지 확장한다
            while left >=0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1:right-1]

        #해당 사항이 없을 때 빠르게 return
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        #슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result, expand(i,i+1), expand(i, i+2), key=len)
        
        return result

