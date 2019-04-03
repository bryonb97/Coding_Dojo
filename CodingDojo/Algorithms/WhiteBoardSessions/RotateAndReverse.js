function reverse(arr){
    var swap = arr[0];
    for(var i = arr.length - 1; i >= 0; i--){
      for(var j = i - 1; j >= 0; j--){
        swap = arr[i];
        arr[i] = arr[j];
        arr[j] = swap;
      }
    }
    return arr;
  }
  // console.log(reverse([1,2,3,4,5]));
  
  function rotate(arr, turns = 1){
    turns = turns % arr.length;
    while(turns != 0){
      var last = arr[arr.length - 1];
      for(var j = arr.length - 1; j >= 0; j--){
        arr[j] = arr[j - 1];
      }
      arr[0] = last;
      if(turns > 0){
        turns--;
      }else{
        turns++
      }
  
    }
    return arr;
  }
  console.log(rotate([1,2,3,4,5], 7));