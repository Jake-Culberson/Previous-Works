

#simple formula to help a friend calculate different values of acids and bases for their chemistry work. 
#made on the fly so not much useful versatility but if given the chance to work with a chemist i would enjoy 
#making this a much more versatile file

import math

mole = .1
ph = 5
pka = 4.76

#Ph = pka + math.log(x)

x = 10 ** (ph-pka)


Cacid = mole/(x+1)
Cbase = mole-Cacid

Vacid = Cacid * 9
Vbase = Cbase * 9

Macid = Cacid * (Vacid/1000)
Mbase = Cbase * (Vbase/1000)

test = ((Mbase-(.00001))/(Macid+(.00001)))

phTwo = 4.76 + math.log(test)


#"\nVacid = ", {Vacid}, "\nVbase = ", {Vbase}

print(test)
print(phTwo)

print(x)

print(f"Cacid = ", {Cacid}, "\nCbase = ", {Cbase}, "\nVacid = ", {Vacid}, "\nVbase = ", {Vbase},"\nMacid = ", {Macid}, "\nMbase = ", {Mbase})

