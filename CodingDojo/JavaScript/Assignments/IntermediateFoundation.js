// 1
//Implement a function sigma(num) that, given a number, returns the sum of all positive integers from 1 up to number
//(inclusive). Ex: sigma(3) = 6(or 1+2+3)

function Sigma(num){
    var sum = 0;
    var start = num;

    for(start; start > 0; start--){
        sum += start;
    }
    return sum;
}
Sigma(5); 

// 2
// Factorial
// Write a function factorial(num) that, given a
// number, returns the product (multiplication) of all
// positive integers from 1 up to number (inclusive).
// For example, factorial(3) = 6 (or 1 * 2 * 3);
// factorial(5) = 120 (or 1 * 2 * 3 * 4 * 5).

function factorial(num){
    var startNum = 1;
    var product = num;
    while(startNum !== num){
        product *= startNum;
        startNum++;
    }
    return product;
}
factorial(5);

// 3
// Fibonacci - Create a function to generate Fibonacci numbers.  In this famous mathematical sequence, each number is the sum of the previous two, starting with values 0 and 1.  Your function should accept one argument, an index into the sequence (where 0 corresponds to the initial value, 4 corresponds to the value four later, etc).  Examples: fibonacci(0) = 0 (given), fibonacci(1) = 1 (given), fibonacci(2) = 1 (fib(0)+fib(1), or 0+1), fibonacci(3) = 2 (fib(1) + fib(2)3, or 1+1), fibonacci(4) = 3 (1+2), fibonacci(5) = 5 (2+3), fibonacci(6) = 8 (3+5), fibonacci(7) = 13 (5+8).  Do this without using recursion first.  If you don't know what a recursion is yet, don't worry as we'll be introducing this concept in Part 2 of this assignment.

function fib(num){
    var arr = [0,1];
    while(arr.length <= num){
        arr.push(arr[arr.length - 1] + arr[arr.length - 2]);
    }
    return arr[arr.length - 1];
}
fib(6);

// 4
// Array: Second-to-Last: Return the second-to-last element of an array. Given [42, true, 4, "Liam", 7], return "Liam".  If array is too short, return null.

function secondToLast(arr){
    var last = arr.length - 2;
    for(var i = arr.length - 1; i > last; i--){
        if(arr.length < 2){
            return null;
        }
        else{
            return arr[last];
        }
    }
}
secondToLast([42, true, 4, "Liam", 7]);

// 5
// Array: Nth-to-Last: Return the element that is N-from-array's-end.  Given ([5,2,3,6,4,9,7],3), return 4.  If the array is too short, return null.

function nToLast(arr, num){
    var last = arr.length - num;
    for(var i = arr.length - 1; i > last; i--){
        if(arr.length < 2){
            return null;
        }
        else{
            return arr[last];
        }
    }
}
nToLast([5,2,3,6,4,9,7],3);

// 6 
// Array: Second-Largest: Return the second-largest element of an array. Given [42,1,4,3.14,7], return 7.  If the array is too short, return null.

function secondLargest(arr){
    var largest = 0;
    var secondLargest = 0;
    for(var i = 0; i < arr.length; i++){
    if(arr[i]>largest){
            secondLargest = largest;
            largest = arr[i];
        }
        else if(arr[i] > secondLargest && arr[i] != largest)
            secondLargest = arr[i];
    }
    return secondLargest;
}
secondLargest([42,1,4,3.14,7]);

// 7
// Double Trouble: Create a function that changes a given array to list each existing element twice, retaining original order.  Convert [4, "Ulysses", 42, false] to [4,4, "Ulysses", "Ulysses", 42, 42, false, false].

function doubleTrouble(arr){
    console.log(arr);
    for(var i = 0; i < arr.length; i+=2){
        arr.splice(i, 0, arr[i]);
        console.log(arr);
    }
    console.log(arr);
}
doubleTrouble([4, "Ulysses", 42, false]);
