universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(universities):
    students=[]
    tuition=[]
    for uni in universities:
        students.append(uni[1])
        tuition.append(uni[2])
    return students,tuition
def mean(data):
    return sum(data) / len(data)
def median(data):
    data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]
students, tuition=enrollment_stats(universities)
print("******************************")
print("Total students:", f"{sum(students):,}")
print("Total tuition: $", f"{sum(tuition):,}")
print()
print("Student mean:", f"{mean(students):,.2f}")
print("Student median:", f"{median(students):,}")
print()
print("Tuition mean: $", f"{mean(tuition):,.2f}")
print("Tuition median: $", f"{median(tuition):,}")
print("******************************")
