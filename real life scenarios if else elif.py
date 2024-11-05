#Real Life Scenarios
# Restaurant order discount

bill = float(input("Enter your bill: "))

if bill > 50:
    discount = bill * 0.1
    final_bill = bill - discount
    print ("Discount applied! YOur final bill is ${final_bill},")

else:
    print ("No discount applied. Your total bill is ${bill},")

