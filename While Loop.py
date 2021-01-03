error = 50.0
while error > 1 :
    error = error / 4
    print(error)


x = -2
while x < 10 :
    print(x)
    x = x +1

offset=8
while offset != 0:
        print("correcting...")
        offset = offset - 1
        print(offset)

offset=16
while offset != 0 :
    print("correcting...")
    if (offset>0) :
      offset=offset-1
    else :
      offset=offset+1
    print(offset)