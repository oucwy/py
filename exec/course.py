# 夏秋学期：学时 1036 课程数： 34 老师数：29, 人均学时： 37.0
# 春季学期：学时 954 课程数：22 老师数：19, 人均学时： 50
# 老师数：45
# 总学时：1990
# 人均学时：44.2
# 课程数：56
# 人均课程数：1.2
# 讲师：7+4
# 副教授：12+9
# 教授：8+4
professor = 17
associate_professor = 28
lecturer = 31
faculty = professor+associate_professor+lecturer
print ("老师数：",professor+associate_professor+lecturer)
course_count = 56

a = [15,
18,
18,
4,
51,
15,
12,
12,
12,
24,
51,
51,
51,
48,
48,
24,
27,
27,
24,
24,
24,
51,
24,
27,
51,
51,
51,
27,
12,
12,
51,
24,
24,
51]
print ("夏秋学期：学时",sum(a), "课程数：",len(a), "老师数：29, 人均学时：",sum(a)/29)
b = [24,
12,
24,
48,
48,
30,
48,
24,
24,
48,
48,
48,
48,
48,
48,
48,
48,
48,
48,
48,
48,
48,
48]
print ("春季学期：学时",sum(b), "课程数：22","老师数：19, 人均学时：",sum(b)/19)
print ("人均课时：", (1036+954)/45)