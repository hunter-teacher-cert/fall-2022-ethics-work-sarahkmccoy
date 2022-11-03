bill = float(input("how much is the bill: "))
people = int(input("how many people: "))
tip = bill*.2
total= tip + bill
each = total/people
print("Each person pays: $"  + str(each))