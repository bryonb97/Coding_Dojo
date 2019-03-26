// 1
// Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.

function get1To255(){
    var arr = [];
    for(var i = 1; i <= 255; i++){
        arr.push(i);
    }
    return arr;
}
get1To255();

// 2
// Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.

function getEven1000(){
    var sum = 0;
    for(var i = 0; i <= 1000; i++){
        if(i % 2 == 0){
            sum += i;
        }
    }
    return sum;
}
getEven1000();

// 3
// Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).

function getOddSum5000(){
    var sum = 0;
    for(var i = 0; i <= 5000; i++){
        if(i % 2 !== 0){
            sum += i;
        }
    }
    return sum;
}
getOddSum5000();

// 4
// Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).

function sumArr(arr){
    var sum = 0;
    for(let i of arr){
        sum += i;
    }
    return sum;
}
sumArr([-5,2,5,12]);

// 5
// Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)

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
 PrintMaxOfArray([1,2,3,4,5]);

 // 6
 // Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)

function findAvg(arr){
    var leng = arr.length;
    var sum = 0;
    var avg = 0;
    for(let i of arr){
        sum += i;
        avg = sum / leng;
    }
    return avg;
}
findAvg([1,3,5,7,20]);

// 7
// Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.

function oddNums(){
    var arr = [];
    for(var i = 0; i <= 50; i++){
        if(i % 2 !== 0){
            arr.push(i);
        }
    }
    return arr;
}
oddNums();

// 8 
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

// 9
// Squares - Given an array with multiple values, write a function that replaces each value in the array with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])
 
function squareValue(x){
    for(let i of x){
        x[i] *= x[i] * 2;
    }
    return x;
 }
squareValue([1,5,10,-2]);

// 10
// Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])

function negatives(arr){
    var replace = 0;
    for(let i of arr){
        if(arr[i] < 0){
            arr[i] = replace;
        }
    }
    return arr;
}
negatives([1,5,10,-2]);

// 11
// Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])

function maxMinAvg(arr){
    var min = arr[0];
    var max = arr[0];
    var sum = 0;
    var average;
  for(let i of arr){
    if(i > max){
      max = arr[i];
    }
    if(i < min){
      min = arr[i];
    }

    sum += arr;
    average = sum / arr.length;
  }
  console.log(max,min,average);
}
maxMinAvg([1,2,3,4,5]);

// 12
// Swap Values - Write a function that will swap the first and last values of any given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).

function swapValues(arr){
    var temp = 0;

    temp = arr[0];
    arr[0] = arr[arr.length - 1];
    arr[arr.length - 1] = temp;

    return arr;
}
swapValues([1,5,10,-2]);

// 13
// Number to String - Write a function that takes an array of numbers and replaces any negative values within the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].

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