import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mcqdb = myclient["MCQProject"]
userCollection = mcqdb["userDetails"]
questionsCollection = mcqdb["programmingMCQQuestion"]
resultCollection = mcqdb["result"]

questionsTypeSet = {}
questionsTypeList = []

# contains list of all languages
languageList = []
languageSet = {}
# each language contents eg:
# languageContent={"java":{"variable","datatypes","operator"},"python":{"variable","datatypes","operator"}}
languageContent = {}
for data in questionsCollection.find():
    language = data["language"]
    languageList.append(language)
    languageSet = set(languageList)
    type = data["type"]
    questionsTypeList.append(type)
    questionsTypeSet = set(questionsTypeList)
    # questionsTypeSet = ("Programming", "cyber security", "Testing")
    for i in languageSet:
        content = []
        for j in questionsCollection.find({"language": i}):
            topic = j["topic"]
            content.append(topic)
        languageContent[i] = set(content)


def questionsList(topic, language):
    questions = []
    eachQuestion = {}
    print("topic", topic, "\nlanguage", language)
    for j in questionsCollection.find({'$and': [{"topic": topic}, {"language": language}]}):
        print("jjjjjjjjjjjjjjjjjjjjjjjjj", j)
        eachQuestion = {}
        eachQuestion["question"] = j["questions"]
        eachQuestion['option1'] = j['option1']
        eachQuestion['option2'] = j['option2']
        eachQuestion['option3'] = j['option3']
        eachQuestion['option4'] = j['option4']
        eachQuestion['answer'] = j['answer']
        eachQuestion['time'] = j['time']
        eachQuestion['mark'] = j['mark']
        questions.append(eachQuestion)
    return questions


# print(languageContent, "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
# languageSet = {"Python", "Java", "Html", "CSS", "C", "C++", "Javascript"}
# questionsTypeSet = {"Programming", "Testing", "Networking"}
# userCollection.insert_one({"name": "Abirami", "emailId": "abi@gmail.com",
#                           "dateOfBirth": "02.12.2004", "mobileNumber": 9874563214, "profileImage": "img.jpg"})
{"questions": "",
 "option1": "",
 "option2": "",
 "option3": "",
 "option4": "",
 "answer": "",
 "language": "Python",
 "type": "Programming",
 "topic": "Data types",
 "level": "beginner",
 "noOfPersonsAttended": 56684,
 "mark": 1,
 "time": 1}
pythonQuestions = [{"questions": "Which type of Programming does Python support?",
                    "option1": "object-oriented programming",
                    "option2": "structured programming",
                    "option3": "functional programming",
                    "option4": "all of the mentioned",
                    "answer": "all of the mentioned",
                    "language": "python",
                    "type": "Programming",
                    "topic": "Basic of Python",
                    "level": "beginner",
                    "noOfPersonsAttended": 56684,
                    "mark": 1,
                    "time": 1},
                   {"questions": "Is Python case sensitive when dealing with identifiers?",
                    "option1": "no",
                    "option2": "yes",
                    "option3": "machine dependent",
                    "option4": "none of the mentioned",
                    "answer": "yes",
                    "language": "python",
                    "type": "Programming",
                    "topic": "Basic of Python",
                    "level": "beginner",
                    "noOfPersonsAttended": 56684,
                    "mark": 1,
                    "time": 1},
                   {"questions": "Which of the following is the correct extension of the Python file?",
                    "option1": ".python",
                    "option2": ".pl",
                    "option3": ".py",
                    "option4": ".p",
                    "answer": ".py",
                    "language": "python",
                    "type": "Programming",
                    "topic": "Basic of Python",
                    "level": "beginner",
                    "noOfPersonsAttended": 56684,
                                "mark": 1,
                                "time": 1},
                   {"questions": "Is Python code compiled or interpreted?",
                    "option1": "Python code is both compiled and interpreted",
                    "option2": "Python code is neither compiled nor interpreted",
                    "option3": "Python code is only compiled",
                    "option4": "Python code is only interpreted",
                    "answer": "Python code is both compiled and interpreted",
                    "language": "python",
                    "type": "Programming",
                    "topic": "Basic of Python",
                    "level": "beginner",
                    "noOfPersonsAttended": 56684,
                    "mark": 1,
                    "time": 1},
                   {"questions": "All keywords in Python are in_________",
                    "option1": "Capitalized",
                    "option2": "lower case",
                    "option3": "UPPER CASE",
                    "option4": "None of the mentioned",
                    "answer": "None of the mentioned",
                    "language": "python",
                    "type": "Programming",
                    "topic": "Basic of Python",
                    "level": "beginner",
                    "noOfPersonsAttended": 56684,
                    "mark": 1,
                    "time": 1}]
