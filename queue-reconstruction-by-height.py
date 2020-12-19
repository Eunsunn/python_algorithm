from typing import List
import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # max queue에 키 순으로 입력
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1])) # 첫번째 값(-persion[0]) 기준 정렬

        ret = []
        while heap:
            person = heapq.heappop(heap)
            ret.insert(person[1], [-person[0], person[1]])
        
        return ret


if __name__ == "__main__":
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    sol = Solution()
    sol.reconstructQueue(people)