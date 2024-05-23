class Calculator():
    def __init__(self, *args):
        from math import pi
        self.pi = pi
        self.C = 2.99792*10**8 #speed of light
        self.kB = 1.38065*10**-23 #boltzmann constant

        self.Hz = 2.01 * 10 ** 7  # base freq. (Hz)
        self.mG = 9.3 * 10 ** 0  # antenna maxgain (unit not specified, I assume dB)
        self.B = 6 * 10 ** 3  # bandwidth (Hz)
        self.K = 9.1 * 10 ** 4  # antenna temp. (K)
        self.AuD = 4.2 * 10 ** 0  # distance to object (AU) ##Jupiter is about 4.2 AU

        self.calculateisotropicpower()

    def set_Hz(self, *Hz):
        if len(Hz) == 1:
            if Hz[0].isnumeric():
                self.Hz = float(Hz[0])
                self.calculateisotropicpower()
                return True
        return False

    def set_mG(self, *mG):
        if len(mG) == 1:
            if mG[0].isnumeric():
                self.mG = float(mG[0])
                self.calculateisotropicpower()
                return True
        return False

    def set_B(self, *B):
        if len(B) == 1:
            if B[0].isnumeric():
                self.B = float(B[0])
                self.calculateisotropicpower()
                return True
        return False

    def set_K(self, *K):
        if len(K) == 1:
            if K[0].isnumeric():
                self.K = float(K[0])
                self.calculateisotropicpower()
                return True
        return False

    def set_AuD(self, *AuD):
        if len(AuD) == 1:
            if AuD[0].isnumeric():
                self.AuD = float(AuD[0])
                self.calculateisotropicpower()
                return True
        return False

    def calculateisotropicpower(self, *args):
        λ : float = self.C/self.Hz #wavelength
        G : float= 10**(self.mG/10) #antenna gain
        Ae : float = G*λ**2/(4*self.pi) #effective area

        W : float = self.kB*self.K*self.B #power to antenna
        F : float = W/(Ae*self.B) #flux density
        J : float = F*10**26 #Jansky, unused but it was in the sheet
        r : float = self.AuD*1.5*10**11 #distance to the sun (m)
        rSph : float = 4*self.pi*r**2 #surface area of sphere with radius r
        Wpms : float = 1/rSph #watts per square meter

        iW : float = F/Wpms #isotropic joules
        self.isotropicpower : float = iW*2*10**6
        return self.isotropicpower