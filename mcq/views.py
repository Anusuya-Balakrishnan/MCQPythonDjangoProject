from django.shortcuts import render, HttpResponse, redirect
from . import databaseConnection
from bson.objectid import ObjectId
from django.http import JsonResponse
import json

# user name function

# function which return full name of user


def userNameFunction(id):
    user = databaseConnection.userCollection.find_one(
        {"_id": ObjectId(oid=id)})
    userName = user["firstName"]+" "+user["lastName"]
    return userName


# login page
def login(req):
    if(req.session.get("user") == None):
        if req.method == "POST":
            emailId = req.POST.get("emailId")
            isNewUser = False
            for eachPerson in databaseConnection.userCollection.find():
                if(eachPerson["emailId"] == emailId):
                    req.session["user"] = str(eachPerson["_id"])
                    return redirect('home')
                else:
                    isNewUser = True
        # if user mobile number is not present in the database, move to signup page
            if(isNewUser):
                return redirect('signup')

    else:
        return redirect('home')

    return render(req, "login.html", {"userProfile": 0, "exit":False})


# sign up page
def signup(req):
    if req.method == "POST":
        firstName = req.POST.get("firstName")
        lastName = req.POST.get("lastName")
        emailId = req.POST.get("emailId")
        dateOfBirth = req.POST.get("dob")
        mobileNumber = req.POST.get("mobileNumber")
        profileImage = req.POST.get("profileImage")
        newUser = {"firstName": firstName, "lastName": lastName, "emailId": emailId, "dateOfBirth": dateOfBirth,
                   "mobileNumber": mobileNumber, "profileImage": profileImage}
        # inserting new user into database
        data = databaseConnection.userCollection.insert_one(newUser)
        # print("new user inserted", data.inserted_id)
        if(bool(data.inserted_id)):
            req.session["user"] = str(data.inserted_id)
            return redirect('home')
    return render(req, "signup.html",  {"userProfile": 0,"exit":False},)

# home page


def home(req):
    if(req.session.get("user") == None):
        return redirect('login')
    # userNameFunction(req.session["user"])
    data = {
        "userName": userNameFunction(req.session["user"]),
        "userProfile": 1,
        "questionsType": databaseConnection.questionsTypeSet,
        "t": "ocean","exit":False
    }
    if(req.session.get("QuizCompleted") != None):
        del req.session["QuizCompleted"]
    return render(req, "home.html", data)


# logout
def logout(req):
    # print("LOGOUT", req.session.get("user"), "\n\n")
    if(req.session.get("user") != None):
        for key in list(req.session.keys()):
            # print(req.session[key])
            del req.session[key]

    return redirect('login')


def testList(req):
    if(req.session.get("user") == None):
        return redirect('login')
    return render(req, "testList.html", {"userName": userNameFunction(req.session["user"]),
                                         "userProfile": 1, "language": databaseConnection.languageSet})


SelectedLanguage = ""

#  MCQ'S Test content -->> datatypes, variables, basic of python

def testContent(req, lang):
    languageKeys = databaseConnection.languageContent.keys()
    content = []
    # print("languageKeys", languageKeys)
    for key in languageKeys:
        if(lang == key and databaseConnection.languageContent[key] != ""):
            content = databaseConnection.languageContent[key]
            global SelectedLanguage
            SelectedLanguage = key

    if(req.session.get("user") == None):
        return redirect('login')
    

    # get topic details of student already attended test
    current__user=req.session.get("user")
    findPerson__resultCollection=list(databaseConnection.resultCollection.find({"username":current__user}))
    
    # languageList contains list of language already attended 
    languageList=[]
    for eachResult in findPerson__resultCollection:
        languageList.append(eachResult.get("language"))
    
    languageList=list(set(languageList))
    print(languageList)
    # dictionary contains details about language and topics
    personAttendedTopic={}
    
    for eachLanguage in languageList:
        topics=[]
        for eachResult in findPerson__resultCollection:
            if(eachLanguage==eachResult.get("language")):
                topics.append(eachResult.get("topic"))
            
        personAttendedTopic[eachLanguage]=topics
    

    print("personAttendedTopic",personAttendedTopic.get(lang))
    req.session["language"] = lang.title()
    return render(req, "testContent.html", {"userName": userNameFunction(req.session["user"]),
                                            "userProfile": 1, "language": lang.title(),"exit":False, 
                                            "contentList": content,"attendedTopic":personAttendedTopic.get(lang)})


questionList = []


def testInstruction(req, cont, languageName):

    if(req.session.get("user") == None):
        return redirect('login')
    req.session["topic"] = cont.title()
    resultPersonId = databaseConnection.findPersonResultCollection(
        req.session.get("user"), req.session["language"], req.session["topic"])
    # print("returenValue", resultPersonId)
    # if(resultPersonId):
    #     return redirect('home')

    # function return list of questions based on language and topic
    questionList = databaseConnection.questionsList(cont, languageName)
    
    req.session["questionList"] = questionList
    sumTime = 0
    for eachQuestion in questionList:
        sumTime += int(eachQuestion["time"])
    # print(sumTime)
    # print(questionList, "questionList")

    return render(req, "testInstruction.html", {"userName": userNameFunction(req.session["user"]),
                                                "userProfile": 1, "topic": cont.title(),
                                                "questionList": questionList,
                                                # "currentQuestion": questionList[0],
                                                "noQuestions": len(questionList),
                                                "time": sumTime,"exit":False})


