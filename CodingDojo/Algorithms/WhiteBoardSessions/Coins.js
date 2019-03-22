// Coins Generated
// Find the most efficient way to give change back for a given number.
const QUARTERS = 25;
const DIMES = 10;
const NICKELS = 5;
const PENNIES = 1;

function giveChange(num){
  var quarters = 0;
  var dimes = 0;
  var nickels = 0;
  var pennies = 0;

  while(num !== 0){
    if(num % QUARTERS === 0){
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
  console.log("Quarters: " + quarters);
  console.log("Dimes: " + dimes);
  console.log("Nickels: " + nickels);
  console.log("Pennies: " + pennies);
}
giveChange(100);