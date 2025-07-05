import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="manyadammire",
  database="project"
)
mycursor = mydb.cursor()
#print(mydb)

#/zahra_rostami

#view1

#view_query = "create view view1_p as select course.course_code,course.course_name,class.class_number,course.professor_coname,course.faculty from course,class where course.course_code = class.class_id"
#mycursor.execute(view_query)

#select_query = "select * from view1_p"
#mycursor.execute(select_query)

#result = mycursor.fetchall()

#for row in result:
#  print(row)

#view5

#view_query = "CREATE VIEW view5_p AS SELECT student.student_number,student.student_name FROM student,select_unit WHERE select_unit.passed_course < 12 AND student.student_number = select_unit.student_student_number"
#mycursor.execute(view_query)

#select_query = "SELECT * FROM view5_p"
#mycursor.execute(select_query)

#result = mycursor.fetchall()

#for row in result:
# print(row)

#trigger2

#trigger_query = """
#CREATE TRIGGER trigger2_p AFTER INSERT ON food_reservation FOR EACH ROW 
#BEGIN
#update student
#set financial_balance = financial_balance - ( select price from food,food_reservation
#     where (food.food_reservation_reserve_fid = food_reservation.reserve_fid) and new.food_reservation.reserved = '1' )
#     where student_number = new.food_reservation.student_student_number;
#END
#"""
#mycursor.execute(trigger_query)


#trigger ex1

#trigger_query = """
#CREATE TRIGGER ex1 AFTER UPDATE ON food_reservation FOR EACH ROW 
#BEGIN
#if new.eaten = 1 then
#update food_reservation
#set forgot = 0;
#End if ;
#END
#"""
#mycursor.execute(trigger_query)


#examination_schedule

#s_num = input("Enter your student number: ")

#select_query = f"SELECT examination_schedule.course_ename,examination_schedule.professor_ename,examination_schedule.exam_day,examination_schedule.exam_time,examination_schedule.exam_date,examination_schedule.class,examination_schedule.seat_number FROM examination_schedule where examination_schedule.student_student_number = '{s_num}'"
#mycursor.execute(select_query)

#result = mycursor.fetchall()

#for row in result:
#  print(row)

#reserve food

#table_name = "food_reservation"

#select_query = "SELECT food.food_id,food.food_name,food.price from food"
#mycursor.execute(select_query)

#result = mycursor.fetchall()

#for row in result:
#  print(row)

#req = input("Which food do you want? ")
#status = "yes"

#insert_query = f"UPDATE {table_name1} SET reserved = '{status}' WHERE food_reservation.reserve_fid = '{req}'"

#print("food: " + req + " reserved.")


# delete food

#print("reserved food")

#table_name2 = "food_reservation"

#select_query = "SELECT food.food_id,food.food_name from food,food_reservation where food_reservation.reserve_fid = food.food_id and food_reservation.reserved = 1 "
#mycursor.execute(select_query)

#result = mycursor.fetchall()

#for row in result:
#  print(row)

#req2 = input("Which food do you want to delete? ")
#status2 = "no"


#insert_query = f"UPDATE {table_name2} SET reserved = '{status}' WHERE food_reservation.reserve_fid = '{req2}'"

#print("food: " + req2 + " deleted.")


#extra1

#select_query = "SELECT student.student_name,student.student_number,student.address from student where student.address <> 'mshd'"
#mycursor.execute(select_query)

#result = mycursor.fetchall()

#for row in result:
#  print(row)

#extra2

#c_num = input("Enter your room number: ")

#select_query = f"SELECT examination_schedule.course_ename,examination_schedule.exam_day,examination_schedule.exam_time from examination_schedule where examination_schedule.class = '{c_num}' "
#mycursor.execute(select_query)

#result = mycursor.fetchall()

#for row in result:
#  print(row)


table_name1 = "student"
s_num = input("enter student number : ")

while True:
    edit = input("Which item do you want to edit? student_name, phone_number, address, Email, exit: ")

    if edit == "exit":
        break
    elif edit == "student_name":
        value = input("Enter student_name: ")
        select_query = f"UPDATE {table_name1} SET student_name = '{value}' WHERE student.student_number = {s_num}"
        print("successful")
    elif edit == "phone_number":
        value = input("Enter phone_number: ")
        select_query = f"UPDATE {table_name1} SET phone_number = '{value}' WHERE student.student_number = {s_num}"
        print("successful")
    elif edit == "address":
        value = input("Enter address: ")
        select_query = f"UPDATE {table_name1} SET address = '{value}' WHERE student.student_number = {s_num}"
        print("successful")
    elif edit == "Email":
        value = input("Enter Email: ")
        select_query = f"UPDATE {table_name1} SET Email = '{value}'WHERE student.student_number = {s_num}"
        print("successful")
    else:
        print("Input warning !!!")
        continue

    mycursor.execute(select_query)

    result = mycursor.fetchall()
    for row in result:
        print(row)



mydb.commit()

mycursor.close()
mydb.close()

