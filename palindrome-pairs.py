from typing import List
import collections

class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.children = collections.defaultdict(TrieNode)
        self.p = [] # 현재 글자까지 봤을 때, 그 앞의 글자들이 팰린드롬인가? (word index)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def check_palindrome(word):
        return word == word[::-1]

    def insert(self, word, idx):
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.check_palindrome(word[:len(word)-i]):
                node.p.append(idx)
            node = node.children[char]
        node.word_id = idx

    
    def search(self, word, idx):
        ret = []
        node = self.root
        i = 0
        for i in range(len(word)):
            char = word[i]
            # 앞 > 뒤: 내려오다가 마주친 짧은 글자들
            if node.word_id >= 0:
                if self.check_palindrome(word[i:]) and idx != node.word_id:
                    ret.append([idx, node.word_id])
            # 내려갈 경로가 없으면 반복 종료
            if char not in node.children:
                return ret
            node = node.children[char]
        
        # 앞 글자를 모두 검사한 경우만
        # 앞 < 뒤
        for p_idx in node.p:
                ret.append([idx, p_idx])
        # 앞 = 뒤
        if node.word_id >= 0 and node.word_id != idx:
            ret.append([idx, node.word_id])
            
        return ret


class Solution:
    # def checkPalindrome(self, w1: str, w2: str) -> bool:
    #     string = w1 + w2
    #     return string == string[::-1]

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # # 1. Brute Force: 시간 초과
        # ret = []
        # for i in range(len(words)):
        #     for j in range(len(words)):
        #         if i==j: continue
        #         if self.checkPalindrome(words[i], words[j]):
        #             ret.append([i, j])
        # return ret

        
        # 2. Trie를 이용한 풀이
        # reversed Trie를 생성한다.
        trie = Trie()
        for idx, word in enumerate(words):
            trie.insert(word, idx)

        # 각 단어마다 팰린드롬 쌍을 검사한다.
        ret = []
        for idx, word in enumerate(words):
            ret.extend(trie.search(word, idx))
        
        return ret



if __name__ == "__main__":
    words = ["a","abc","aba",""]
    sol = Solution()
    print(sol.palindromePairs(words))