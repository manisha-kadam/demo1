var mqtt=require('mqtt');
var client=mqtt.createClient({
    clientId:"a",
    clean:false
}).subscribe("iot/temp",{qos:1},function(){
    alert("subscribe done");
    client.end();
});