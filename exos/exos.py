# Implement a group_by_owners function that:
# 	Accepts a dictionary containing the file owner name for each file name.
# 	Returns a dictionary containing a list of file names for each owner name, in any order

# For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners
# function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}

def group_by_owners(files):
    values = files.values()
    values = list(set(values))
    new_files = {}
    for value in values:
      new_files[value] = [i for i in files if files[i] == value]   
    return new_files

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))
    
    
# Implement the unique_names method. 
# When passed two lists of names, it will return a list containing the names that appear in either or both lists. 
# The returned list should have no duplicates.
# For example, calling unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma']) 
# should return a list containing Ava, Emma, Olivia, and Sophia in any order.

def unique_names(names1, names2):
    
    all_names = list(set(names1+names2))
    
    return all_names

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2))
    
# Binary search tree (BST) is a binary tree where the value of each node is larger or equal to the values in all the nodes in that node's left subtree and is smaller than the values in all the nodes in that node's right subtree.
# Write a function that, efficiently with respect to time used, checks if a given binary search tree contains a given value.
# For example, for the following tree:

# 	n1 (Value: 1, Left: null, Right: null)
# 	n2 (Value: 2, Left: n1, Right: n3)
# 	n3 (Value: 3, Left: null, Right: null)

# Call to contains(n2, 3) should return True since a tree with root at n2 contains number 3.
    
import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    
    if root.value == value:
      return True
    elif root.value < value:
      if root.right != None:
        return contains(root.right,value)
      else:
        return False
    elif root.value > value:
      if root.left != None:
        return contains(root.left,value)
      else:
        return False
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3))

# A playlist is considered a repeating playlist if any of the songs contain a reference to a previous song in the playlist. Otherwise, the playlist will end with the last song which points to None.
# Implement a function is_in_repeating_playlist that,efficiently with respect to time used, returns true if a playlist is repeating or false if it is not.
# For example, the following code prints "True" as both songs point to each other.
# first = Song("Hello")
# second = Song("Eye of the tiger")
    
# first.next_song(second)
# second.next_song(first)
    
# first.is_in_repeating_playlist()

class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_in_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        playlist = {self}
        next_song = self.next
        while next_song:
          if next_song in playlist:
            return True
          else: 
            playlist.add(next_song)
            next_song = next_song.next
        return False
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_in_repeating_playlist())

# Write a function that, when passed a list and a target sum, returns,efficiently with respect to time used, ;two ;distinct ;zero-based indices of any two of the numbers, whose sum is equal to the target sum. If there are no two numbers, the function should return None
# For example, find_two_sum([3, 1, 5, 7, 5, 9], 10) should return a single;tuple containing any of the following pairs of indices:

# 	0 and 3 (or 3 and 0) as 3 + 7;= 10
# 	1 and 5 (or 5 and 1);as 1;+ 9;= 10
# 	2 and 4;(or 4 and 2);as;5 + 5 = 10

def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    for i in numbers:
      for j in numbers:
        if i+j == target_sum:
          return ((numbers.index(i),numbers.index(j)))

    

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
    
# Implement the function find_roots to find the roots of the quadratic equation: ax² + bx + c = 0. 
# The function should return a tuple containing roots in any order.
# If the equation has only one solution, the function should return that solution as both elements of the tuple.
# The equation will always have at least one solution.

from math import *
def find_roots(a, b, c):
    discriminant = (b*b) - (4*a*c)
    
    return (((-b-sqrt(discriminant))/(2*a)),((-b+sqrt(discriminant))/(2*a)))

print(find_roots(2, 10, 8));


# The LeagueTable class tracks the score of each player in a league. After each game, the player records their score with the record_result function.
# The player's rank in the league is calculated using the following logic:</p>

# 	The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
# 	If two players are tied on score, then the player who has played the fewest games is ranked higher.
# 	If two players are tied on score and number of games played, then the player who was first in the list of players is ranked higher.

# Implement the player_rank function that returns the player at the given rank.

# For example:

# table = LeagueTable(['Mike', 'Chris', 'Arnold'])
# table.record_result('Mike', 2)
# table.record_result('Mike', 3)
# table.record_result('Arnold', 5)
# table.record_result('Chris', 5)
# print(table.player_rank(1))

# All players have the same score.However, Arnold and Chris have played fewer games than Mike, and as Chris is before Arnold in the list of players, he is ranked first. Therefore, the code above should display "Chris".

