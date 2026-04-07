def student_averages(students):
    result = {}

    for student, assignments in students.items():
        total = sum(assignments.values())
        count = len(assignments)
        average = round(total / count)
        result[student] = average

    return result


def assignment_averages(students):
    result = {}
    if not students:
        return {}

    for assignment in next(iter(students.values())).keys():
        total = 0
        count = 0

        for student in students:
            total += students[student][assignment]
            count += 1

        result[assignment] = round(total / count)

    return result