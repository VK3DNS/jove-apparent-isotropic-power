from PySide6.QtCore import QObject, Signal, Slot
from calculator import Calculator, Sender

values = {
    'Hz': False,
    'mG': False,
    'B': False,
    'K': False,
    'AuD': False
}

class Communicate(QObject):
    set_Hz = Signal(int)
    set_mG = Signal(int)
    set_B = Signal(int)
    set_K = Signal(int)
    set_AuD = Signal(int)

    get_Hz = Signal()
    get_mG = Signal()
    get_B = Signal()
    get_K = Signal()
    get_AuD = Signal()
    get_values = Signal()


class Receive:
    """
    class Receive:
    Receive values from the calculator and store them in the values dictionary.
    PySide6 does not allow a return value from a slot, so seperate signals are used to send the values to the handler.

    Attributes:
        None

    Methods:
        receive_values(self, array_values)
        receive_Hz(self, Hz)
        receive_mG(self, mG)
        receive_B(self, B)
        receive_K(self, K)
        receive_AuD(self, AuD)
    """

    @Slot(list)
    def receive_values(self, array_values):
        """
        @Slot(list)
        receive_values(self, array_values)
        Receive the values from the calculator and store them in the values dictionary.

        Parameters:
            array_values: list
            The values from the calculator.

        Key lines:
            values[key] = value
        """
        for key, value in zip(values.keys(), array_values):
            values[key] = value

    @Slot(float)
    def receive_Hz(self, Hz):
        """
        @Slot(float)
        receive_Hz(self, Hz)
        Receive the value of Hz from the calculator and store it in the values dictionary.

        Parameters:
            Hz: float
            The value of Hz from the calculator.

        Key lines:
            values['Hz'] = Hz
        """
        values['Hz'] = Hz

    @Slot(float)
    def receive_mG(self, mG):
        """
        @Slot(float)
        receive_mG(self, mG)
        Receive the value of mG from the calculator and store it in the values dictionary.

        Parameters:
            mG: float
            The value of mG from the calculator.

        Key lines:
            values['mG'] = mG
        """
        values['mG'] = mG

    @Slot(float)
    def receive_B(self, B):
        """
        @Slot(float)
        receive_B(self, B)
        Receive the value of B from the calculator and store it in the values dictionary.

        Parameters:
            B: float
            The value of B from the calculator.

        Key lines:
            values['B'] = B
        """
        values['B'] = B

    @Slot(float)
    def receive_K(self, K):
        """
        @Slot(float)
        receive_K(self, K)
        Receive the value of K from the calculator and store it in the values dictionary.

        Parameters:
            K: float
            The value of K from the calculator.

        Key lines:
            values['K'] = K
        """
        values['K'] = K

    @Slot(float)
    def receive_AuD(self, AuD):
        """
        @Slot(float)
        receive_AuD(self, AuD)
        Receive the value of AuD from the calculator and store it in the values dictionary.

        Parameters:
            AuD: float
            The value of AuD from the calculator.

        Key lines:
            values['AuD'] = AuD
        """
        values['AuD'] = AuD

def run():
    """
    run()
    Package the calculator, sender, receiver, and communicator into a single function. Useful for ease of reading in the main function.

    Local Variables:
        communicate: instance of class Communicate
        rx: instance of class Receive
        tx: instance of class Sender
        calc: instance of class Calculator

    Returns:
        communicate: instance of class Communicate
        values: dictionary
        rx: instance of class Receive
        tx: instance of class Sender
        calc: instance of class Calculator
    """
    from calculator import Calculator, Sender


    communicate = Communicate()
    rx = Receive()
    tx = Sender()
    calc = Calculator(tx)

    communicate.set_Hz.connect(calc.set_Hz)
    communicate.set_mG.connect(calc.set_mG)
    communicate.set_B.connect(calc.set_B)
    communicate.set_K.connect(calc.set_K)
    communicate.set_AuD.connect(calc.set_AuD)

    communicate.get_Hz.connect(calc.get_Hz)
    communicate.get_mG.connect(calc.get_mG)
    communicate.get_B.connect(calc.get_B)
    communicate.get_K.connect(calc.get_K)
    communicate.get_AuD.connect(calc.get_AuD)

    tx.receive_values.connect(rx.receive_values)
    tx.receive_Hz.connect(rx.receive_Hz)
    tx.receive_mG.connect(rx.receive_mG)
    tx.receive_B.connect(rx.receive_B)
    tx.receive_K.connect(rx.receive_K)
    tx.receive_AuD.connect(rx.receive_AuD)

    communicate.get_values.connect(calc.values)
    communicate.get_values.emit()

    return communicate, values, rx, tx, calc

def main():
    """
    main()
    Used for testing.

    Local Variables:
        communicate: instance of class Communicate
        values: dictionary
        rx: instance of class Receive
        tx: instance of class Sender
        calc: instance of class Calculator

    Returns:
        None

    Key lines:
        communicate.get_values.emit()
        communicate.set_K.emit(1)
        print(f'K is {values["K"]}')
        print(calc.isotropicpower)
    """
    communicate, values, rx, tx, calc = run()
    communicate.get_values.emit()

    print(f'K is {values["K"]}')
    print(calc.isotropicpower, end="\n\n\n")

    communicate.set_K.emit(1)
    print(f'K is {values["K"]}')
    print(calc.isotropicpower)

    #print(f'apparent isotropic power transmitted over the 2MHz band is {calc.isotropicpower} Joules')


if __name__ == '__main__':
    print(Receive.receive_values.__doc__)
    main()
