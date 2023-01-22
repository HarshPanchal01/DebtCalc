def Credit(balance):
    intrest = [1, 3, 5, 10]
    for i in range(len(intrest)):
        credit = 0
        for j in range(intrest[i]):
            credit = credit + balance
        credit = credit + credit*0.1999
        intrest[i] = credit
    return intrest

print(Credit(20000))
