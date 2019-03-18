//Setting and Swapping
//Set myNumber to 42. Set myName to your name.
//Now swap myNumber into myName & vice versa.

var myNumber = 42;
var myName = "Bryon Bauer"

myNumber = myName;
myName = myNumber;

// Print -52 to 1066
// Print integers from -52 to 1066 using a FOR loop

for(var i = -56; i < 1067; i++){
    //console.log()?
    console.log(i);
}

// Don’t Worry, Be Happy
// Create beCheerful(). Within it, console.log
// string "good morning!" Call it 98 times.

function beCheerful(){
    for(var i = 0; i < 98; i++){
        console.log("good morning!");
    }
}
beCheerful();

// Multiples of Three – but Not All
// Using FOR, print multiples of 3 from -300 to 0.
// Skip -3 and -6

function multiplesOfThree(){
    for(var i = -300; i <= 1; i++){
      if(i % 3 === 0 && i !== -3 && i !== -6){
        console.log(i);
      }
    }
  }
  multiplesOfThree();

  // Printing Integers with While
// Print integers from 2000 to 5280, using a WHILE

var count = 2000;
var max = 5280;

while(count <= max){
  console.log(count);
  count++;
}

// You Say It’s Your Birthday
// If 2 given numbers represent your birth month
// and day in either order, log "How did you
// know?", else log "Just another day...."

var birthdayStr = "09/15";

if(birthdayStr){
  console.log("How did you know?");
}
else{
  console.log("Just anoter day....");
}

//  Leap Year
// Write a function that determines whether a given
// year is a leap year. If a year is divisible by four,
// it is a leap year, unless it is divisible by 100.
// However, if it is divisible by 400, then it is.

function LeapYear(year){
    var isLeapYear = false;
  
    if(year % 4 == 0){
      isLeapYear = true;
    }
    else if(year % 100 == 0){
      isLeapYear = false;
    }
    else if(year % 400 == 0){
      isLeapYear = true;
    }
  
    return isLeapYear;
  }
  
  LeapYear(2000);

  // Print and Count
// Print all integer multiples of 5, from 512 to 4096.
// Afterward, also log how many there were.

var count = 0;

for(var i = 512; i <= 4096; i++){
  if(i % 5 == 0){
    console.log(i);
    count++;
  }
}
console.log(count);

// Multiples of Six
// Print multiples of 6 up to 60,000, using a WHILE.
// var start = 6;
// var max = 600;

// while(6 <= 600){
//   if(max % 6 == 0){
//     console.log(start);
//   }
//   start++;
// }

// Counting, the Dojo Way
// Print integers 1 to 100. If divisible by 5, print
// "Coding" instead. If by 10, also print " Dojo"

for(var i = 1; i <= 101; i++){
    console.log(i);
    if(i % 5 === 0){
      console.log("Coding");
  
      if(i % 10 === 0){
      console.log("dojo");
    }
    }
  }

// What Do You Know?
// Your function will be given an input parameter
// incoming. Please console.log this value.
var input = "";

function takesInput(input){
  console.log(input);
}

// Whoa, That Sucker’s Huge…
// Add odd integers from -300,000 to 300,000, and
// console.log the final sum. Is there a shortcut?
var finalSum = 0;

for(var i = -300000; i <= 300001; i++){
  if(i % 2 !== 0){
    finalSum += i;
  }
}
console.log(finalSum);

// Countdown by Fours
// Log positive numbers starting at 2016, counting
// down by fours (exclude 0), without a FOR loop.

for(var i = 2016; i >= 0; i--){
    if(i % 4 == 0){
      console.log(i);
    }
  }

// Flexible Countdown
// Based on earlier “Countdown by Fours”, given
// lowNum, highNum, mult, print multiples of mult
// from highNum down to lowNum, using a FOR.
// For (2,9,3), print 9 6 3 (on successive lines).
var lowNum = 2;
var mult = 3;

  for(var highNum = 9; highNum >= lowNum; highNum--){
    if(highNum % mult === 0){
      console.log(highNum);
    }
  }

  // The Final Countdown
