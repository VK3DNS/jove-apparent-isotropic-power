from calculator import Calculator

c = Calculator()

Hz = 2.01*10**7 #base freq. (Hz)
mG = 9.3*10**0 #antenna maxgain (unit not specified, I assume dB)
B = 6*10**3 #bandwidth (Hz)
K = 1.41034*10**6 #antenna temp. (K)
AuD = 9.94111*10**-1 #distance to the sun (AU)
print(f'apparent isotropic power transmitted over the 2MHz band is {c.isotropicpower(Hz,mG,B,K,AuD)} Joules')