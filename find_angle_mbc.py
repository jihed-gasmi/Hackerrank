
#inputs#
AB,BC=[int(input()) for i in range(2)]
#end#

#imports#
from math import sqrt,acos,pi
#end#

#formulas#
median=sqrt(BC**2+AB**2)*0.5
theta_pi=acos(BC/median*0.5)  # Al-qashi law of cosines
theta=round(theta_pi*180/pi)
#end#

#output#
AC=10
BC=10
print(f"{theta}\N{DEGREE SIGN}")
#end#
