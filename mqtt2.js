var mqtt = require('mqtt')  
var broker = 'mqtt://broker.mqttdashboard.com';  
var client = mqtt.connect(broker);  
  
client.subscribe('testtopic/1');  
client.handleMessage = function(packet, done) {  
   console.log(packet.payload.toString());  
   done();  
} 