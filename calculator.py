class Calculator():
    def __init__(self, Hz = 2.01 * 10 ** 7, mG = 9.3 * 10 ** 0, B = 6 * 10 ** 3, K = 9.1 * 10 ** 4, AuD = 4.2 * 10 ** 0, *args):
        from math import pi
        self.pi : float = pi
        self.C : float = 2.99792*10**8 #speed of light
        self.kB : float = 1.38065*10**-23 #boltzmann constant

        self.Hz : float = Hz  # base freq. (Hz)
        self.mG : float = mG # antenna maxgain (unit not specified, I assume dB)
        self.B : float = B  # bandwidth (Hz)
        self.K : float = K  # antenna temp. (K)
        self.AuD : float = AuD  # distance to object (AU) ##Jupiter is about 4.2 AU

        self.Hz : float = self.Hz if type(self.Hz) is int or float else 2.01 * 10 ** 7
        self.mG : float = self.mG if type(self.Hz) is int or float else 9.3 * 10 ** 0
        self.B : float = self.B if type(self.Hz) is int or float else 6 * 10 ** 3
        self.K : float = self.K if type(self.Hz) is int or float else 9.1 * 10 ** 4
        self.AuD : float = self.AuD if type(self.Hz) is int or float else 4.2 * 10 ** 0

        self.calculateisotropicpower()

    def values(self, *args):
        return [self.Hz,self.mG,self.B,self.K,self.AuD,self.isotropicpower]

    def get_Hz(self, *args):
        return self.Hz

    def get_mG(self, *args):
        return self.mG

    def get_B(self, *args):
        return self.B

    def get_K(self, *args):
        return self.K

    def get_AuD(self, *args):
        return self.AuD

    def set_Hz(self, *Hz):
        if len(Hz) == 1:
            if str(Hz[0]).isnumeric():
                self.Hz = float(Hz[0])
                self.calculateisotropicpower()
                return True
        return False

    def set_mG(self, *mG):
        if len(mG) == 1:
            if str(mG[0]).isnumeric():
                self.mG = float(mG[0])
                self.calculateisotropicpower()
                return True
        return False

    def set_B(self, *B):
        if len(B) == 1:
            if str(B[0]).isnumeric():
                self.B = float(B[0])
                self.calculateisotropicpower()
                return True
        return False

    def set_K(self, *K):
        if len(K) == 1:
            if str(K[0]).isnumeric():
                self.K = float(K[0])
                self.calculateisotropicpower()
                return True
        return False

    def set_AuD(self, *AuD):
        if len(AuD) == 1:
            if str(AuD[0]).isnumeric():
                self.AuD = float(AuD[0])
                self.calculateisotropicpower()
                return True
        return False

    def calculateisotropicpower(self, *args):
        λ : float = self.C/self.Hz #wavelength
        G : float = 10**(self.mG/10) #antenna gain
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

def main():
    c = Calculator()
    print(c.isotropicpower)

if __name__ == "__main__":
    main()

