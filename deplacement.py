from motor import Motor

class Move:
    def __init__(self, m1p1, m1p2, m2p1, m2p2, m3p1, m3p2, m4p1, m4p2):
        self.moteur1 = Motor(m1p1, m1p2)
        self.moteur2 = Motor(m2p1, m2p2)
        self.moteur3 = Motor(m3p1, m3p2)
        self.moteur4 = Motor(m4p1, m4p2)

        self.MoteurDir = {"av": ["avant", "avant", "avant", "avant"],
                          "ar": ["arriere", "arriere", "arriere", "arriere"],
                          "g": ["avant", "arriere", "arriere", "avant"],
                          "d": ["arriere", "avant", "avant", "arriere"],
                          "davd": ["libre", "avant", "avant", "libre"],
                          "davg": ["avant", "libre", "libre", "avant"],
                          "dard": ["arriere", "libre", "libre", "arriere"],
                          "darg": ["libre", "arriere", "arriere", "libre"],
                          "off": ["libre", "libre", "libre", "libre"],
                          "fh": ["avant", "arriere", "avant", "arriere"],
                          "fah": ["arriere", "avant", "arriere", "avant"],
                          "stop": ["stop", "stop", "stop", "stop"]}

    def msens(self, sens, moteur):
        if sens == "avant":
            moteur.pin1.value(1)
            moteur.pin2.value(0)
        elif sens == "arriere":
            moteur.pin1.value(0)
            moteur.pin2.value(1)
        elif sens == "libre":
            moteur.pin1(0)
            moteur.pin2(0)
        elif sens == "stop":
            moteur.pin1.value(1)
            moteur.pin2.value(1)

    def mov(self, dire):
        self.msens(self.MoteurDir[dire][0], self.moteur1)
        self.msens(self.MoteurDir[dire][1], self.moteur2)
        self.msens(self.MoteurDir[dire][2], self.moteur3)
        self.msens(self.MoteurDir[dire][3], self.moteur4)
