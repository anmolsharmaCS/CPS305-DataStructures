class HashTable_linear_probing:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = hashvalue
          i= 0
          while self.slots[nextslot] != None and \
                            i != self.size:
              nextslot = self.secondhashfunction(hashvalue,i,key,len(self.slots))
              i=i+1         

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            print('Not possible to enter {} into list '.format(key))

    def hashfunction(self,key,size):
        return (3*key+5)%size
      
    def secondhashfunction(self,u,i,key,size):
         v = 7-(key%7)
         # (u + v * i) % size
         return (u + v * i)% size
 

    def rehash(self,oldhash,size):
        return (3*oldhash+5)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

H=HashTable_linear_probing()

H[12]="key0"
H[44]="key1"
H[13]="key2"
H[88]="key3"
H[23]="key4"
H[94]="key5"
H[11]="key6"
H[39]="key7"
H[20]="key8"
H[16]="key9"
H[5]="key11"

print(H.data)
print(H.slots)


# 12 is at 8 
# 44 is at 5
# 13 is at 0
# 88 is at 5 > 6
# 23 is at 8>9 
# 94 is at 1
# 11 is at 5 > 7
# 39 is at 1 >2
# 20 is at 10 
# 16 is at 9> 4