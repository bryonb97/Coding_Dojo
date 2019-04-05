function nthLargest(arr,n){
    for(var i=0;i<arr.length;i++){
      var min = i;
      var swap = arr[0];
      for(var j=i+1; j<arr.length;j++){
        if(arr[min]>arr[j]){  
          min = j;
        }
      }
      swap = arr[i];
      arr[i] = arr[min];
      arr[min] = swap;
    }
    return arr[arr.length-n];
  ​
  }
  ​
  myArr = [54, 26, 93, 17, 77, 31, 44, 55, 20, 1, 3, 5, 6 , 4, 9, 12, 8];
  nthLargest(myArr, 3);