// This is based on “Flexible Countdown”. The parameter names are not as helpful, but the problem is
// essentially identical; don’t be thrown off! Given 4 parameters (param1,param2,param3,param4),
// print the multiples of param1, starting at param2 and extending to param3. One exception: if a
// multiple is equal to param4, then skip (don’t print) it. Do this using a WHILE. Given (3,5,17,9), print
// 6,12,15 (which are all of the multiples of 3 between 5 and 17, and excluding the value 9).

var param1 = 3; //multiples of 3
var param2 = 5; //start here
var param3 = 17; //end here
var param4 = 9; //if mult equals this skip

while(param3 >= param2){
  if(param2 % param1 === 0){
    console.log(param2);
  }
  else if(param4 / param1 == param1){
      break;
    }
  param2++;
}

// Countdown
// Create a function that accepts a number as an input. Return a new array that counts down by one, from
// the number (as array’s ‘zeroth’ element) down to 0 (as the last element). How long is this array? 

function Countdown(num){
    var newArr = [num];
  
    for(var i = num - 1; i > 0; i--){
      newArr.push(i);
    }
    return newArr;
  }
  
  Countdown(5);

  // Print and Return
// Your function will receive an array with two numbers. Print the first value, and return the second. 

function PrintAndReturn(arr){
    console.log(arr[0]);
    return arr[1];
  }
  
  PrintAndReturn([1,2]);

// First Plus Length
// Given an array, return the sum of the first value in the array, plus the array’s length. What happens if
// the array’s first value is not a number, but a string (like "what?") or a boolean (like false). 

var arr = [1, 2 , 3, 4, 5];
var sum = arr[0] + arr.length;

console.log(sum);

// Values Greater than Second
// For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return how many values this is. 
var arr = [1,3,5,7,9,13];
var secondVal = arr[1];
var count = 0;

  for(var i = 0; i <= arr.length; i++){
    if(arr[i] > secondVal){
      count++;
    }
  }
  console.log(count);

  // Values Greater than Second, Generalized
// Write a function that accepts any array, and returns a new array with the array values that are greater
// than its 2nd value. Print how many values this is. What will you do if the array is only one element long?
var arr = [1, 2, 3, 4 ,6];

var newArr = [];
var secondVal = arr[1];
var count = 0;

function GreaterThanSecond(arr){
  for(var i = 0; i < arr.length; i++){
    if(arr[i] > secondVal){
      newArr.push(arr[i]);
      count++;
    }
    
  }
  console.log(count);
  return newArr;
}
GreaterThanSecond(arr);

// This Length, That Value
// Given two numbers, return array of length num1 with each value num2. Print "Jinx!" if they are same.

var num1 = 12;
var num2 = 15;
var arr = [];

while(arr.length < num1){
  arr.push(num2);
}

if(num1 == num2){
      console.log("Jinx!");
    }

console.log(arr);

// Fit the First Value
// Your function should accept an array. If value at [0] is greater than array’s length, print "Too big!";
// if value at [0] is less than array’s length, print "Too small!"; otherwise print "Just right!". 

function FitFirstValue(arr){
    if(arr[0] > arr.length){
      console.log("Too big!");
    }
    else{
      console.log("Just right!");
    }
  }
  
  FitFirstValue([9, 2, 4, 3, 5]);

  // Fahrenheit to Celsius
// Kelvin wants to convert between temperature scales. Create fahrenheitToCelsius(fDegrees)
// that accepts a number of degrees in Fahrenheit, and returns the equivalent temperature as expressed
// in Celsius degrees. For review, Fahrenheit = (9/5 * Celsius) + 32.

function fahrenheitToCelsius(fDegrees){
    var celsius = (5/9) * (fDegrees - 32);
    return celsius;
  }
  
  fahrenheitToCelsius(5);

  // Celsius to Fahrenheit
// Create celsiusToFahrenheit(cDegrees) that accepts number of degrees Celsius, and returns
// the equivalent temperature expressed in Fahrenheit degrees.
// (optional) Do Fahrenheit and Celsius values equate at a certain number? Scientific calculation can be
// complex, so for this challenge just try a series of Celsius integer values starting at 200, going downward
// (descending), checking whether it is equal to the corresponding Fahrenheit value. 

