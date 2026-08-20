marks=[]

while True:
        print("===/n student management system=====")
        print("1.insert marks")
        print("2.display marks")
        print("3.update marks")
        print("4.delete marks")
        print("5.exist")

        choice=int(input("enter your choice:"))

        if choice==1:
            mark=int(input("enter student marks:"))
            marks.append(mark)
            print("marks inserted successfully.")

        elif choice==2:
              if len(marks)==0:
                    print("no marks available.") 
              else:
                print("student marks:")
                for i in range(len(marks)):
                    print("student",i+1,":",marks[i])

        elif choice==3:
             student=int(input("enter student number to update:"))
             if i<=student<=len(marks):
                  new_marks=int(input("enter student marks:"))
                  marks[student-1]=new_marks
                  print("marks update successfully:")

             else:
                  print("invalid student number.")

        elif choice==4:
             student=int(input("enter student number to delete."))
             if i<=student<=len(marks):
                  marks.pop(student-1) 
                  print("marks deleted successfully.")
             else:
                  print("invalid student number.")

        elif choice==5:
             print("program ended.")
             break
        else:
             print("invalid choice.")          

                