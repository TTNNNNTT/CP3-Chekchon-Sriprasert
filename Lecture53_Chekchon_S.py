def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
priceInput = int(input("Price : "))
print(vatCalculate(priceInput))