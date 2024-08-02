from PySide6.QtCore import QObject, Signal, Slot


class Sender(QObject):
    """
    class Sender:
    Send values to the calculator.

    Attributes:
        receive_values: Signal
        receive_Hz: Signal
        receive_mG: Signal
        receive_B: Signal
        receive_K: Signal
        receive_AuD: Signal
    """
    receive_values = Signal(list)
    receive_Hz = Signal(float)
    receive_mG = Signal(float)
    receive_B = Signal(float)
    receive_K = Signal(float)
    receive_AuD = Signal(float)


class Calculator(QObject):
    """
    class Calculator(QObject):
    Calculate the isotropic power.

    Attributes:
        pi: float
        C: float
        kB: float
        Hz: float
        mG: float
        B: float
        K: float
        AuD: float
        isotropicpower: float
        tx: instance of class Sender

    Methods:
        values(self)
        get_Hz(self)
        get_mG(self)
        get_B(self)
        get_K(self)
        get_AuD(self)
        set_Hz(self, Hz)
        set_mG(self, mG)
        set_B(self, B)
        set_K(self, K)
        set_AuD(self, AuD)
        calculateisotropicpower(self)
    """
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
        """
        @Slot()
        values(self)
        Send the values to the calculator.

        Key lines:
            self.tx.receive_values.emit([self.Hz, self.mG, self.B, self.K, self.AuD])
        """
        self.tx.receive_values.emit([self.Hz, self.mG, self.B, self.K, self.AuD, self.isotropicpower])

    @Slot()
    def get_Hz(self):
        """
        @Slot()
        get_Hz(self)
        Send the Hz value to the calculator.

        Key lines:
            self.tx.receive_Hz.emit(self.Hz)
        """
        self.tx.receive_Hz.emit(self.Hz)

    @Slot()
    def get_mG(self):
        """
        @Slot()
        get_mG(self)
        Send the mG value to the calculator.

        Key lines:
            self.tx.receive_mG.emit(self.mG)
        """
        self.tx.receive_mG.emit(self.mG)

    @Slot()
    def get_B(self):
        """
        @Slot()
        get_B(self)
        Send the B value to the calculator.

        Key lines:
            self.tx.receive_B.emit(self.B)
        """
        self.tx.receive_B.emit(self.B)

    @Slot()
    def get_K(self):
        """
        @Slot()
        get_K(self)
        Send the K value to the calculator.

        Key lines:
            self.tx.receive_K.emit(self.K)
        """
        self.tx.receive_K.emit(self.K)

    @Slot()
    def get_AuD(self):
        """
        @Slot()
        get_AuD(self)
        Send the AuD value to the calculator.

        Key lines:
            self.tx.receive_AuD.emit(self.AuD)
        """
        self.tx.receive_AuD.emit(self.AuD)

    @Slot(float)
    def set_Hz(self, Hz):
        """
        @Slot(float)
        set_Hz(self, Hz)
        Set the Hz value to the calculator.
        Update the isotropic power.

        Parameters:
            Hz: float
            The value of Hz from the calculator.

        Key lines:
            self.Hz = float(Hz)
            self.calculateisotropicpower()
            self.tx.receive_Hz.emit(self.Hz)
        """
        self.Hz = float(Hz)
        self.calculateisotropicpower()
        self.tx.receive_Hz.emit(self.Hz)

    @Slot(float)
    def set_mG(self, mG):
        """
        @Slot(float)
        set_mG(self, mG)
        Set the mG value to the calculator.
        Update the isotropic power.

        Parameters:
            mG: float
            The value of mG from the calculator.

        Key lines:
            self.mG = float(mG)
            self.calculateisotropicpower()
            self.tx.receive_mG.emit(self.mG)
        """
        self.mG = float(mG)
        self.calculateisotropicpower()
        self.tx.receive_mG.emit(self.mG)

    @Slot(float)
    def set_B(self, B):
        """
        @Slot(float)
        set_B(self, B)
        Set the B value to the calculator.
        Update the isotropic power.

        Parameters:
            B: float
            The value of B from the calculator.

        Key lines:
            self.B = float(B)
            self.calculateisotropicpower()
            self.tx.receive_B.emit(self.B)
        """
        self.B = float(B)
        self.calculateisotropicpower()
        self.tx.receive_B.emit(self.B)


    @Slot(float)
    def set_K(self, K):
        """
        @Slot(float)
        set_K(self, K)
        Set the K value to the calculator.
        Update the isotropic power.

        Parameters:
            K: float
            The value of K from the calculator.

        Key lines:
            self.K = float(K)
            self.calculateisotropicpower()
            self.tx.receive_K.emit(self.K)
        """
        self.K = float(K)
        self.calculateisotropicpower()
        self.tx.receive_K.emit(self.K)

    @Slot(float)
    def set_AuD(self, AuD):
        print("set_AuD")
        AuD /= 10**7
        print(AuD)
        """
        @Slot(float)
        set_AuD(self, AuD)
        Set the AuD value to the calculator.
        Update the isotropic power.

        Parameters:
            AuD: float
            The value of AuD from the calculator.

        Key lines:
            self.AuD = float(AuD)
            self.calculateisotropicpower()
            self.tx.receive_AuD.emit(self.AuD)
        """
        self.AuD = float(AuD)
        self.calculateisotropicpower()
        self.tx.receive_AuD.emit(self.AuD)

    def calculateisotropicpower(self, *args):
        """
        calculateisotropicpower(self, *args)
        Calculate the isotropic power.

        Key lines:
            self.isotropicpower = iW*2*10**6

        Returns:
            self.isotropicpower: float
            outdated return. not used in the current version of the code.
        """
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
    """
    main()
    Test the Calculator class.

    Local Variables:
        c: instance of class Calculator

    Key lines:
        c = Calculator()
        print(c.isotropicpower)

    idk why you'd want to run calculator.py as a standalone script, but here you go. :)
    """
    print(main.__doc__)
    c = Calculator(Sender())
    print(c.isotropicpower)


if __name__ == "__main__":
    main()

