
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.marks_set = {"first_sem": [5, 3, 4, 5, 4], "second_sem": [5, 2, 5, 4, 3]}

    def __str__(self):
        return "Students name is '%s %s'" % (self.surname, self.name)

    def average_mark_sem(self, sem):
        if sem == 1:
            var = "first_sem"
        else:
            var = "second_sem"
        try:
            return sum(self.marks_set[var]) / len(self.marks_set[var])
        except ZeroDivisionError:
            return "Marks mapping is empty"

    def average_anually(self):
        try:
            return \
            (sum(self.marks_set["first_sem"]) + sum(self.marks_set["second_sem"]))\
            / \
            (len(self.marks_set["first_sem"]) + len(self.marks_set["second_sem"]))
        except ZeroDivisionError:
            return "Marks mapping is empty"

    def best_sem(self):
        try:
            first_aver = sum(self.marks_set["first_sem"]) / len(self.marks_set["first_sem"])
            second_aver = sum(self.marks_set["second_sem"]) / len(self.marks_set["second_sem"])
            if second_aver > first_aver:
                return 2
            else:
                return 1
        except ZeroDivisionError:
            return "Marks mapping is empty"

stud = Student("Dima", "Dima")

print(stud)
print(stud.average_mark_sem(1))
print(stud.average_anually())
print(stud.best_sem())
