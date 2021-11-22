# | computer memory |
# |.................|
# |....1 2.....1 6..|
# |....^.......^....|
# |....|.......|....|
# +----+-------+----+
#      |       |
#  a --+       |
#  b ----------+
#
# What does it mean for 'a' to be
# equal to 'b'?
#
# It means the value in memory
# where 'a' points to, is equal
# to the value where b points to
# the computer (CPU) itself has an
# instruction to compare two
# integers.

a = 2
b = 6

if a == b:
  print(a + b)
else:
  print(a * b)