javaQuestions = [{"questions": "Who invented Java Programming?",
                  "option1": "Guido van Rossum",
                 "option2": "James Gosling",
                  "option3": "Dennis Ritchie",
                  "option4": "Bjarne Stroustrup",
                  "answer": "James Gosling",
                  "language": "Java",
                  "type": "Programming",
                  "topic": "Basic of Java",
                  "level": "beginner",
                  "noOfPersonsAttended": 56684,
                  "mark": 1,
                  "time": 1},
                 {"questions": "Which statement is true about Java?",
                  "option1": "Java is a sequence-dependent programming language",
                 "option2": "Java is a code dependent programming language",
                  "option3": "Java is a platform-dependent programming language",
                  "option4": "Java is a platform-independent programming language",
                  "answer": "Java is a platform-independent programming language",
                  "language": "Java",
                  "type": "Programming",
                  "topic": "Basic of Java",
                  "level": "beginner",
                  "noOfPersonsAttended": 56684,
                  "mark": 1,
                  "time": 1},
                 {"questions": "Which component is used to compile, debug and execute the java programs?",
                  "option1": "JRE",
                 "option2": "JIT",
                  "option3": "JDK",
                  "option4": "JVM",
                  "answer": "JDK",
                  "language": "Java",
                  "type": "Programming",
                  "topic": "Basic of Java",
                  "level": "beginner",
                  "noOfPersonsAttended": 56684,
                  "mark": 1,
                  "time": 1},
                 {"questions": "Which one of the following is not a Java feature?",
                  "option1": "Object-oriented",
                 "option2": "Use of pointers",
                  "option3": "Portable",
                  "option4": "Dynamic and Extensible",
                  "answer": "Use of pointers",
                  "language": "Java",
                  "type": "Programming",
                  "topic": "Basic of Java",
                  "level": "beginner",
                  "noOfPersonsAttended": 56684,
                  "mark": 1,
                  "time": 1},
                 {"questions": "Which of these cannot be used for a variable name in Java?",
                  "option1": "identifier & keyword",
                 "option2": "identifier",
                  "option3": "keyword",
                  "option4": "none of the mentioned",
                  "answer": "keyword",
                  "language": "Java",
                  "type": "Programming",
                  "topic": "Basic of Java",
                  "level": "beginner",
                  "noOfPersonsAttended": 56684,
                  "mark": 1,
                  "time": 1}]
