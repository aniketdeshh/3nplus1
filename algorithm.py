current = int(input('Enter a positive integer >> '))
previous = 0

while current != 1.0:
    previous = current
    if current % 2 == 0:  
        current /= 2
    else:
        current *= 3
        current += 1
    print(current)


