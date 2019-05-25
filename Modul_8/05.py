class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def __len__(self):
        return len(self.qlist)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)

    def dequeue(self):
        n = []
        for i in self.qlist:
            n.append(i.priority)
        print (self.qlist.pop(n.index(min(n))).item)

class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority


alvx = PriorityQueue()
alvx.enqueue('Minggu', 7)
alvx.enqueue('Senin', 1)
alvx.enqueue('Rabu', 3)
alvx.enqueue('Jumat', 5)
alvx.enqueue('Selasa', 2)
alvx.enqueue('Kamis', 4)
alvx.enqueue('Sabtu', 6)

