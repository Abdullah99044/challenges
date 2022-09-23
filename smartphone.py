
def cheap_phone(cheap_phone , cheap_price ):
    return  "De {} is het goedKoopst, de telefoon kost {} Euro".format(cheap_phone  , cheap_price )

def expensive_phone(expensive_phone ,  expensive_price ):
    return "De {} is het duurst, de telefoon kost {} Euro".format(expensive_phone , expensive_price)

def result( cheap_phone , expensive_phone , deffrince ):
    return "Het advies is dus de {} te kopen. Deze is namelijk {} euro goedkoper dan {}".format(cheap_phone , deffrince , expensive_phone )

def diffrence(num1 ,num2):
    return num1 - num2


def advise(iphone , samsung  ):
    if iphone  > 900 and samsung > 900:
        return "Het advies is dus geen telefoon te kopen , ze zijn te duur"
    
    elif iphone > 900 :
       
        return result( "samsung" , "iphone" ,  diffrence(iphone  , samsung) )
    
    elif samsung > 900 :
       
        return result( "iphone" , "samsung"  ,  diffrence( samsung , iphone) )

    else:
        if iphone > samsung:


            deffrince =  diffrence( iphone , samsung )  

            if deffrince > 50 :
                return result( "samsung" , "iphone"  ,deffrince )
                
            else:
                return "Het advies is dus de iphon te kopen. Deze is namelijk {} euro duurder dan samsung".format(deffrince )
                
        else:
            deffrince = diffrence( samsung , iphone )  
            return result( "iphone" , "samsung" , deffrince )
        

iphone = float(input("Hoe duur is de iphone  : "))
samsung = float(input("Hoe duur is de samsung  : "))
print("*************************")
 

if iphone < samsung:
    print(cheap_phone(" iphone " , iphone ))
    print(expensive_phone(" samsung " , samsung ))
    print(advise(iphone , samsung  ))

else:
    print(cheap_phone(" samsung " , samsung))
    print(expensive_phone( " iphone " , iphone ))
    print(advise(iphone , samsung  ))