# without using Generators

def numbers(nums):
    empty = []
    for num in nums:
        empty.append(num)
    return empty

no_gen = numbers([1,2,3,4,5,6,7,8])
print(no_gen)

# Using Generators

def numbers_2(nums):
    for num in nums:
        yield num
    
gen = numbers_2([1,2,3,4,5,6,7,8])
print(gen)
print(next(gen))

# Using List Comprehension and Genratores

nums = [1,2,3,4,5,6,7,8]
Both = (num for num in nums)

print(next(Both))


