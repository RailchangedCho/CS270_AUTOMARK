import quest as question
import ans as answer

q_result = question.getquestion()
a_result = answer.getanswer()

print(q_result)
print(a_result)

for i in range(10):
    if q_result[i] == a_result[i]:
        print("Problem " + str(i) + " correct")
    else:
        print("Problem " + str(i) + " incorrect")



