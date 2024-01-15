# Insert: O(1) — No collisions (best case)
# Insert: O(n) — If all the keys mapped to the same index,
# we would need to probe over all n elements (Worst Case)
# DOCKER TEST to trigger every 5 minutes

class HashTable_linear_probing:
    def __init__(self):
        self.size = 11
        self.values = [None] * self.size # create empty list size 11
        self.key_numbers = [None] * self.size  # create empty list size 11

    def hashfunction(self,key,size):
         return (3*key+5)%size

    def put(self,key,key_numbers):             # place values at hashvalue 
      hashvalue = self.hashfunction(key,len(self.values)) # the calculated hashvalue

      if self.values[hashvalue] == None:                 # if location is not taken, add value to location
        self.values[hashvalue] = key
        self.key_numbers[hashvalue] = key_numbers
      else:
        if self.values[hashvalue] == key:               # if value already exist
          self.key_numbers[hashvalue] = key_numbers # replace
        else:
          index = hashvalue
          while self.values[index] != None and \
                          self.values[index] != key:
            index = index + 1
            if index == len(self.values):
               index = 0
            

          if self.values[index] == None:
            self.values[index]=key
            self.key_numbers[index]=key_numbers
          else:
            self.key_numbers[index] = key_numbers #replace

    def __setitem__(self,key,key_numbers):
        self.put(key,key_numbers)

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
