


var fn = prompt("What is your name?")
var ln = prompt("What is your last name?")

var age = prompt("how old are you?")
var height = prompt("how tall are you?")
var pn = prompt("What is your pet name?")
alert("Thank you!")

var nameCond = null;
var ageCond = null;
var heightCond = null;
var petCond = null;




if (fn[0]===ln[0]) {
  nameCond= true;
}else {
  nameCond=false;
}

if (age > 20 && age < 30) {
  ageCond= true;
}else {
  ageCond=false;
}

if (height > 170) {
  heightCond= true;
}else {
  heightCond=false;
}

if (pn[pn.length-1]==="y") {
  petCond= true;
}else {
  petCond=false;
}



if (nameCond && ageCond && heightCond && petCond) {
  console.log("Welcome Spy")
}else {
  console.log("Yoo")
}
