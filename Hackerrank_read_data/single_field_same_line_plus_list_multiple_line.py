# The first line contains a single integer denoting n (the number of students). 
# Each line i of the n subsequent lines contains a single integer, grade_i, denoting student i's grade.

# Sample input
4
73
67
38
33

n = int(input().strip())
grades = []
for grades_i in range(n):
   grades.append(int(input().strip()))