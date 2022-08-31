
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log("Received number" + msg.number);
        //maintain a list of ten numbers
        if (numbers_received.length >=9){
            numbers_received.shift()
        }            
        numbers_received.push(msg.number);
        numbers_string = '';
        var volts = 'V'
        var imagenames = ['EVtoH.png','PhotoVoltaics.png']
        var location = '/static/'
        for (var i = 0; i < numbers_received.length; i++){


            numbers_string =   '<var>' + numbers_received[i].toString() + '</var>'+volts;

 //<img src="/static/PhotoVoltaics.png" alt="Girl in a jacket" style="width:300px;height:300px;">
        }
        $('#log').html(numbers_string);
    });

});