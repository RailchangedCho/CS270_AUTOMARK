import quest as question
import ans as answer

def eval():
    q_result = question.getquestion()
    a_result = answer.getanswer()

    print("Q :" + str(q_result))
    print("A :" + str(a_result))

    AnsOrNot = []
    for i in range(10):
        if q_result[i] == a_result[i]:
            print("Problem " + str(i+1) + " correct")
            AnsOrNot.append(True)
        else:
            print("Problem " + str(i+1) + " incorrect")
            AnsOrNot.append(False)

    print(AnsOrNot)
    return AnsOrNot

eval()



