class Length():
    def __init__(self, measure):
        self.measure = measure

    def km_in_mile(self, x):
        return round(float(x) / 1.609, 2)

    def m_in_feet(self, x):
        return round(float(x) * 3.281, 2)

    def cm_in_inch(slef, x):
        return round(float(x) / 2.54, 2)


class Weight():
    def __init__(self, measure):
        self.measure = measure

    def kg_in_lb(self, x):
        return round(float(x) * 2.205, 2)

    def gm_in_oz(self, x):
        return round(float(x) / 2.205, 2)


class Volume():
    def __init__(self, measure):
        self.measure = measure

    def l_in_gal(self, x):
        return round(float(x) / 3.785, 2)


class Temperature():
    def __init__(self, measure):
        self.measure = measure

    def c_in_f(self, x):
        return round((float(x) * (9 / 5)) + 32, 1)

    def c_in_k(self, x):
        return round(float(x) + 273.15, 2)
