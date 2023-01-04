nb = 0

while nb <= 1000:
    i = 2
    while i < nb and nb % i != 0:
        i = i + 1

    if i == nb:
        print(nb)
    nb = nb + 1
