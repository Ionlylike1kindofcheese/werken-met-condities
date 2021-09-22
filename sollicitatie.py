print("U gaat een sollicitatie citeria invullen")
print("Antwoord bij alle vragen met ja of nee tenzij er word gezegd dat er iets anders genoteerd moet worden")

ervaring = input("Heeft u ervaring met dieren-dressuur, jongleren of acrobatiek? ")
if ervaring == ("ja"):
    print("Noteer alleen met nummers voor de volgende vragen.")
    welkberoep = input("Waarmee heeft u ervaring? 1: dieren-dressuur, 2: jongleren of 3: acrobatiek? ")
    if welkberoep == ("1"):
        dierendressuur = input("Hoeveel jaar heeft u ervaring hiermee? " )
        if dierendressuur >= ("4"):
            print("U heeft voldoende ervaring in dit beroep.")
        else:
            print("U voldoet helaas niet aan de eisen.")
    elif welkberoep == ("2"):
        jongleren = input("Hoeveel jaar heeft u ervaring hiermee? " )
        if jongleren >= ("5"):
            print("U heeft voldoende ervaring in dit beroep.")
        else:
            print("U voldoet helaas niet aan de eisen.")
    elif welkberoep == ("3"):
        acrobatiek = input("Hoeveel jaar heeft u ervaring hiermee? ")
        if acrobatiek >= ("3"):
            print("U heeft voldoende ervaring in dit beroep.")
        else:
            print("U voldoet helaas niet aan de eisen.")
elif ervaring == ("nee"):
    print("U voldoet helaas niet aan de eisen.")

mbodiploma = input("Bezit u een MBO-4 diploma? ")
if mbodiploma == ("ja"):
    vrachtwagen = input("Heeft u een geldig vrachtwagenbewijs? ")
    if vrachtwagen == ("ja"):
        hogehoed = input("Bent u in bezit van een hoge hoed? ")
        if hogehoed == ("ja"):
            certificaat = input("Heeft u een certificaat voor overleven met gevaarlijk personeel? ")
            if certificaat == ("ja"):
                print("We gaan u nu effe wat vragen stellen wat betreft uw geslacht")
            else:
                print("U voldoet helaas niet aan de eisen.")
        else:
            print("U voldoet helaas niet aan de eisen.")
    else:
        print("U voldoet helaas niet aan de eisen.")
else:
    print("U voldoet helaas niet aan de eisen.")

geslacht = input("Bent u een man of vrouw? ")
if geslacht == ("man"):
    snor = input("Hoelang is uw snor? Antwoord in centimeters. Als u geen snor heeft, antwoord dan met nee. ")
    if snor >= ("10"):
        print("We gaan u nu wat vragen stellen wat betreft lengte en gewicht.")
    else:
        print("U voldoet helaas niet aan de eisen.")
elif geslacht == ("vrouw"):
    krulhaar = input("Hoelang is uw rood krulhaar? Antwoord in centimeters. Als u geen rood krulhaar heeft, antwoord dan met nee. ")
    if krulhaar >= ("20"):
        print("We gaan u nu wat vragen stellen wat betreft lengte en gewicht.")
    else:
        print("U voldoet niet aan de eisen.")
else:
    print("U moet een man of vrouw zijn. Mocht u een andere gender hebben, dan voldoet u helaas niet aan de eisen.")

lengte = input("Hoelang bent u in centimeters? ")
if lengte >= ("150"):
    gewicht = input("Hoe zwaar weegt u in kilogram? ")
    if gewicht >= ("90"):
        print("Gefeliciteerd,")
    else:
        print("U voldoet helaas niet aan de eisen.")
else:
    print("U voldoet helaas niet aan de eisen.")

if ervaring == ("ja") and mbodiploma == ("ja") and (geslacht == ("man") or ("vrouw")) and lengte >= ("150"):
    print("U voldoet aan alle eisen")
else:
    print("Waarschijnlijk is er een error ontstaan. Excuses voor het ongemak. Probeer het a.u.b. opnieuw.")