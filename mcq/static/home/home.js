var Menuoption = false;
const userProfile = document.querySelector(".MCQ-userProfile");
var t = JSON.parse(document.getElementById("t-data").textContent);
console.log(t);
function optionFunction() {
  console.log(window.s);
  element = document.querySelector(".MCQ-userProfile__options");
  if (!Menuoption) {
    element.style.display = "block";
    Menuoption = true;
  } else {
    element.style.display = "none";
    Menuoption = false;
  }
}

userProfile.addEventListener("click", optionFunction);
console.log(userProfile);

// question page
