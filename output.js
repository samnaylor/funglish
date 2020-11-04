var myFunctionOne = (theInput) => Math.round((theInput + 6) / 2);

var awesomeFunction = (theInput) => myFunctionOne(2);

var a = (theInput) => 2;

var b = (theInput) => 3;

console.log((a() + b()))

var b = (theInput) => 4;

console.log((a() + b()))