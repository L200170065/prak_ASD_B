class Queue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist.pop(0)

    ## 1.1 soal-soal untuk mahasiswa
    def getFrontMost(self):
        return self.qlist[0]

    ## 1.2 soal-soal untuk mahasiswa
    def getRearMost(self):
        return self.qlist[len(self.qlist) - 1]

alvx = Queue()
alvx.enqueue(10)
alvx.enqueue(2)
alvx.enqueue(4)
alvx.enqueue(22)

print (alvx.getFrontMost())
print (alvx.qlist)

print (alvx.getRearMost())
print (alvx.qlist)