def questions(req, languageTopic, questionNo=0):
    if(req.session.get("user") == None):
        return redirect('login')

    return render(req, "questionPage.html", {"userName": userNameFunction(req.session["user"]),
                                             "userProfile": 1, "topic": languageTopic,"exit":True })
    #  "questionList": req.session.get("questionList"),
    #  "noOfQuestions": len(req.session.get("questionList"))
    # "questionList": questionList, 'noOfQuestions': len(questionList)

# another way to get data from result data


questionNo = 0


def questionsPagePart2(req, languageTopic):

    questionList = req.session.get("questionList")
    noOfQuestions = len(questionList)
    questions = {}
    questionNoList = []
    resultList = []
    if((req.session.get("QuizCompleted") == None)):
        if(req.session.get("user") == None):
            return redirect('login')
        if(req.session.get("currentQuestionNo") == None):
            req.session["currentQuestionNo"] = 0
            currentQuestionNo = 0
        else:
            req.session["currentQuestionNo"] = str(
                int(req.session.get("currentQuestionNo"))+1)
            currentQuestionNo = int(req.session["currentQuestionNo"])

        if(currentQuestionNo < noOfQuestions):
            addResultData(req)
            keys = questionList[currentQuestionNo].keys()
            questionNoList.append(currentQuestionNo)
            for key in keys:
                questions[key] = questionList[currentQuestionNo].get(key)
        else:
            addResultData(req)
            del req.session["currentQuestionNo"]
            return redirect('resultPage')

        resultValue = {"userName": userNameFunction(req.session["user"]),
                       "userProfile": 1, "noOfQuestions": noOfQuestions,
                       'currentQuestionNo': currentQuestionNo,
                       "nextQuestionNo": currentQuestionNo+1,
                       "currentQuestion": questions,
                       "questionNo": questionNoList[-1]+1,

                       "topic": languageTopic
                       }
    else:
        return redirect("home")

    return render(req, "questionPagePart2.html", resultValue)


def demo(req):
    return render(req, "resultPage.html", {"userName": userNameFunction(req.session["user"]),
                                           "userProfile": 1 })

def resultLogic(req):
    if req.method == 'POST' and req.is_ajax():
        print("HEllo")
        data_from_ajax = json.loads(req.body.decode('utf-8'))
        
        # Process the data (e.g., save to the database)
        # You can access the list: data_from_ajax['values']

        value= JsonResponse({'message': 'Data processed successfully'})
        print("result_____________________",data_from_ajax)

    # return JsonResponse({'message': 'Invalid request'}, status=400)
    return render(req,"resultPage.html", {"userName": userNameFunction(req.session["user"]),
                                           "userProfile": 1  ,"exit":False})

def result(req):
    if(req.session.get("user") == None):
        return redirect('login')
    if(req.session.get("resultData") != None):
        req.session["QuizCompleted"] = True
        resultData = req.session["resultData"]
        correctCount = 0
        wrongCount = 0
        skippedCount = 0
        totalQuestion = len(resultData)
        # print(resultData, "\nlength", len(resultData))
        for eachQuestion in resultData:
            if(eachQuestion["selectedOption"] == eachQuestion["correctAnswer"]):
                correctCount += 1
            elif(eachQuestion["selectedOption"] == None):
                skippedCount += 1
            elif(eachQuestion["selectedOption"] != eachQuestion["correctAnswer"]):
                wrongCount += 1
        percentage = int((correctCount/totalQuestion)*100)
        databaseConnection.insertResultData(req.session.get(
            "user"), resultData, req.session["topic"], req.session["language"], percentage)
    else:
        return redirect('home')
    # print(correctCount)

    del req.session["resultData"]
    return render(req, "resultPage.html", {"userName": userNameFunction(req.session["user"]),
                                           "userProfile": 1,
                                           "percentage": percentage,
                                           'correctCount': correctCount,
                                           "skippedCount": skippedCount,
                                           "wrongCount": wrongCount

                                           })


def addResultData(req):
    questionDict = {}
    if(req.method == "POST"):
        questionName = req.POST.get("currentQuestion")
        selectedOption = req.POST.get("option")
        correctAnswer = req.POST.get("correctAnswer")
        questionDict = {"questionName": questionName,
                        "selectedOption": selectedOption, "correctAnswer": correctAnswer}
        if(req.session.get("resultData") == None):
            resultList = []
            resultList.append(questionDict)
            req.session["resultData"] = resultList
        else:
            resultList = req.session.get("resultData")
            resultList.append(questionDict)
            req.session["resultData"] = resultList
        # print(req.session["resultData"])
