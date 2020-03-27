// console.log("TEST")
window.onload = function date() {
    Date.prototype.getWeek = function() {
    var date = new Date(this.getTime());
    date.setHours(0, 0, 0, 0);
    // Thursday in current week decides the year.
    date.setDate(date.getDate() + 3 - (date.getDay() + 6) % 7);
    // January 4 is always in week 1.
    var week1 = new Date(date.getFullYear(), 0, 4);
    // Adjust to Thursday in week 1 and count number of weeks from date to week1.
    return 1 + Math.round(((date.getTime() - week1.getTime()) / 86400000
                          - 3 + (week1.getDay() + 6) % 7) / 7);
  }
  
  // Returns the four-digit year corresponding to the ISO week of the date.
  Date.prototype.getWeekYear = function() {
    var date = new Date(this.getTime());
    date.setDate(date.getDate() + 3 - (date.getDay() + 6) % 7);
    return date.getFullYear();
  }

n =  new Date();
y = n.getFullYear();
m = n.getMonth() + 1;
d = n.getDate();
w = n.getWeek();
// console.log(w)
// document.getElementById("date").innerHTML = d + "/" + m + "/" + y;

var curr = new Date; // get current date
var first = curr.getDate() - curr.getDay(); // First day is the day of the month - the day of the week
// console.log(first)
var last = first + 6; // last day is the first day + 6

var firstday = new Date(curr.setDate(first)).toUTCString().split('2020')[0];
var lastday = new Date(curr.setDate(last)).toUTCString().split('2020')[0];

x = document.getElementById("week").innerHTML = firstday + "-" + lastday
}

days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday" ]
// console.log(days)
for (var i = 0; i<days.length; i++) {
  
  var x = document.getElementById(days[i])
  // console.log(x)
  // console.log(x)
  var now = new Date; // get current date
  // console.log(toString(now.getFullYear))
  var day = now.getDate() - now.getDay(); 
  var y = day + i
  temp = new Date(now.setDate(y));
  y = temp.toUTCString().split('2020')[0]
  // console.log(y)
  x.innerHTML = y
  // console.log(firstday+i)
}
// console.log(x)