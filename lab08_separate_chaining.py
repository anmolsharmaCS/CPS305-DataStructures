# Big O complexity would be constant time O(1) for 2 or 3 operations (best case)
# if hash table gets more than 10 items in one index (worst case)
# The Big O complextiy would then be O(n) time, because 
# you would have to iterate by going through a list to insert/delete
# at the end of that particular index 

class HashTable_separate_chaining(object):
  def __init__(self):
    self.count = 0
    self.size = 11 # 11 entry hash table size
    self.key_numbers =  [ [] for i in range(self.size)]  # creating empty list 
    self.values = [ [] for i in range(self.size)] # creating empty list

  def hash_(self, key):
    return (3*key.__hash__()+5) % self.size

  def set(self, key, value):
    hash_value = self.hash_(key)
    
    if key in self.key_numbers[hash_value]:          # If the key already exists, find it and set the value
      index = self.key_numbers[hash_value].index(key)
      self.values[hash_value][index] = value  
    else:                                    # The key does not exist, append it 
      self.key_numbers[hash_value].append(key)
      self.values[hash_value].append(value)
      self.count += 1

  def get(self, key):
    value = None
    hash_value = self.hash_(key)
    
    if key in self.key_numbers[hash_value]:          # Check to see if key exist
      index = self.key_numbers[hash_value].index(key)
      value = self.values[hash_value][index]
    return value                             # return none if not found

  def __getitem__(self, key):
    return self.get(key)

  def __setitem__(self, key, value):
    return self.set(key, value)

H = HashTable_separate_chaining()
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

print(H.values)
print(H.key_numbers)

# 12 is at 8 
# 44 is at 5
# 13 is at 0
# 88 is at 5 >
# 23 is at 8 > 
# 94 is at 1
# 11 is at 5 > 
# 39 is at 1 >
# 20 is at 10 
# 16 is at 9  
#  5 is at 9 >