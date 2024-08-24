grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3],
          [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

a_grades =  [(sum(grades[0])/5),(sum(grades[1])/4),
             (sum(grades[2])/4),(sum(grades[3])/3),(sum(grades[4])/5)]

sort_students = sorted(students)
list_students = {sort_students[0]:a_grades[0],sort_students[1]:a_grades[1],
                 sort_students[2]:a_grades[2],sort_students[3]:a_grades[3],
                 sort_students[4]:a_grades[4]}
print(list_students)