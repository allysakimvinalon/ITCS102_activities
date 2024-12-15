#compute final grades

prelim = eval(input("Prelim Grade ---> "))
midterm = eval(input("Midterm Grade ---> "))
semis = eval(input("Semi-Finals Grade ---> "))
finals = eval(input("Finals Grade ---> "))
quiz = eval(input("Quiz Grade ---> "))
project = eval(input("Project Grade ---> "))

#Nested Condition 
if (prelim >= 65 and prelim <= 100) and (midterm >= 65 and midterm <= 100) and (semis >= 65 and semis <= 100) and (finals >= 65 and finals <= 100) and (quiz >= 65 and quiz <= 100) and (project >= 65 and project <= 100):
	FG = (prelim * 0.15) + (midterm * 0.15) + (semis * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.15)
	if FG >= 75 :
		print ("Congratulations, you passed the course/subject.")
	else :
		print("Sorry, you failed. Better luck next time.")
else : 
	print("The grade is invalid.")

