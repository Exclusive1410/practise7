#1 Implement a script which receives a string and replaces all " symbols with ' and vise versa. The script should return modified string.

print('-----------')

#2 Write a script that checks whether a string is a palindrome or not.
x = "refer"
w = ""
for i in x:
    w = i + w
if (x == w):
    print("Yes")
else:
    print("No")

print('-----------')

#3 Implement a script which works the same as str.split
def split(word):
    return [char for char in word]

word = 'geeks'
print(split(word))

print('-----------')

#4 Implement a script which returns the longest word in the given string.
def longestword(a):
    max1 = len(a[0])
    temp = a[0]
    for i in a:
        if (len(i) > max1):
            max1 = len(i)
            temp = i

    print('The word with the longest length is : ', temp)

a = ['egor', 'slava', 'nastya', 'anya']
longestword(a)

print('-----------')

#5 For a positive integer n calculate the result value, which is equal to the sum of the odd numbers of n.

print('-----------')

#6 Create a script that for a positive integer n calculates the result value, which is equal to the sum of the “1” in the binary representation of n otherwise, returns None.

print(bin(14).count('1'))

#7 map = [ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" ]

map = [ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" ]

opposites = { "NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST" }

def reduction(list):
    new_list = [ ]
    for i in range(0,len(list)):
        if len(new_list) == 0:
            new_list.append(list[i])
        elif new_list[-1] != opposites[list[i]]:
            new_list.append(list[i])
        else:
            new_list.pop()
    return new_list

new_map = reduction(map)
print(f"Final map is {new_map}")

#8 English Shiritori has the same principle, with the first and last letters of words. That being said the lose condition is saying a word that doesn't start with the previous word's last letter or not saying a word quick enough.
 