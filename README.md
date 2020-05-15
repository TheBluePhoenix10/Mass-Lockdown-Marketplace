# Mass Lockdown Marketplace
 It is the entire codebase for the Mass Lockdown Marketplace project on Hackster.io
The project has three independent nodes(raspberrypi or beaglebone black) based on debian OS

Node 1 : Packaging BOT 

Node 2 : Delivery BOT

Node 3 : Parking Station

When a user does a payment to the first node i.e Packaging bot by changing the QR code it looks for the services provided by nearby  autonomous delivery bots.
When an active delivery bot is found it commences the payment and assigns the delivery task to the end location. 
The delivery car then picks up the order and maps the delivery location.
It follows the route and delivers the product to the given location.
On successful delivery, it tries to find the nearest parking station.
When an empty parking slot is found at the parking station, it moves towards it and pays for the parking.
Once the payment is made the gate of the parking slot opens, allowing the delivery bot to park inside.
Once the delivery bot parks within the parking area, the gate closes.
This can be used as an autonomous cum contactless delivery system

To setup the nodes, follow the steps provided in the readme file present inside their corresponding folders. 
