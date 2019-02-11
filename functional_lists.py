nos = [7, 8, 10, 3, 2, 4, 6]

# new evens list from nos list
# functional programming

ans = list(filter(lambda ele: not ele % 2, nos))
print(ans)

# squares of even cubes of odd
ans = tuple(map(lambda ele: ele ** 3 if ele % 2 else ele ** 2, nos))
print(ans)