from imutils.perspective import four_point_transform
import imutils
import cv2
import numpy as np
import os 

string = 'gabarito_teste4[Ciências Humanas]'
print(string.find('['))
print(string.find(']'))
print(string[string.find('[')+1:string.find(']')])
