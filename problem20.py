marks = [[56,89,70,92,67,100],[60,70,100,45,70,76], [60,95,90,85,93,45],[55,80,56,45,51,76],[78,100,65,77,91,87], [45,78,65,50,45,87],[32,50,45,67,40,80]]
students = ["Pelin","Dominique","Valentin","Christine","John Paul"," Patrick","Kellen"]
subjects = ["Algorighms and Data Structures","Java","Web App Development","Databases", "Human Computer Interaction"," Information Retrieval"]
print("ALL LESSONS ARE:")
print(subjects)
print()
for i in range(len(marks)):
    s=marks[i]
    d=0
    for n in s:
        d=d+n
        average=(d*100)/600
    print(students[i],":",marks[i],'=',round(float(average,),2),"%")
    for n in range(len(s)):
        if s[n]<50:
            print(students[i],"you have failed in",subjects[n],"you have to repeat")
