

"""
7|8|9
-----
4|5|6
-----
1|2|3


X|X|O
-----
O|X|X
-----
X|O|O

None
"X"
"O"

Array [3][3]
"""


"""
def print_table(table):
    string = ""
    for row in table:
        for element in row:
            if element == None:
                string += " "
            else:
                string += element
            string += " "
        string += "\n"
    print(string)


def center_of(table):
    return table[1][1]



game1 = [["X", None, "O"],
         ["O", "X", "X"],
         ["X", "O", "O"]]


#print(game1[0][0])

#print_table(game1)

x = center_of(game1)
print(x)"""

# 0 1 1 2 3 5 8 13
z = 0
x = 0 
y = 1

print(x)
print(y)

while True:
    z = x + y 
    print(z)
    x = y
    y = z
    


