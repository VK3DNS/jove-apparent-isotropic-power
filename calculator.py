from PySide6.QtCore import QObject, Signal, Slot

class Sender(QObject):
    receive_values = Signal(list)
    receive_Hz = Signal(float)
    receive_mG = Signal(float)
    receive_B = Signal(float)
    receive_K = Signal(float)
    receive_AuD = Signal(float)

class Calculator(QObject):
    def __init__(self, tx, Hz = None, mG =None, B = None, K = None, AuD = None, *args):
        from math import pi
        self.pi: float = pi
        self.C: float = 2.99792*10**8  # speed of light
        self.kB: float = 1.38065*10**-23  # boltzmann constant

        self.Hz: float = Hz if str(Hz).isnumeric() else 2.01 * 10 ** 7
        self.mG: float = mG if str(mG).isnumeric() else 9.3 * 10 ** 0
        self.B: float = B if str(B).isnumeric() else 6 * 10 ** 3
        self.K: float = K if str(K).isnumeric() else 9.1 * 10 ** 4
        self.AuD: float = AuD if str(AuD).isnumeric() else 4.2 * 10 ** 0

        self.isotropicpower: float = 0

        self.calculateisotropicpower()

        self.tx = tx

    @Slot()
    def values(self):
        self.tx.receive_values.emit([self.Hz, self.mG, self.B, self.K, self.AuD])

    @Slot()
    def get_Hz(self):
        self.tx.receive_Hz.emit(self.Hz)

    @Slot()
    def get_mG(self):
        self.tx.receive_mG.emit(self.mG)

    @Slot()
    def get_B(self):
        self.tx.receive_B.emit(self.B)

    @Slot()
    def get_K(self):
        self.tx.receive_K.emit(self.K)

    @Slot()
    def get_AuD(self):
        self.tx.receive_AuD.emit(self.AuD)

    @Slot(float)
    def set_Hz(self, Hz):
        self.Hz = float(Hz)
        self.calculateisotropicpower()
        self.tx.receive_Hz.emit(self.Hz)

    @Slot(float)
    def set_mG(self, mG):
        self.mG = float(mG)
        self.calculateisotropicpower()
        self.tx.receive_mG.emit(self.mG)

    @Slot(float)
    def set_B(self, B):
        self.B = float(B)
        self.calculateisotropicpower()
        self.tx.receive_B.emit(self.B)


    @Slot(float)
    def set_K(self, K, *args):
        self.K = float(K)
        self.calculateisotropicpower()
        self.tx.receive_K.emit(self.K)

    @Slot(float)
    def set_AuD(self, AuD):
        self.AuD = float(AuD)
        self.calculateisotropicpower()
        self.tx.receive_AuD.emit(self.AuD)

    def calculateisotropicpower(self, *args):
        λ: float = self.C/self.Hz  # wavelength
        G: float = 10**(self.mG/10)  # antenna gain
        Ae: float = G*λ**2/(4*self.pi)  # effective area

        W: float = self.kB*self.K*self.B  # power to antenna
        F: float = W/(Ae*self.B)  # flux density
        J: float = F*10**26  # Jansky, unused but it was in the sheet
        r: float = self.AuD*1.5*10**11  # distance to the sun (m)
        rSph: float = 4*self.pi*r**2  # surface area of sphere with radius r
        Wpms: float = 1/rSph  # watts per square meter

        iW: float = F/Wpms  # isotropic joules
        self.isotropicpower : float = iW*2*10**6
        return self.isotropicpower

def main():
    c = Calculator()
    print(c.isotropicpower)



if __name__ == "__main__":
    main()

