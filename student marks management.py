marks=[12,13,14,15,16]

marks.append(18)
marks.remove(12)

marks[0]=89

print("update marks list:",marks)
print("maximum marks list ",max(marks))
print("average marks list:",sum(marks)/len(marks))