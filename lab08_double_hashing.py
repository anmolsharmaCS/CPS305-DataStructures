# Insert: O(1) — No collisions (best case)
# Insert: O(n) — If we are extremely unlucky,
# we may have to probe over all n element 
# and still not have any possible entries (Worst case)

class HashTable_double_hashing:
    def __init__(self):
        self.size = 11
        self.values = [None] * self.size
        self.key_numbers = [None] * self.size

    def hashfunction(self,key,size):
        return (3*key+5)%size

    def secondhashfunction(self,u,i,key,size):
         v = 7-(key%7)
         # (u + v * i) % size
         return (u + v * i)% size

    def put(self,key,key_numbers):
      hashvalue = self.hashfunction(key,len(self.values))

      if self.values[hashvalue] == None:
        self.values[hashvalue] = key
        self.key_numbers[hashvalue] = key_numbers
      else:
        if self.values[hashvalue] == key:
          self.key_numbers[hashvalue] = key_numbers  #replace
        else:
          index = hashvalue
          i= 0
          while self.values[index] != None and \
                            i != self.size:
              index = self.secondhashfunction(hashvalue,i,key,len(self.values))
              i=i+1         

          if self.values[index] == None:
            self.values[index]=key
            self.key_numbers[index]=key_numbers
          else:
            print('Not possible to enter {} into list '.format(key))

    def __setitem__(self,key,key_numbers):
        self.put(key,key_numbers)

H=HashTable_double_hashing()

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

print(H.key_numbers)
print(H.values)


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