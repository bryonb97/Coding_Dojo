// Requiring fs module in which 
// writeFile function is defined. 
var fs = require('fs')

var users = [{username:"key", password:"value"}]

// Data which will write in a file. 
var json = JSON.stringify(users)

  
// Write data in 'Output.txt' . 
function write(){
        fs.writeFile('Users.json', json, 'utf8', callback)
}


// Read from 'Users.json'
function read(){
        readFile('Users.json', (err, data) => { 
                if (err) throw err; 
              
                console.log(data.toString()); 
            })
}

