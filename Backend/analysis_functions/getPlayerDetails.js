import fs from 'fs';


function getName(playerID){

  const playerIDStr = String(playerID)

    fs.readFile('../data/idtonamemap.json', 'utf8', (err, data) => {
      if (err) {
        console.error('Error reading JSON file:', err);
        return;
      }
    
      try {
        const jsonData = JSON.parse(data);

        // Process the JSON data
        const name = jsonData[playerIDStr][1];
        const team = jsonData[playerIDStr][3];
        return(name+"_"+team)
      } catch (err) {
        console.error('Error parsing JSON data:', err);
      }
    });
}


function getID(name){
      fs.readFile('../data/nametoidmap.json', 'utf8', (err, data) => {
      if (err) {
        console.error('Error reading JSON file:', err);
        return;
      }
    
      try {
        const jsonData = JSON.parse(data);
        // Process the JSON data
        const id = jsonData[name];
        console.log(id)
        return(id)
      } catch (err) {
        console.error('Error parsing JSON data:', err);
      }
    });
}

export {getName,getID}