class ClasseA:
    def __init__(self):
        self.A1 = 0
        self.A2 = 0.0

    def MA1(self):
        print("MA1")

    def MA2(self):
        print("MA2")

    def MA3(self):
        print("Alteração a classe A partir do clone")

    # Método solicitado no passo 37
    def getSoma(self, a, b):
        return a + b
