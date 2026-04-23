class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        points = self.scores[index]

        if points >= 90:
            return "A"
        elif points >= 80:
            return "B"
        elif points >= 70:
            return "C"
        elif points >= 60:
            return "D"
        elif points >= 50:
            return "E"
        else:
            return "F"


    def find(self ,score):
        scores = self.scores
        indexes = []
        i= 0

        for i, x in enumerate(scores, start=0):
            if x == score:
                indexes.append(i)
                i += 1
        return indexes



    def get_sorted(self):
        scores = self.scores.copy()

        m = len(scores)

        for cislo_pruchodu in range(m):
            for j in range(0, m - cislo_pruchodu - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]

        return scores


def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print("Studenti:", results.count())

    for i in range(results.count()):
        print(f"Student {i}: {results.get_by_index(i)} points - {results.get_grade(i)}")

    print("plny pocet bodu", results.find(100))
    print("Serazseno:", results.get_sorted())
    print("Puvodni:", results.scores)

if __name__ == "__main__":
    main()