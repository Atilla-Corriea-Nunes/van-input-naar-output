pplamnt = input("Met hoeveel mensen ga je op uit? ")

vrbool = input("Wilt u gebruik maken van de VIP headset (Ja/Nee)? ")

str.lower(vrbool)


if (vrbool.lower() == "ja"):

    vrmin = input("Hoeveel minuten wilt u spenderen op de vrheadset? ") 
    num1 = 7.45
    num3 = 0.37
    num4 = 3
    num5 = 45
    sum1 = int(vrmin) / 5
    sum2 = sum1 * num3
    sum4 = num1 * int(pplamnt)
    sum3 = sum2 + sum4

    print('Dit geweldige dagje-uit met '+ str(pplamnt) +' mensen in de Speelhal met '+ str(num5) +' minuten VR kost je maar '+ str(sum3) +' euro')  

else:

    num1 = 7.45
    sum1 = int(pplamnt) * num1


    print('Dit geweldige dagje-uit met '+ str(pplamnt) +' mensen in de Speelhal kost je maar '+ str(sum1) +' euro')  


   









  



