    var mqtt = require('mqtt')  
    var fs = require('fs')  
    var broker = 'mqtt://test.mosquitto.org'  
    var client = mqtt.connect(broker)  
    var forecast = fs.readFileSync('../forecast.json').toString();  
      
    client.publish('mydevice/forecast', forecast)  
    client.end();  
      
    console.log('Successful!');  