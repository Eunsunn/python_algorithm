class BinaryHeap(object):
    # 최소 힙
    def __init__(self):
        self.items = [None] # 인덱스 0은 사용하지 않기 위해
    
    def __len__(self):
        return len(self.items)-1

    def _percolate_up(self):
        i = len(self)
        parent = i//2
        while parent >= 0:
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] = self.items[i], self.items[parent]
            else:
                break
            i = parent
            parent = parent // 2

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def _percolate_down(self, idx):
        left = 2 * idx
        right = 2 * idx + 1
        smallest = idx
        
        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right
        if idx != smallest:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
            self._percolate_down(smallest)
            
       
    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted
