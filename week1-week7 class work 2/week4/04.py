def average_grade(records):
    total_grade = sum(record[2] for record in records)
    return total_grade

students = (
    ('James', 20,85)
    ('Sumeety', 22,35)
    ('Modi', 20,35)

)

def main():
    average_grade = average_grade(students)
    print("Average grade:" ,average_grade)
    main()
