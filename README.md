# smartToll_hardware

<h1>Smart Toll</h1>
<p>This project showcases a simple inter-connectivity among a server, a mobile application and a hardware. The mobile application (android) majorly deals with user input and exchanges data with the server (PHP). The server in turn publishes data onto the mqtt channel. The hardware (raspberry pi 3) is connected to the same mqtt channel and depending on the message sent over the channel does specific operation.<p>

<h3>Proposed Working Principle:</h3>
<p>Consider a metro station with tollbooth. Commutators scan a QR Code on the tollbooth which unlocks the toll gate. The travel through the metro and once they reach the destination station, they scan the QR Code on the toll booth again to unlock the gate. The transaction not only gets recorded but the entire process requires no physical exchange of money. <p>
<ul>
  <li>A tollbooth consists a QR Code attached to it.</li>
  <li>The QR Code encodes the station and gate number of the tollbooth. This helps to note which tollbooth is the commutator using. The   information is sent to the server when the QR Code is scanned.</li>
  <li>Use the mobile application to scan the QR code on the tollbooth.</li>
  <li>Data associated with the tollbooth and user is spent over to the server.</li>
  <li>Server updates the database and spends message over MQTT Channel to open the connected toll gate.</li>
  <li>Simlarly the commutator can unlock the gate at the destination station.</li>
</ul>

<h3>Requirements:</h3>
<ol>
  <li>Raspberry Pi/Arduino - This handles the hardware part of the system. We have used Raspberry to avoid the trouble of setting up        ethernet for arduino.</li>
  <li>Ultrasonic Sensor (HC-SR04) - This will enable the auto closing of the gate after a commutator passes through the gate.</li>
  <li>Server</u> - This handles the centralized transaction and updation of user records. We have used XAMPP and coded our server with      PHP.</li>
  <li>Mobile Application - This handles the interaction with the user. The camera of the mobile scans the QR Code and use internet to     relay data to the server. We have used Android.</li>
  <li>MQTT Broker - (Message Queuing Telemetry Transport) In lucid terms it is just a channel where devices can <b>publish</b> or         <b>subscribe</b> to a <b>topic</b>. There are many free brokers available for testing!</li>
   <li>Database System - Store the user data for authentication, transaction and tour details. We have used MYSQL.</li>
  </ol>

<h3>Repositories:</h3>
<ul>
  <li><b>Android (Mobile Application)</b> - https://github.com/iamsandeepkhan/smartToll_app</li>
  <li><b>PHP (Server)</b> - https://github.com/iamsudiptasaha/smartToll_server</li>
  <li><b>Raspberry pi (Hardware)</b> - https://github.com/iamsudiptasaha/smartToll_hardware</li>
</ul>
    
 <h3>About this repository:</h3>

<p>This repository contains our Raspberry Pi functionalities to handle the server. We have used MQTT Protocol which communicates with the server to unlock the gates. The locking of the gates are managed by ultrasonic sensor that senses proximity of commutators.</p>

<p>Link to setting up HC-SR04 with Raspberry Pi  : https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi</p>
<p>Link to understanding MQTT with Raspberry Pi  : https://www.youtube.com/watch?v=Pb3FLznsdwI</p>

<h3>Miscellaneous informations : </h3>
<ul>
  <li><b>Please update the MQTT authentication details in the file!</b></li>
  <li>Data over MQTT Channel : JSON Encoded data. Contains two mandatory fields to determine successful server operation:
    <p>"station" : Station name or code</p>
    <p>"gate" : Gate code associated with the station.</p>
  </li>
  
</ul>


