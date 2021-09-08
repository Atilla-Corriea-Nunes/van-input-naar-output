croisantamount = input("Hoeveel croissants wilt u? ")

stokamount = input("Hoeveel stokbroden wilt u? ")





num2 = 0.39
num3 = 2.78


sum1 = int(croisantamount) * num2
sum2 = num3 * int(stokamount)
sum3 = sum1 + sum2

print('De feestlunch kost je bij de bakker '+ str(sum3) +' euro voor de '+ str(croisantamount) +' croissantjes en de '+ str(stokamount)  +' stokbroden als de 3 kortingsbonnen nog geldig zijn!')
