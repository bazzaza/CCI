class HashMap:
    def __init__(self,size=1000):
        self.size  = size
        self.array = [None for i in range(self.size)]

    def get_hash(self,s):
        sum = 0
        for c in s:
            sum += ord(c)
        return sum%self.size

    def add(self, key,val):
        i = self.get_hash(key)
        self.array[i] = (key,val)

    def get(self, s):
        i = self.get_hash(s)
        return self.array[i][1]


if __name__ == '__main__':
    map = HashMap()
    map.add("srk",0.23)
    map.add("btc",55000)
    map.add("eth",1800)