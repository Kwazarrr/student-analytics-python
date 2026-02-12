def load_students(filename):
    students = []

    with open(filename, "r") as f:
        lines = f.readlines()

    for line in lines[1:]:
        clean = line.strip()
        parts = clean.split(",")
        name = parts[0]
        group = parts[1]
        grade = int(parts[2])

        student = {
            "name" : name,
            "group": group,
            "grade": grade
        }

        students.append(student) 
    return  students


def count_students_by_group(students):
    count_by_group = {}

    for student in students:
        group = student["group"]
        if group not in count_by_group:
            count_by_group[group] = 1
        else:
            count_by_group[group] += 1 
    return count_by_group


def sum_grades_by_group(students):
    sum_grades = {}

    for student in students:
        group = student["group"]
        grade = student["grade"]
        if group not in sum_grades:
            sum_grades[group] = grade
        else:
            sum_grades[group] += grade 
    return sum_grades          


def avg_grade_of_groups(students):
    sums = sum_grades_by_group(students)
    counts = count_students_by_group(students)

    avgs = {}
    for group in sums:
        avgs[group] = sums[group] / counts[group]

    return avgs

students = load_students("students.csv")

print(count_students_by_group(students))
print(sum_grades_by_group(students))
print(avg_grade_of_groups(students))





