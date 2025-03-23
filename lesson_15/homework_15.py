class Rhombus:
    def __init__(self, side_a, angle_a=None, angle_b=None):
        self.side_a = side_a
        if angle_a is not None:
            self.angle_a = angle_a
        if angle_b is not None:
            self.angle_b = angle_b
        if angle_a is not None and angle_b is not None:
            if angle_a + angle_b != 180:
                raise ValueError("Cума кутів angle_a і angle_b повинна дорівнювати 180 градусам.")

    def __setattr__(self, name, value):
     if name == "side_a":
        if value <= 0:
            value = abs(value)
        elif name == "angle_a":
            if not (0<value<180):
                raise ValueError("Кут має бути в діапазоні від 0 до 180 градусів.")
            self.__dict__["angle_b"] = 180 - value
        elif name == "angle_b":
            if not (0<value<180):
                raise ValueError("Кут має бути в діапазоні від 0 до 180 градусів.")
            self.__dict__["angle_a"] = 180 - value
        self.__dict__[name] = value