from calculator import Calculator

c = Calculator()

Hz = 2.01*10**7 #base freq. (Hz)
mG = 9.3*10**0 #antenna maxgain (unit not specified, I assume dB)
B = 6*10**3 #bandwidth (Hz)
K = 9.1*10**4 #antenna temp. (K)
AuD = 4.2*10**0 #distance to object (AU) ##Jupiter is about 4.2 AU
print(f'apparent isotropic power transmitted over the 2MHz band is {c.isotropicpower(Hz,mG,B,K,AuD)} Joules')