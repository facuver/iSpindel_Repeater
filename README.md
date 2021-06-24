# iSpindel_Repe
An acces point for several iSpindels to connect and repeat to ubidots server, bases on an esp32 and micropython.

The ESP32 will create an access point called iSpindel_repeater with a default password : "test1234". And once configurated it will try to connect to an wifi network to be able to log the data to the web. Ubidots for now.
A server is creater so you can change the configuration and se the iSpindels status.
