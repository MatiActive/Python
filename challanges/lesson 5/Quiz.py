import requests
import html

class Question:
    def __init__(self, category, questionStr, correctAnswerFlag, difficulty):
        self.category = category
        self.questionStr = questionStr
        self.correctAnswerFlag = correctAnswerFlag
        self.difficulty = difficulty

class Quiz:
    def __init__(self, numQuestion):
        self.apiUrl = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.numQuestion = numQuestion
        self.questionList = []
        self.LoadQuiz(numQuestion)
    def LoadQuiz(self, numQyestion):
        response = requests.get(self.apiUrl + str(numQyestion))
        if response.ok:
            #print(response.json())
            data  = response.json()
            results = data["results"]

            for i in results:
                category = i["category"]
                gestionType = i["type"]
                difficulty = i["difficulty"]
                questionStr = html.unescape(i["question"])
                correctAnswerFlag = i["correct_answer"].lower() in ['true', '1']
                #print(questionStr)

                qEvr = Question(category, questionStr, correctAnswerFlag, difficulty)
                self.questionList.append(qEvr)

    def startQuiz(self):
        print("\n Welcom \n Start Quiz \n ")
        correctAnswers = 0 
        n = 0 
        numQuestion = len(self.questionList)

        while (n < numQuestion):
            q = self.questionList[n]
            print("Quest category : ", q.category)
            print("Quest Level " + q.difficulty)
            print("Quest number " + str(n+1) + ":", q.questionStr)
            #print("answer : ",q.correctAnswerFlag)
            answer = input("Podaj odpowiedz: ")
            
            answerBool = False
            if answer == "y": answerBool = True
            
            if answerBool == q.correctAnswerFlag:
                print("correct")
                correctAnswers += 1
            else:
                print("incorrect")
            n+=1

        print("Poprawne odpowiedzi", correctAnswers, " z ", len(self.questionList) )

quiz = Quiz(2)
quiz.startQuiz()