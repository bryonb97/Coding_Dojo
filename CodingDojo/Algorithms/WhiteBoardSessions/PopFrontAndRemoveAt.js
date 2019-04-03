function popFront(arr){
  var temp = arr[0];
  for(var i = 0; i < arr.length; i++){
    arr[i] = arr[i + 1];
  }
  arr.pop();
  console.log(arr);
  return temp;
}
popFront([0,5,2,3,4,6,5,4,1,4]);

function removeAt(arr, idx = 0){
  var val = arr[idx];
  while(arr[arr.length-1] != val){
    var temp = arr[idx];
    arr[idx] = arr[idx + 1];
    arr[idx + 1] = temp;
    idx++;
  }
  arr.pop();
  console.log(arr);
  return val;
}

function removeAt(arr, idx = 0){
  var val = arr[idx];
  for(var i = idx; i < arr.length; i++){
    arr[idx] = arr[idx + 1];
    idx++
  }
  // while(arr[arr.length-1] != val){
  //   var temp = arr[idx];
  //   arr[idx] = arr[idx + 1];
  //   arr[idx + 1] = temp;
  //   idx++;
  // }
  arr.pop();
  console.log(arr);
  return val;
}
removeAt([0,5,2,3,4,6,5,4,1,4]);