class Calculator():
    def __init__(self):
        from math import pi
        self.pi = pi
        self.C = 2.99792*10**8 #speed of light
        self.kB = 1.38065*10**-23 #boltzmann constant

    def isotropicpower(self, Hz, mG, B, K, AuD):
        #C = 3*10**8 #speed of light (1 sig fig)
        λ = self.C/Hz #wavelength
        G = 10**(mG/10) #antenna gain
        Ae = G*λ**2/(4*self.pi) #effective area

        W = self.kB*K*B #power to antenna
        F = W/(Ae*B) #flux density
        J = F*10**26 #Jansky, unused but it was in the sheet
        r = AuD*1.5*10**11 #distance to the sun (m)
        rSph = 4*self.pi*r**2 #surface area of sphere with radius r
        Wpms = 1/rSph #watts per square meter

        iW = F/Wpms #isotropic joules
        apparentIsotropicWattsOver2MHz = iW*2*10**6
        return apparentIsotropicWattsOver2MHz