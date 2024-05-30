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
    @Slot(list)
    def receive_values(self, array_values):
        for key, value in zip(values.keys(), array_values):
            values[key] = value

    @Slot(float)
    def receive_Hz(self, Hz):
        values['Hz'] = Hz

    @Slot(float)
    def receive_mG(self, mG):
        values['mG'] = mG

    @Slot(float)
    def receive_B(self, B):
        values['B'] = B

    @Slot(float)
    def receive_K(self, K):
        values['K'] = K

    @Slot(float)
    def receive_AuD(self, AuD):
        values['AuD'] = AuD

def run():
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

    print(f'K is {values["K"]}')
    print(calc.isotropicpower, end="\n\n\n")

    communicate.set_K.emit(1)
    print(f'K is {values["K"]}')
    communicate.get_values.emit()
    print(calc.isotropicpower)

    #print(f'apparent isotropic power transmitted over the 2MHz band is {calc.isotropicpower} Joules')


if __name__ == '__main__':
    main()
