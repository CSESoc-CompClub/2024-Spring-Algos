# 2024 Spring - Problem Solving & Algorithms - Cheatsheet

- [2024 Spring - Problem Solving \& Algorithms - Cheatsheet](#2024-spring---problem-solving--algorithms---cheatsheet)
  - [For Loops](#for-loops)
  - [List Splicing](#list-splicing)
  - [str()](#str)
  - [split()](#split)
  - [Linear Search](#linear-search)
  - [Binary Search](#binary-search)
  - [Max Sub-array](#max-sub-array)

## For Loops
Just like any other programming languanges, Python has loops built it to it. For this section, we will be focusing solely on `for` loops.

```
for i in range(10):
  print(i)
```
In general, there are 4 components that define a `for` loop. 

1. The `for` keyword indicates that we are defining a `for` loop
2. The `i` indicates the counter
3. And the `range` indicates... well... the range. Basically how far the loop is gonna go
4. After the `:`, any code below this line that is indexed some tab space in is the logic/code that will be repeated. In the example, this logic is simply `print(i)`

Much like other programming languages, Python is zero indexed, meaning that numbers start from 0 instead of 1. Meaning that declaring `range(10)` actually gives you 0-9 instead of 1-10.

## List Splicing
List splicing refers to the process of extracting subset(s) from a list or array. This basically allows you to select sections or portions of a list. 

Let's say you have the word **pineapple**. You *splice* your **pineapple** and extract the word **apple**. This is basically list splicing, but instead of fruits, you are splicing arrays and lists.

```
fruit = ["p", "i", "n", "e", "a", "p", "p", "l", "e"]
apple = fruit[4:8:1]
print(apple)
```

To list splice, simply refer to your list and in square brackets declare your **starting index**, **ending index** and your **step**. So, you get something like: `list[start:stop:step]`.

Note that the stop index is exclusive. This means that for example from **pineapple** you want to splice the string "pine". Since the ending letter 'e' is in index 3, you would want to stop at 4 since the stop index is not inclusive.

## str()
`str()` is a builtin function from Python and transforms whatever you input into a string.

```
number = 10
string = str(10)
```

In this example, the `string` variable represents a string value equal to "10".

## split()
Similar to splicing, `split()` allows you to split a list/array into multiple different sections. 

```
fullName = "Robert Downey Jr."
splitName = fullName.split(" ")

print(splitName) # ['Robert', 'Downey', 'Jr.']
```

The `split()` function takes in a separator which indicates at what characters you want to split. This case, we split when we encounter a whitespace. Note that `split()` can also take a second optional argument. This second argument represents the number of splits you can do before stopping.

```
fullName = "Robert Downey Jr."
splitName = fullName.split(" ", 1)

print(splitName) # ['Robert', 'Downey Jr.']
```

## Linear Search
Goes through all the index of a list from start to finish and returns the index of the value if the value is found. Will return -1 if the value is not found

```
list = [33,45,12,4,5,3,987,42]
indexOfTwelve = linear_search(list, 12)

print(indexOfTwelve) # 2
```

## Binary Search
> Note: Binary search will only properly work when the given list is sorted (preferably in ascending order)

Binary search does the same purpose as `linear_search` but faster. The only downside is that in order to work properly, the given list must be ordered.

Binary search works by first splitting down the midpoint of the list, they see if the current value is lower or greater than the target value. If greater, they dispose of everything on their left and vice versa if the current value is lower. This repeats until there is only one value left.

```
list = [12,17,23,29,56,76,77,98]
indexOfSeventeen = binary_search(list, 17)

print(indexOfSeventeen) # 1
```

A detailed view:
```
target = 17
original_list = [12,17,23,29,56,76,77,98]
                 ^           ^         ^
                 L           M         R

** 56 is bigger than 17, take the left! **

first_step    = [12,17,23,29]
                 ^     ^  ^         
                 L     M  R       

** 23 is bigger than 17, take the left! **

second_step   = [12,17]
                 ^  ^         
                 L  M and R   

** Current M = 17, found!

return indexOf(17)

```

## Max Sub-array
`Max Sub-array` is a function that returns the maximum sum subarray of an array. Basically, in a list of integers, this functions returns the subarray which makes up the largest sum.

For the array `[1, -2, 3, 5, -1, 2]`, the function would return the subarray `[3, 5, -1, 2]`, which has the maximum sum. No other combinations of adjacent numbers make a sum bigger than *3 + 5 - 1 + 2 = 9*

```
list = [1, -2, 3, 5, -1, 2]
maxSubarray = max_subarray(list)

print(maxSubarray) # [3, 5, -1, 2]
```
