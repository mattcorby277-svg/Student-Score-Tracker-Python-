numberOfStudents= int(input("Enter number of students: "))


listOfScores= []
dictionary ={}

totalScore=0 
classAverage=0

count=0

while count < numberOfStudents:
    studentName = input("Enter student name: ")
    
    if studentName in dictionary:
        print("You have already entered this person")
        continue

    while True:
        try:
            score = int(input("Enter your score: "))    
            if score <0 or score >100:
                print("Score must be between 0 and 100")
                continue
            break
        except ValueError:
            print("Please enter a valid number")

    dictionary[studentName] = score
    listOfScores.append(score)
    totalScore += score

    failed = score <=50
    

    print(f"Name: {studentName}\nScore: {score}\nFailed: {failed}")
    count +=1

classAverage = totalScore/numberOfStudents
print(f"\nClass Average: {classAverage:.2f}")




    
    





            
            
                    


    






