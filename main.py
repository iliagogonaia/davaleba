
#1.

ls = [i**3 for i in range(0,101,5)]
ls.sort(reverse = True)
print(ls[0])

#2.

ls = [i**3 for i in range(0,101,5)]
ls = iter(ls)
while True:
    try:
     print(next(ls))
    except StopIteration:
     break

#3.

ls = [i**3 for i in range(0,101,5)]
print(sum(ls) / len(ls))

#4.

tup = tuple(i**3 for i in range(0,101,5))
print(tup)
print(len(tup))

#5.

tup = tuple(i**3 for i in range(0,101,5))
it = iter(tup)
while True:
    try:
        print(next(it))
    except StopIteration:
        break


