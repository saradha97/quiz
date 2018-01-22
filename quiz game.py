students=[]
student2=[]
name1=[]
name2=[] 
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name,score])
maxi=min(students, key=lambda x: x[1])
maxx=maxi[1]
j=0
for i in students:
    if students[j][1]!=maxx:
        student2.append(students[j])        
    j=j+1
name1=min(student2, key=lambda x: x[1])
j=0
m=name1[1]
for i in student2:
    if student2[j][1] == m:
        print("sds")
        name2.append(student2[j][0])
        j=j+1
k=0
list.sort(name2)
for i in name2:
    print(name2[k])
    k=k+1
    
     


