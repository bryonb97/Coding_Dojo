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

