class Student:
    def __init__(self, name, number_of_scores):
        self.name = name
        self.test_scores = [0] * number_of_scores

    def _validate_position(self, position):
        if not 1 <= position <= len(self.test_scores):
            raise IndexError("Score position out of range.")

    def getName(self):
        return self.name

    def getScore(self, position):
        self._validate_position(position)
        return self.test_scores[position - 1]

    def setScore(self, position, value):
        self._validate_position(position)
        self.test_scores[position - 1] = value

    def getHighestScore(self):
        if not self.test_scores:
            return 0
        return max(self.test_scores)

    def getAverageScore(self):
        if not self.test_scores:
            return 0
        return sum(self.test_scores) / len(self.test_scores)

    def __str__(self):
        return (
            f"Name: {self.name}, Scores: {self.test_scores}, "
            f"Highest: {self.getHighestScore()}, Average: {self.getAverageScore():.2f}"
        )


def main():
    name = input("Enter student name: ")
    number_of_scores = int(input("Enter number of test scores: "))

    student = Student(name, number_of_scores)

    for i in range(1, number_of_scores + 1):
        score = float(input(f"Enter score {i}: "))
        student.setScore(i, score)

    print("\nStudent Details")
    print(student)


if __name__ == "__main__":
    main()
