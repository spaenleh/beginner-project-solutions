total = 99
for i in range(total, 0, -1):
    if i == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take it down and pass it around, no more bottles of beer on the wall.")
    elif i == 2:
        print("{0} bottles of beer on the wall, {0} bottles of beer.".format(i))
        print("Take it down and pass it around, 1 bottle of beer on the wall.")
    else:
        print("{0} bottles of beer on the wall, {0} bottles of beer.".format(i))
        print("Take it down and pass it around, {0} bottle of beer on the wall.".format(i - 1))

print("No more bottles of beer on the wall, no more bottles of beer.")
print("So go to the store and buy some more. {0} bottles of beer on the wall.".format(total))
