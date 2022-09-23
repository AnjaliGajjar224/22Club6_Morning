"""
1. Arithmetic Operators
2. Comparison Operators
3. Assignment Operators
4. Bitwise Operators
5. Logical Operators
6. Membership Operators
7. Identity Operators
"""

# Arithmetic Operators

"""
1. + Addition
2. - Subtraction
3. * Multiplication
4. / Division
5. % Remainder(Modulus)
6. // (Floor division)
7. ** Exponent
"""

# print(5/2)
# print(5//2)
# print(5**3)

"""
Comparison Operators

1. == (Equal to)
2. != (Not equal to)
3. < (less than)
4. > (greater than)
5. <= (less than or equal to)
6. >= (greater tha or equal to)

---> Return boolean values(True, False)
"""

# print(5 == 5)
# print(5 != 5)
# print(5 < 9)
# print(5 > 8)
# print(5 <= 5)
# print(6 >= 9)

"""
Assignment Operators

1. =
2. += 
3. -=
4. *=
5. \=
...So on
"""

# a = 10
# print(a)

# a += 5                # a += 5 ---> a = a + 5 --> a = 10 + 5 = 15
# print(a)

# a -= 3               # a = a - 3 ---> a = 15 - 3 = 12
# print(a)

# a *= 2               
# print(a)

"""
Bitwise Operators

1. & - And
2. | - Or
3. ^ - XOR
4. Shift Operators
   ---> 1. << (left shift)
   ---> 2. >> (right shift)

Decimal to Binary Conversion: 
-----------------------------------

43 - 101011

2 | 43
2 | 21 ---> 1
2 | 10 ---> 1
2 | 5  ---> 0
2 | 2  ---> 1
  | 1  ---> 0

45 - 101101

Binary to Decimal Conversion:
------------------------------------

101011


      1 0  1 0 1 1
      * *  * * * *
---> 32 16 8 4 2 1

---> 32 * 1 + 0 * 16 + 8 * 1 + 4 * 0 + 2 * 1 + 1 * 1
   = 32 + 0 + 8 + 0 + 2 + 1
   = 43 
"""

"""
1. & (and)

Truth Table
----------------
a | b | a&b
0 | 0 | 0
0 | 1 | 0
1 | 0 | 0
1 | 1 | 1


43 - 1 0 1 0 1 1 
&    & & & & & &
45 - 1 0 1 1 0 1 
-----------------------
     1 0 1 0 0 1 (41)
"""

# print(43&45)


"""
2. | (or)

Truth Table
----------------
a | b | a|b
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 1


43 - 1 0 1 0 1 1 
|    | | | | | |
45 - 1 0 1 1 0 1 
-----------------------
     1 0 1 1 1 1 (47)
"""

# print(43|45)


"""
3. ^ (xor)

Truth Table
----------------
a | b | a^b
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 0


43 - 1 0 1 0 1 1 
^    ^ ^ ^ ^ ^ ^
45 - 1 0 1 1 0 1 
-----------------------
     0 0 0 1 1 0 (6)
"""
# print(43^45)

"""
4. Shift Operators

----> 1. >> (Right Shift)

43 - 101011

43 >> 2 - (?)

43 - 1  0  1 0 1 1 
     32 16 8 4 2 1

43 >> 1 -     1  0 1 0 1 1 
           32 16 8 4 2 1 

43 >> 2 -        1 0 1 0 1 1 
           32 16 8 4 2 1
     
43 >> 2 - 1010 (10)     
"""

# print(43 >> 2)
# print(43>>7)

"""
----> 2. << (Left Shift)

15 - 1111

15 << 3 - (?)

15 - 1 1 1 1 
     8 4 2 1 


15 << 1 -  1  1 1 1 0
           16 8 4 2 1

15 << 2 -  1  1 1 1 0 0
          32 16 8 4 2 1

15 << 3 -  1   1 1  1 0 0 0 
           64 32 16 8 4 2 1 

15 << 3 --> 1111000 (120)
"""

# print(15<<3)

"""
5. Logical Operators
---------------------
1. and (&&)
2. or (||)
3. not (!)

---> 1. and

Truth table
-----------------
a      | b      | a and b
False  | False  | False
False  | True   | False
True   | False  | False
True   | True   | True 


---> 2. not

a    | !a
True | False
False| True


----> Return a boolean Values
"""

# print(15 > 12 and 12 > 10)         # True and True = True
# print(15 > 12 and 12 < 10)

# print(15 > 12 or 12 < 10)

# print(not 15 > 12)

"""
6. Membership Operators
--> 1. in        2. not in

---> Return a boolean values
"""

# print('b' in 'banana')
# print('k' in 'banana')


# print('b' not in 'banana')
# print('k' not in 'banana')

# print('Python' in 'Python is a Fun')

# l = ["Royal","Hye","Bye","HEllo"]
# m = "Bye"

# print(m in l)


"""
Take a string and character from the user and check whether the character is in the string or not.
"""

# myStr = input("Enter your string: ")
# ch = input("Enter character: ")

# print(ch in myStr)
"""
7. Identity Operators

--> 1. is      2. is not
"""

# a = 10
# b = 15
# c = 10


# print(id(a))
# print(id(b))
# print(id(c))

# print(a is b)
# print(a is c)

# print(a is not c)