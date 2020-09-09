import collections

class Solution:

    def numJewelsInStones(self, J: str, S: str) -> int:
        
        # ### 풀이1 ###
        # #jwrl_cnt[보석] = 돌에서 개수
        # jwrl_cnt = {}
        
        # #보석마다 기본값(0)을 넣어준다
        # for j in J:
        #     jwrl_cnt[j] = 0

        # #돌마다 확인한다
        # for s in S:
        #     if s in jwrl_cnt:
        #         jwrl_cnt[s] += 1
        
        # #합 리턴
        # return sum(jwrl_cnt.values())




        # ### 풀이2 ###
        # freqs = collections.defaultdict(int)
        # count = 0

        # #비교없이 돌(S) 빈도수 계산
        # for char in S:
        #     freqs[char] += 1
        
        # #비교없이 보석(J) 빈도수 계산
        # for char in J:
        #     count += freqs[char]

        # return count


        

        # ### 풀이3 ###
        # freqs = collections.Counter(S) #돌(S)의 빈도수 계산
        # count = 0

        # #비교없이 보석(J)의 빈도수 계산
        # for char in J:
        #     count += freqs[char]

        # return count




        ### 풀이4 ###
        return sum(s in J for s in S)
        
