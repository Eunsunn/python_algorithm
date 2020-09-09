import collections

#key, value가 int인 해시맵
class HashMap:
    # 초기화
    def __init__(self):
        self.size = 1000 #해시 테이블 크기
        self.table = collections.defaultdict(ListNode) #존재하지 않는 키 조회시 자동으로 디폴트 생성

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size # 해시함수 = mod(해시테이블 크기)
        #index에 노드가 존재하지 않는 경우
        if self.table[index].value is None: #deafaultdict 결과 존재하지 않는 key 조회시 디폴트 객체 생성 -> .value로 조회
            self.table[index] = ListNode(key, value)
            return
        #index에 노드가 존재하는 경우
        p = self.table[index]
        while p:
            if p.key == key: #이미 key값이 있어서 중복되는 경우
                p.value = value #value를 갱신하고 return
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int):
        index = key % self.size
        #index에 노드가 없는 경우
        if self.table[index].value is None:
            return -1
        #index에 노드가 있는 경우
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int):
        index = key % self.size
        #index에 노드가 없는 경우: 잘못 삭제하는 경우
        if self.table[index].value is None:
            return
        #index에 노드가 있는 경우
        # Case1. 개별 체이닝의 첫번째 값을 삭제하는 경우
        p = self.table[index]
        if p.key == key: 
            self.table[index] = ListNode() if p.next is None else p.next
            return 
        # Case2. 첫번째 이후 값을 삭제하는 경우       
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


#해시맵의 버킷 (개별 체이닝)
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None