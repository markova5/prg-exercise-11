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

        for number in scores:
            if number == score:
                indexes.append(i)
                i += 1
        return indexes

    def get_sorted(self):
        scores = self.scores.copy()

        m = len(numbers)

        for cislo_pruchodu in range(m):
            for j in range(0, m - cislo_pruchodu - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        return numbers



def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.count())
    print(results.get_by_index(2))
    print(results.scores)
