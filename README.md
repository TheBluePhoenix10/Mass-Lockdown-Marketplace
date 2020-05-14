# Mass Lockdown Marketplace
 It is the entire codebase for the Mass Lockdown Marketplace project on Hackster.io
The project ha three independent nodes(raspberrypi or beaglebone black) based on debian OS

Node 1 : Packaging BOT 

Node 2 : Delivery BOT

Node 3 : Parking Station

When a user do a payment to the first node i.e Packaging bot by cnanning the Qr code it looks for the autonomous deleivery bot services nearby.
When a active delivery bot is found it commence the payment and assign the delivery task to the end location 
The delivery car then pick up the order and maps the delivery location
It follows the route and deliver the product to the given location.
Once on successfull delivery it start to find the nearest parking station
when a empty parking station is found it move to it and pay for the parking.
This can be used for autonomous contactless delivery sysytem

To setup the nodes follow the steps from the readme files present in the respective node folders
