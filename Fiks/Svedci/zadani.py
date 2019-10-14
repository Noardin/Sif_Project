class Zadani:
    def __init__(self, pocet_svedku, vztahy):
        self.pocet_svedku = pocet_svedku
        self. vztahy = vztahy

    def distribute(self):
        vuz1 = []
        vuz2 = []
        max_vztahu = 0
        for clovek, znamy in self.vztahy.items():
            if len(znamy) > max_vztahu:
                max_vztahu = len(znamy)

        for i in range(max_vztahu+1):
            for k, v in self.vztahy.items():
                if len(v) == i:
                    if len(v) == 0:
                        vuz1.append(k)