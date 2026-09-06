nums = list(range(20, 28))

print(nums)


numbers = list(range(20))
print(numbers[::-1])


numbers = [1,2,3,4,5,6,7,8,12,23,43,23,21,123,43,234,234,234,2,3454,4,56]
first, *other , last = numbers
print(first, last)
print(other)


letters = ["a","b","c","d","e"]
for index, letter in enumerate(letters):
    print(index, letter)

#enumerate means to return both the index and the value of each element in the list.
letters.pop(0)
letters.remove("b")
del letters[0:3]

numbers.sort(reverse=True)

sorted_numbers = sorted(numbers, reverse=True)

# Do not alter the original list, but return a new sorted list.



