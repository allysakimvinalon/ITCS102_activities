pera = eval(input("Enter amount to deposit:"))
print("-------------------------------------")

libo = pera // 1000
libo_sukli = pera - (libo * 1000)
five_h = libo_sukli // 500
fiveh_sukli = libo_sukli - (five_h * 500)
two_h = fiveh_sukli // 200
twoh_sukli = fiveh_sukli - (two_h * 200)
one_h = twoh_sukli // 100
oneh_sukli = twoh_sukli - (one_h * 100)
fifty = oneh_sukli // 50
fifty_sukli = oneh_sukli - (fifty * 50)
twenty = fifty_sukli // 20
twenty_sukli = fifty_sukli - (twenty * 20)
ten = twenty_sukli // 10
ten_sukli = twenty_sukli - (ten * 10)
five = ten_sukli // 5
five_sukli = ten_sukli - (five * 5)
one = five_sukli // 1
one_sukli = five_sukli - (one * 1)

print(libo , "- 1000")
print(five_h , "- 500")
print(two_h , "- 200")
print(one_h , "- 100")
print(fifty , "- 50")
print(twenty , "- 20")
print(ten , "- 10")
print(five , "- 5")
print(one , "- 1")
