from motor import Motor

class Move(object):
    def __init__(self, m1p1, m1p2, m2p1, m2p2, m3p1, m3p2, m4p1, m4p2):
        self.moteur1 = Motor(m1p1, m1p2)
        self.moteur2 = Motor(m2p1, m2p2)
        self.moteur3 = Motor(m3p1, m3p2)
        self.moteur4 = Motor(m4p1, m4p2)

        self.MoteurDir = {"av": ["avant", "avant", "avant", "avant"],
                          "ar": ["arriere", "arriere", "arriere", "arriere"],
                          "g": ["avant", "arriere", "arriere", "avant"],
                          "d": ["arriere", "avant", "avant", "arriere"],
                          "davd": ["stop", "avant", "avant", "stop"],
                          "davg": ["avant", "stop", "stop", "avant"],
                          "dard": ["arriere", "stop", "stop", "arriere"],
                          "darg": ["stop", "arriere", "arriere", "stop"],
                          "off": ["stop", "stop", "stop", "stop"],
                          "rotad": ["avant", "arriere", "avant", "arriere"],
                          "rotag": ["arriere", "avant", "arriere", "avant"],
                          "stop": ["stop", "stop", "stop", "stop"]}

    def msens(self, sens, moteur):
        if sens == "avant":
            moteur.pin1.value(1)
            moteur.pin2.value(0)
        elif sens == "arriere":
            moteur.pin1.value(0)
            moteur.pin2.value(1)
        elif sens == "stop":
            moteur.pin1.value(1)
            moteur.pin2.value(1)

    def mov(self, dire):
        self.msens(self.MoteurDir[dire][0], self.moteur1)
        self.msens(self.MoteurDir[dire][1], self.moteur2)
        self.msens(self.MoteurDir[dire][2], self.moteur3)
        self.msens(self.MoteurDir[dire][3], self.moteur4)
