function pushFront(arr, val){
    arr.push(0);
    for(var i = arr.length - 2; i > 0; i--){
      arr[i + 1] = arr[i];
    }
    arr[0] = val;
    return arr;
  }
  // pushFront([1,2,3,4,5], 1);
  
  function insertAt(arr, idx, val){
    arr.push(0);
    for(var i = arr.length - 2; i >= idx; i--){
      arr[i + 1] = arr[i];
    }
    arr[idx] = val;
    return arr;
  }
  insertAt([1,2,3,4,5], 2, 5);