
//This sample extracts text from an image and returns the text in JSON-Format


// npm install microsoft-computer-vision
// npm install file-system

var fs = require('file-system');

const microsofComputerVision = require("microsoft-computer-vision");

var input_file  =  process.argv[2].toString().trim();

fs.readFile(input_file, (err, img_data) => {
  if (err) throw err;
  console.log('reading image successful, now analyzing...');

    microsofComputerVision.orcImage({
        "Ocp-Apim-Subscription-Key": "my_key_here",
        "request-origin":"westeurope",
        "content-type": "application/octet-stream",
        "body": img_data,
       // "language": "unk",
        "detect-orientation": true
    }).then((data)=>{
      console.log('\ncomplete info: \n');
      console.log(JSON.stringify(data));
      
    // etxract pure wording
    var long_text = '';
    for (j in data.regions)  {
        for ( i in data.regions[j].lines)  {
            for (m in data.regions[j].lines[i].words)   {
            long_text += (String(data.regions[j].lines[i].words[m].text) ) + ' ';
            }
            long_text += '\n'; // new line
        }
    }
    console.log('\npure text: \n');
    console.log (long_text);


    }).catch((err)=>{
      throw err;
    })

});


