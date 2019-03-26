// Coins Generated
// Find the most efficient way to give change back for a given number.
const HUNDREDS = 100;
const FIFTIES = 50;
const TWENTIES = 20;
const TENS = 10;
const FIVES = 5;
const ONES = 1;
const QUARTERS = 0.25;
const DIMES = 0.10;
const NICKELS = 0.05;
const PENNIES = 0.01;

function giveChange(num){
  var hundreds = 0;
  var fifties = 0;
  var twenties = 0;
  var tens = 0;
  var fives = 0;
  var ones = 0;
  var quarters = 0;
  var dimes = 0;
  var nickels = 0;
  var pennies = 0;

  while(num !== 0){
    if(num % HUNDREDS === 0){
      num -= HUNDREDS;
      hundreds++;
    }
    else if(num % FIFTIES === 0){
      num -= FIFTIES;
      fifties++;
    }
    else if(num % TWENTIES === 0){
      num -= TWENTIES;
      twenties++;
    }
    else if(num % TENS === 0){
      num -= TENS;
      tens++;
    }
    else if(num % FIVES === 0){
      num -= FIVES;
      fives++;
    }
    else if(num % ONES === 0){
      num -= ONES;
      ones++;
    }
    else if(num % QUARTERS === 0){
      num -= QUARTERS;
      quarters++;
    }
    else if(num % DIMES === 0){
      num -= DIMES;
      dimes++;
    }
    else if(num % NICKELS === 0){
      num -= NICKELS;
      nickels++;
    }else{
      num -= PENNIES;
      pennies++;
    }
  }
  console.log("Hundreds: " + hundreds);
  console.log("Fifties: " + fifties);
  console.log("Twenties: " + twenties);
  console.log("Tens: " + tens);
  console.log("Fives: " + fives);
  console.log("Ones: " + ones);
  console.log("Quarters: " + quarters);
  console.log("Dimes: " + dimes);
  console.log("Nickels: " + nickels);
  console.log("Pennies: " + pennies);
}
giveChange(127.88);