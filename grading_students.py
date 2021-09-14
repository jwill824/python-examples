import unittest

import math

# HackerLand University has the following grading policy:
# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.

# Sam is a professor at the university and likes to round each student's grade according to these rules:

# If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
# If the value of  is less than , no rounding occurs as the result will still be a failing grade.

# Examples:
# grade = 84 round to 85 (85 - 84 is less than 3)
# grade = 29 do not round (result is less than 40)
# grade = 57 do not round (60 - 57 is 3 or higher)

# Given the initial value of grade for each of Sam's  students, write code to automate the rounding process.

# Function Description
# Complete the function gradingStudents in the editor below.

# gradingStudents has the following parameter(s):
# int grades[n]: the grades before rounding

# Returns
# int[n]: the grades after rounding as appropriate

# Input Format
# The first line contains a single integer, n, the number of students.
# Each line i of the n subsequent lines contains a single integer, grades[i].

# Constraints
# 1 <= n <= 60
# 0 <= grades[i] <= 100

def gradingStudents(grades):
    rounded_grades = []
    
    for grade in grades:
        next_multiple = math.ceil(grade / 5) * 5
        if (next_multiple - grade) < 3 and grade >= 38:
            grade = next_multiple
        rounded_grades.append(grade)
            
    return rounded_grades

class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual([75, 67, 40, 33], gradingStudents([73, 67, 38, 33]))

if __name__ == '__main__':
    unittest.main()