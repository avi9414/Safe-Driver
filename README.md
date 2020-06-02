Hello.
This driver safety app has two modules Distracted Driver and Pothole Detector from following sources with minor changes.
Pothole: https://github.com/anantSinghCross/pothole-detection-system-using-convolution-neural-networks
Distracted Driver : https://github.com/akshaybahadur21/Drowsiness_Detection


The remaining Part is about how we can implement Emergency Vehical Priority System.
There are two apps here:
1. The flask web app for EV drivers to provide coordinates of accident
2. User side python application (UI by Tkinter) so that driver can be alerted on various occasions.
This module uses Geofences to check if vehicles is in a fence of EV or not.

Also a file named Keys.py should be created at the very begining to store the Api keys.
