import os

def questionParse(filename,questionindex):
    print("\n"+filename+"================\n")
    answersBegin = '<ol type="a">'

    questionText = "" 
    question = "" 
    answers = "" 

    questionFile = open(filename, "r")
    questionText = questionFile.read()
    
    question = questionText[0:questionText.find(answersBegin)].strip()
    answers = questionText[questionText.find(answersBegin):len(questionText)]

    answerList = []

    for x in range(0,4):
        li = '<li>'
        endli = '</li>'
        answerList.append(answers[answers.find(li)+(len(li)):answers.find(endli)])
        answers = answers[answers.find(endli)+(len(li)):len(answers)]
    
    print(question+"\n")
    print(answerList) 

    questionFile.close()


    with open("seeds.rb", "a") as myfile:

####write the question
      thisQ = """
question"""+str(questionindex)+"""text = %q{
"""+question+"""
}

question"""+str(questionindex)+""" = Question.create(
    question_title: "question"""+str(questionindex)+"""",
    question: question"""+str(questionindex)+"""text,
    has_mathjax: true
)
"""
      myfile.write(thisQ)

      answerindex = 0
###write the answers
      for x in range(0,len(answerList)):
            
          answer = """
answer"""+str(questionindex)+str(answerindex)+""" = Answer.create(
  answer: %q{"""+answerList[x]+"""},
  has_mathjax: true
)

QuestionAnswer.create(
    correct_answer: false,
    answer_id: answer"""+str(questionindex)+str(answerindex)+""".id,
    question_id: question"""+str(questionindex)+""".id
)
"""
          answerindex+=1
          myfile.write(answer)

      quizjoin = """
QuizQuestion.create(
    order_index: """+str(questionindex)+""",
    quiz_id: midterm.id,
    question_id: question"""+str(questionindex)+""".id
)
"""
      myfile.write(quizjoin)

    

def main():
    subfolder = "./2804_F18M"
    questions = os.listdir(subfolder)
    questionindex = 0

    for x in range(0, len(questions)):
      questionParse("2804_F18M/"+questions[x],questionindex)
      questionindex+=1

if __name__== "__main__":
  main()