var hot = false
var temp = 44

if (temp>80) {
  console.log("hot outside");
}else if(temp<= 80 && temp >= 50){
  console.log("average temp outside");
}else {
  console.log("it is cold");
}

var ham = 10;
var cheese = 10;


var report = "blank";

if (ham >= 10 && cheese >= 10) {
  report = "strong sales"
}else if (ham === 0 && cheese === 0) {
  report = "Nothing sold"
}else {
  report = "sold something"
}

console.log(report);
