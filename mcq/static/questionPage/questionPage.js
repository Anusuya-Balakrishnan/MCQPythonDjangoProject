var questionList = JSON.parse(document.getElementById("name").textContent);
var questionNumber = document.querySelector(".questionNumber");
var currentQuestionNumber = 0;
var questionsContainer = document.getElementsByClassName(
  "question-page-content__questions"
)[0];
var optionContainer = document.querySelectorAll(
  ".question-page-content__options p"
);
var optionValue = document.querySelectorAll(
  ".question-page-content__options .option"
);
var correctAnswer = document.querySelector(".correctAnswer");
var submitButton = document.querySelector(".question-page-content__submit");
var resultDetails = [];
// console.log(questionList);
function questionRender(eachQuestion) {
  if (currentQuestionNumber < questionList.length) {
    questionsContainer.innerHTML = eachQuestion.question;

    questionNumber.innerHTML = currentQuestionNumber + 1;
    correctAnswer.value = eachQuestion.answer;
    for (let i = 0; i <= 3; i++) {
      optionContainer[i].innerHTML = eachQuestion[`option${i + 1}`];
      optionValue[i].value = eachQuestion[`option${i + 1}`];
      var value = eachQuestion[`option${i + 1}`];
    }
    var option = document.getElementsByName("option");
    for (let i = 0; i < option.length; i++) {
      option[i].checked = false;
    }
  } else {
    currentQuestionNumber = 0;
    resultDetails = [];
  }
  if (currentQuestionNumber < questionList.length - 1) {
    submitButton.innerHTML = "next";
  } else if (currentQuestionNumber == questionList.length - 1) {
    submitButton.innerHTML = "submit";
  }
  // document.getElementById("questionForm").reset();
}

// first rendering of question details list page

questionRender(questionList[currentQuestionNumber]);

// on click next button

submitButton.addEventListener("click", () => {
  var question = document.getElementsByClassName(
    "question-page-content__questions"
  )[0].innerHTML;

  var option = document.getElementsByName("option");
  for (let i = 0; i < option.length; i++) {
    if (option[i].checked) {
      var selectedOption = option[i].value;
    }
  }
  var correctAnswer = document.getElementsByClassName("correctAnswer")[0].value;

  // creating object for currect question ,selected option and answer

  currentQuestionDetails = {
    question: question,
    selectedOption: selectedOption,
    correctAnswer: correctAnswer,
  };
  resultDetails.push(currentQuestionDetails);
  console.log(resultDetails);
  currentQuestionNumber++;
  questionRender(questionList[currentQuestionNumber]);
});