# Topic 2:
# Python variables
pythonQuestions = [{"questions": "Is Python case sensitive when dealing with identifiers?",
                    "option1": "yes",
                    "option2": "no",
                    "option3": "machine dependent",
                    "option4": "none of the mentioned",
                    "answer": "yes",
                    "language": "Python",
                    "type": "Programming",
                    "topic": "Python variables",
                    "level": "beginner",
                    "noOfPersonsAttended": 56684,
                    "mark": 1,
                    "time": 1},
                   {"questions": "What is the maximum possible length of an identifier?",
                    "option1": "31 characters",
                    "option2": "63 characters",
                    "option3": "79 characters",
                    "option4": "none of the mentioned",
                    "answer": "none of the mentioned",
                    "language": "Python",
                    "type": "Programming",
                    "topic": "",
                    "level": "beginner",
                    "noOfPersonsAttended": 56684,
                    "mark": 1,
                    "time": 1},
                   {"questions": "Which of the following is invalid?",
                    "option1": "_a = 1",
                    "option2": "__a = 1",
                    "option3": "__str__ = 1",
                    "option4": "none of the mentioned",
                    "answer": "none of the mentioned",
                    "language": "Python",
                    "type": "Programming",
                    "topic": "",
                    "level": "beginner",
                    "noOfPersonsAttended": 56684,
                    "mark": 1,
                    "time": 1},
                   {"questions": "Which of the following is an invalid variable?",
                    "option1": "my_string_1",
                    "option2": "1st_string",
                    "option3": "foo",
                    "option4": "_",
                    "answer": "1st_string",
                    "language": "Python",
                    "type": "Programming",
                    "topic": "",
                    "level": "beginner",
                    "noOfPersonsAttended": 56684,
                    "mark": 1,
                    "time": 1},
                   {"questions": "Why are local variable names beginning with an underscore discouraged?",
                    "option1": "they are used to indicate a private variables of a class",
                    "option2": "they confuse the interpreter",
                    "option3": "they are used to indicate global variables",
                    "option4": "they slow down execution",
                    "answer": "they are used to indicate a private variables of a class",
                    "language": "Python",
                    "type": "Programming",
                    "topic": "",
                    "level": "beginner",
                    "noOfPersonsAttended": 56684,
                    "mark": 1,
                    "time": 1}]
# data types
pythonQuestions = [{"questions": "Which of these in not a core data type?",
                    "option1": "Lists",
                    "option2": "Dictionary",
                    "option3": "Tuples",
                    "option4": "Class",
                    "answer": "Class",
                    "language": "Python",
                    "type": "Programming",
                    "topic": "Data types",
                    "level": "beginner",
                    "noOfPersonsAttended": 56684,
                    "mark": 1,
                    "time": 1}, {"questions": "Which of the following will run without errors?",
                                 "option1": "round(45.8)",
                                 "option2": "round(6352.898,2,5)",
                                 "option3": "round()",
                                 "option4": "round(7463.123,2,1)",
                                 "answer": "round(45.8)",
                                 "language": "Python",
                                 "type": "Programming",
                                 "topic": "Data types",
                                 "level": "beginner",
                                 "noOfPersonsAttended": 56684,
                                 "mark": 1,
                                 "time": 1}, {"questions": "What is the return type of function id?",
                                              "option1": "int",
                                              "option2": "float",
                                              "option3": "bool",
                                              "option4": "dict",
                                              "answer": "int",
                                              "language": "Python",
                                              "type": "Programming",
                                              "topic": "Data types",
                                              "level": "beginner",
                                              "noOfPersonsAttended": 56684,
                                              "mark": 1,
                                              "time": 1},
                   {"questions": "What data type is the object? L = [1, 23, 'hello', 1]",
                    "option1": "list",
                    "option2": "dictionary",
                    "option3": "array",
                    "option4": "tuple",
                    "answer": "list",
                    "language": "Python",
                    "type": "Programming",
                    "topic": "Data types",
                    "level": "beginner",
                    "noOfPersonsAttended": 56684,
                    "mark": 1,
                    "time": 1},
                   {"questions": "In order to store values in terms of key and value we use what core data type.",
                    "option1": "list",
                    "option2": "tuple",
                    "option3": "class",
                    "option4": "dictionary",
                    "answer": "dictionary",
                    "language": "Python",
                    "type": "Programming",
                    "topic": "Data types",
                    "level": "beginner",
                    "noOfPersonsAttended": 56684,
                    "mark": 1,
                    "time": 1},
                   ]
# operators
# if else
# questionsCollection.insert_many(pythonQuestions)
