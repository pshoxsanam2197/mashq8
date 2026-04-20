# 20-m
class Battery:
    def __init__(self,percent):
        self.percent = percent

    def status(self):
        if self.percent < 20:
            print("Quvvat kam")

        else:
            print("Yaxshi")


b1 = Battery(18)
b1.status()

b2 = Battery(34)
b2.status()