function celsiusToFahrenheit(cDegrees){
    var fahrenheit = (9/5 * cDegrees) + 32;
    return fahrenheit;
  }
  
  celsiusToFahrenheit(1);

  // Biggie Size
// Given an array, write a function that changes all
// positive numbers in the array to “big”. Example:
// makeItBig([-1,3,5,-5]) returns that same
// array, changed to [-1,"big","big",-5]. 

function makeItBig(arr){
    for(var i = 0; i < arr.length; i++){
      if(arr[i] > 0){
        arr[i] = "big";
      }
    }
    return arr;
  }
  
  makeItBig([-1,3,5,-5]);

  // Print Low, Return High
// Create a function that takes array of numbers.
// The function should print the lowest value in the
// array, and return the highest value in the array
var arr = [1,2,3,4,5];

var low = arr[0];
var high = arr[1];

function PrntLowRtrnHigh(arr){
 
  for(var i = 0; i < arr.length; i++){
    if(arr[i] < low){
      low = arr[i];
    }
    else{
      high = arr[i];
    }
  }
  console.log(low);
  return high;
}

PrntLowRtrnHigh(arr);

// Print One, Return Another
// Build a function that takes array of numbers. The
// function should print second-to-last value in the
// array, and return first odd value in the array.
var arr = [2, 2, 3, 4, 5, 7];
var secondToLast = arr[arr.length - 2];
var isFirstOdd = true;
var firstOdd = arr[0];

function PrntOneRtrnAnother(arr){
for(var i = 0; i < arr.length; i++){
  if(isFirstOdd && arr[i] % 2 !== 0){
    firstOdd = arr[i];
    isFirstOdd = false;
  }
}
  console.log(secondToLast);
  return firstOdd;
}

PrntOneRtrnAnother(arr);

// Double Vision
// Given array, create a function to return a new
// array where each value in the original has been
// doubled. Calling double([1,2,3]) should
// return [2,4,6] without changing original.
var arr = [1, 2, 3];
var doubledNum = 0;
var doubledArr = [];

function DoubleVision(arr){
  for(var i = 0; i < arr.length; i++){
    doubledNum = 2 * arr[i];
    doubledArr.push(doubledNum);
  }
  return doubledArr;
}

DoubleVision(arr);

// Count Positives
// Given array of numbers, create function to
// replace last value with number of positive values.
// Example, countPositives([-1,1,1,1])
// changes array to [-1,1,1,3] and returns it. 
var arr = [-1, 1, 1, 2];
var target = arr[0];
var sumOfTarget = 0;
var positive = 0;

function CountPositives(arr){
  for(var i = 0; i < arr.length; i++){
    if(arr[i] >= 1){
      target = arr[i];
      sumOfTarget += target;
    }
  }
  arr[arr.length - 1] = sumOfTarget;
  console.log(sumOfTarget);
  return arr;
}

CountPositives(arr);

// // Evens and Odds
// // Create a function that accepts an array. Every
// // time that array has three odd values in a row,
// // print "That’s odd!" Every time the array has
// // three evens in a row, print "Even more so!"
// var arr = [1,1,2];

// var isOdd = false;
// var isEven = false;

// function EvensAndOdds(arr){
//   for(var i = 0; i < arr.length; i++){
//     if(arr[i] % 2 !== 0){
//       isOdd = true;
//     }
//     else{
//       isEven = true;
//     }
//   }
//   if(isOdd){
//     console.log("That's odd!");
//   }
//   else{
//     console.log("Even more so!");
//   }

//   return arr;
// }
// EvensAndOdds(arr);



// Previous Lengths
// You are passed an array containing strings.
// Working within that same array, replace each
// string with a number – the length of the string at
// previous array index – and return the array

// Add Seven to Most
// Build function that accepts array. Return a new
// array with all values except first, adding 7 to
// each. Do not alter the original array.
var arr = [1,2,3,4,5];
var firstIndex = arr[0];

function SevenToMost(arr){
  for(var i = 0; i < arr.length; i++){
    if(arr[i] !== firstIndex){
      arr[i] += 7;
    }
  }
  return arr;
}

SevenToMost(arr);

  




