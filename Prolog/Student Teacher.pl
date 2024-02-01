teacher(Aruna, Maths).
teacher(Sundari, Science).
teacher(Saravanan, Networks).
teacher(Divya_Bharathi, English ).
student(Guna, Divya_Bharathi, 123).
student(Jack, Aruna, 163).
student(Joe, Aruna, 123).
student(Bala, Naveen, 193).

find_teacher(Teacher_Name,Subject):-
    teacher(Teacher_Name,Subject).
find_student(Student_Name,Teacher_Name,Code):-
    student(Student_Name,Teacher_Name,Code).
