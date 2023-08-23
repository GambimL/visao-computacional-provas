from imutils.perspective import four_point_transform
import imutils
import cv2
import numpy as np
import os 



def falar(comando):
    
    match comando:
        case 1:
            print("ola")
        case 2:
            print("sla")


falar(1)