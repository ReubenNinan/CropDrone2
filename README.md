# CropDrone2
Had to restart the project :(

This project is dedicated to my senior design (ECEN 404) capstone  at Texas A&M University. Here my subsystem is to make a website that is connected to a database,
has a public domain, and can be connected via a drone's onboard computing system. The biggest goal here is to full stack a website, to build the front end and the back end. 
Currently,the database is a PostgreSQL engine running on AWS. My sponsor wanted the website to have a login screen then when each user goes to view their data it shows links
to certain dates. Once those dates are selected then there is a grid of pictures collected on that date and finally there is a .csv download link for the coordinates
downloaded during that data collection flight.

Once my subsystem is complete I then have to integrate it with the rest of the project. That means I have to help figure out how my teammate will run his plant detection and 
drone path planning algorithm on the database and help another teammate figure out how to transfer all the data (pictures and coordinates) from the drone's onboard TX2 board
to the database then be represented on my website.

In total, the project is a crop drone that will remotely take off, detect what crops are out of season and need to be sprayed. Once detenction is complete, it will then head
back to base, the user will fill the tank with pesticides while the drone is calculating the most efficient path to take to spray the plants and head back for energy purposes.
The drone is off limits to the project. The drone is already complete, we the students in this capstone are responsible for the computer science portion. How to gather, 
organize, and represent the data to the user.
