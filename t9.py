#!/usr/bin/python

####################################################################
# T9 lookalike - T9 interpreter of a virtual mobile phone keyboard #
# Written by shainer - http://giudoku.sourceforge.net              #
####################################################################

def solve(number):
  length = len(number)
  associations = ["", "", "abc", "def", "ghi", "jkl", "mno", "prqs", "tuv", "wxyz"]
  poss = associations[int(number[0])] # gets the right string for the first digit
  cache = createCache(poss, length)   # creates the first cache

  for pos in range(1, len(number)):
    poss = associations[int(number[pos])]
    cache = limitCache(pos, poss, cache)

  # Gets only the first length character of the result
  # this is needed for partial matches who are actually bigger words
  for elem in range(len(cache)):
    cache[elem] = cache[elem][:length]

  print set(cache) # no duplicates in our output

# Checks if the given letter is right
def isBad(letter, button):
  for i in button:
    if letter == i:
      return False

  return True

# Reduces the cache by eliminating all the occurrences
# that doesn't have a digit contained in string at the right position
def limitCache(pos, string, oldCache):
  toRemove = []
  
  for word in oldCache:
    if isBad(word[pos], string):
      toRemove.append(word) # save the word for later not to mess up with the for cycle

  for occ in toRemove:
    oldCache.remove(occ)

  return oldCache

# Simply copies into the array every word beginning with the accepted letters
# and of the right length
def createCache(poss, length):
  array = []
  
  for letter in poss:
    
    filename = "ITALIANO." + letter.upper()
    fptr = open(filename, "r")

    for line in fptr:
      line = line.strip()

      if len(line) >= length:
        array.append(line)

    fptr.close()

  return array

if __name__ == "__main__":
  number = raw_input("Enter number: ")

  for c in number:
    if c == '1' or c == '0':
      print "[!!] Format error: 1 and 0 not allowed"
      exit(-1)

  solve(number)
