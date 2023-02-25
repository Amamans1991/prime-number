#hello everyone

num= int(input ("please insert yput number:"))
if num>0:
    for i in range(2,num):
        if num%i == 0:
            print(num, "is not prime number")
            print(i,"itmes",num//i,"is",num)
            break
    else:
        print(num, "is the prime number")
else:
    print("invalid")   