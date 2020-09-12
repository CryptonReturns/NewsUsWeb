function scrape(){
    const {PythonShell} =require('python-shell'); 
  
    let options = { 
        mode: 'text', 
        pythonOptions: ['-u'],  
          scriptPath: './', 
        // args: ['something'] //An argument which can be accessed in the script using sys.argv[1] 
    }; 
      
  
    PythonShell.run('./scraper.py', options, function (err, result){ 
          if (err) throw err; 
          // result is an array consisting of messages collected  
          //during execution of script. 
          console.log('result: ', result.toString()); 
    }); 

}
module.exports = scrape;