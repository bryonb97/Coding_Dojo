// Given an array and a value Y, count and print the number of array values greater than Y.
var count = 0;

function greaterThanY(arr, Y){
  for(let i of arr){
    if(i > Y){
      count++;
    }
  }
  console.log(count);
  // return count;
}
greaterThanY([1,2,3,4,5], 2);

// Given an array, print the max, min and average values for that array.

var min = 99;
var max = 0;
var sum = 0;
var average;

function maxMinAvg(arr){
  for(let i of arr){
    if(i > max){
      max = i;
    }
    if(i < min){
      min = i;
    }

    sum += i;
    average = sum / arr.length;
  }
  console.log(max,min,average);
}
maxMinAvg([1,2,3,4,5]);

// Given an array of numbers, create a function that returns a new array where negative values were replaced with the string ‘Dojo’.   For example, replaceNegatives( [1,2,-3,-5,5]) should return [1,2, "Dojo", "Dojo", 5].
var replace = "Dojo";

function replaceNegatives(arr){
  for(let i of arr){
    if(arr[i] < 0){
      arr[i] = replace;
    }
  }
  return arr;
}
replaceNegatives([1,2-3,-5,5]);

// Given array, and indices start and end, remove values in that index range, working in-place (hence shortening the array).  For example, removeVals([20,30,40,50,60,70],2,4) should return [20,30,70].

function removeVals(arr, start, end){
  var startVal = start;
  var endVal = end;

  for(startVal; startVal <= endVal; startVal++){
    console.log(arr[startVal]);
    delete arr[startVal];
  }
  return arr;
}
removeVals([20,30,40,50,60,70],2,4);

