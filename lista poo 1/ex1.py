class circulo:
    def _init_(self):
        self.raio = 0

    def calc_area(self):
        return 3.14 * self.raio**2

    def calc_circ(self):
        return (2 * 3.14) * self.raio

x = circulo()
x.raio = float(input())
print(f'{x.calc_area():.1f}')
print(f'{x.calc_circ():.1f}')
