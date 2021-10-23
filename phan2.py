
def getGrade(student):
	return student.grade

def sinhvien():
    print("Nhập n số sinh viên ")   
    n = int(input("nhập số n:"))
    list = []
    for i in range(n):
        list.append(STUDENT(i))
        print("MSSV:", i+1)
    count = i
    for student in list:
        if student.graduated() == True:
            count = count + 1
        else:
            return False
    print("Tổng số sinh viên đã tốt nghiệp: ")
    print(count + 1)

#Danh sách điểm trung bình sinh viên từ cao đến thấp-----------------------------------------------------
    list.sort(reverse=True, key=getGrade)

    print("Danh sách sinh viên đã sắp xếp")
    for student in list:
        print("id: %d, grade: %f, graduated: %b" % (student.id, student.grade, student.graduate()))
#Mã số sinh viên có điểm cao nhất------------------------------------------------------------------------
    print("Mã số sinh viên có điểm cao nhất:")
    print("id: %d, grade: %f, graduated: %b" % (list[0].id, student[0].grade, student[0].graduate()))

sinhvien()
   
  
