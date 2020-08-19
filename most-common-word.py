import re
from typing import List
import operator

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-z0-9]', ' ', paragraph)
        words = [word.strip() for word in paragraph.split(' ') if word]

        cnt = {}
        for word in words:
            if word in cnt.keys():
                cnt[word] += 1
            else:
                cnt[word] = 1

        for ban in banned:
            if ban in cnt.keys():
                del cnt[ban]

        return max(cnt.items(), key=operator.itemgetter(1))[0]




if __name__ == '__main__':
    paragraph ="Bob. hIt, baLl"        
    banned = ["bob", "hit"]
    sol = Solution()
    print(sol.mostCommonWord(paragraph, banned))


