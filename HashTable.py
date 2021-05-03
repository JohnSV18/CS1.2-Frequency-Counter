from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)

# Creates an array with linked lists
  def create_arr(self, size):
     
    arr = []

    for i in range(size):
      linked_list = LinkedList()
      arr.append(linked_list)

    return arr
# Hash function that will give us an index from counting the distance from a (first letter of the alphabet)
  def hash_func(self, key):
    first_letter = key[0].lower()
    distance_from_a = ord(first_letter) - ord('a')
    index = distance_from_a % self.size

    return index

# inserting key and value to the linked list
  def insert(self, key, value=1):
    key_hash = self.hash_func(key)
    linked_list = self.arr[key_hash]

    current = linked_list.head

    while current != None:

      if current.data[0] == key:
        current.data[1] += value
        return

      current = current.next
    
    linked_list.append([key, value])
  

# printing the key and values of the array
  def print_key_values(self):
    
    for linked_list in self.arr:
      current = linked_list.head

      while current != None:
        if current.data:
          print(f'{current.data[0]}: {current.data[1]}')

          current = current.next 

