// 1
// print1To255()Print all the integers from 1 to 255.

function Print1To255(){
  for(var i = 1; i <= 255; i++){
    console.log(i);
  }
}
Print1To255();

// 2
// printIntsAndSum0To255()Print integers from 0 to 255, and with each integer print the sum so far.

function PrintIntsAndSum0To255(){
  let sum = 0;
  for(var i = 0; i <= 255; i++){
    sum += i;
    console.log(i, sum);
  }
}
PrintIntsAndSum0To255();

// 3
// printMaxOfArray(arr)Given an array, find and print its largest element

var arr = [1,2,3,4,5];

function PrintMaxOfArray(arr){
  let maxVal = arr[0];
  for(let i of arr){
    if(arr[i] > maxVal){
      maxVal = arr[i];
    }
  }
  console.log(maxVal);
  return maxVal;
}
 PrintMaxOfArray(arr);

// 4
// Return Odds Array 1-255 returnOddsArray1To255()Create an array with all the odd integers between 1 and 255 (inclusive).
var arr = [];
function returnOddsArray1To255(){
  for(var i = 1; i <= 255; i++){
    (i % 2 !== 0) ? arr.push(i): 0;
  }
  return arr;
}
returnOddsArray1To255();

// 4
// Return Array Count Greater than Y return ArrayCountGreaterThanY(arr, Y)Given an array and a value Y, count and print the number of array values greater than Y.
var arr = [1,2,3,4,5];
var count = 0;
function ArrayCountGreaterThanY(arr, Y){
  for(let i of arr){
    if(arr[i] > Y){
      count++;
      console.log(arr[i]);
    }
  }
  return count;
}
ArrayCountGreaterThanY(arr, 2);

// 5
// Print Max, Min, Average Array Values printMaxMinAverageArrayVals(arr)Given an array, print the max, min and average values for that array.
var arr = [1,2,3,4,5,6];
var max = arr[0];
var min = arr[0];
var sum = 0;
var avg = 0;
function printMaxMinAvgArrayVals(arr){
  for(let i of arr){
    if(arr[i] > max){
      max = arr[i];
    }
    if(arr[i] < min){
      min = arr[i];
    }
  sum += i;
  avg = sum / arr.length;
  }
  console.log(sum);
  console.log(max, min, avg);
}
printMaxMinAvgArrayVals(arr);

// Swap String for Array Negative Values swapStringForArrayNegativeVals(arr)Given an array of numbers, replace any negative values with the string 'Dojo'.

var arr = [-1,2,-3];
var replace = "Dojo";

function swapStringForArrayNegativeVals(arr){
  for(var i = 0; i < arr.length; i++){
    if(arr[i] < 0){
      arr[i] = replace;
    }
  }
  return arr;
}
swapStringForArrayNegativeVals(arr);

// 13
// shiftArrayValsLeft(arr)Given an array, move all values forward (to the left) by one index, dropping the first valueand leaving a 0(zero) value at the end of the array.

var arr = [1,2,3,4,5];

function shiftArrayValsLeft(arr){
  for(var i = 0; i < arr.length; i++){
    var temp = arr[0];
  }
  return arr;
}
shiftArrayValsLeft(arr);
var arr = [2,4,6,8,10,6,9]
for(let i of arr){
  console.log(i);
}