from django.shortcuts import render, HttpResponse, redirect
from . import databaseConnection
from bson.objectid import ObjectId

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
            mobileNumber = req.POST.get("mobilenumber")
            isNewUser = False
            for eachPerson in databaseConnection.userCollection.find():
                if(eachPerson["mobileNumber"] == mobileNumber):
                    req.session["user"] = str(eachPerson["_id"])
                    return redirect('home')
                else:
                    isNewUser = True
        # if user mobile number is not present in the database, move to signup page
            if(isNewUser):
                return redirect('signup')

    else:
        return redirect('home')

    return render(req, "login.html", {"userProfile": 0})


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
        print("new user inserted", data.inserted_id)
        if(bool(data.inserted_id)):
            req.session["user"] = str(data.inserted_id)
            return redirect('home')
    return render(req, "signup.html",  {"userProfile": 0})

# home page


def home(req):
    if(req.session.get("user") == None):
        return redirect('login')
    # userNameFunction(req.session["user"])
    data = {
        "userName": userNameFunction(req.session["user"]),
        "userProfile": 1,
        "questionsType": databaseConnection.questionsTypeSet,
        "t": "ocean"
    }
    return render(req, "home.html", data)


# logout
def logout(req):
    # print("LOGOUT", req.session.get("user"), "\n\n")
    if(req.session.get("user") != None):
        del req.session["user"]
        return redirect('login')
    return redirect('home')


def testList(req):
    if(req.session.get("user") == None):
        return redirect('login')
    return render(req, "testList.html", {"userName": userNameFunction(req.session["user"]),
                                         "userProfile": 1, "language": databaseConnection.languageSet})


SelectedLanguage = ""


def testContent(req, lang):
    languageKeys = databaseConnection.languageContent.keys()
    content = []
    print("languageKeys", languageKeys)
    for key in languageKeys:
        if(lang == key and databaseConnection.languageContent[key] != ""):
            content = databaseConnection.languageContent[key]
            global SelectedLanguage
            SelectedLanguage = key

    if(req.session.get("user") == None):
        return redirect('login')
    return render(req, "testContent.html", {"userName": userNameFunction(req.session["user"]),
                                            "userProfile": 1, "language": lang.title(), "contentList": content})


questionList = []


def testInstruction(req, cont, languageName):
    if(req.session.get("user") == None):
        return redirect('login')
    print("content=", cont, "\n")
    questionList = databaseConnection.questionsList(cont, languageName)
    req.session["questionList"] = questionList
    sumTime = 0
    for eachQuestion in questionList:
        sumTime += int(eachQuestion["time"])
    print(sumTime)
    print(questionList, "questionList")
    return render(req, "testInstruction.html", {"userName": userNameFunction(req.session["user"]),
                                                "userProfile": 1, "topic": cont.title(),
                                                "questionList": questionList,
                                                # "currentQuestion": questionList[0],
                                                "noQuestions": len(questionList),
                                                "time": sumTime})


def questions(req, questionNo=0):
    if(req.session.get("user") == None):
        return redirect('login')
    questionList = req.session.get("questionList")

    # count = len(questionList)
    # databaseConnection.resultCollection.insert_one()

    return render(req, "questionPage.html", {"userName": userNameFunction(req.session["user"]),
                                             "userProfile": 1, "questionList": req.session.get("questionList"),
                                             "noOfQuestions": len(req.session.get("questionList"))})
    # "questionList": questionList, 'noOfQuestions': len(questionList)


def result(req):
    if(req.session.get("user") == None):
        return redirect('login')

    return render(req, "resultPage.html", {"userName": userNameFunction(req.session["user"]), "userProfile": 1, })
