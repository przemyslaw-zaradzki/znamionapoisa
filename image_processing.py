#import cv2 as cv2
#import numpy as np
#from os import environ
#import scipy.cluster as cluster
#import scipy.spatial as spatial
#from collections import defaultdict
#from statistics import mean
#import math
#import chess
##import chess.svg
#from svglib.svglib import svg2rlg
#from reportlab.graphics import renderPM
#import sys
#from os import listdir
#from os.path import isfile, join
from Model import transforms_array, get_prediction

def processing(path):
    class_names = [ 'choroba Bowena',
    'rak podstawnokomórkowy',
    'łagodne rogowacenie',
    'dermatofibroma',
    'czerniak',
    'znamię melanocytowe',
    'zmiana naczyniowa' ]
    #img, gray_blur = read_img("static\images\skinn.jpg")
    #tensor = transforms_array(img)
    tensor = transforms_array("static/images/skinn.jpg")
    prediction = get_prediction(tensor)
    print(class_names[int(prediction)])
    return class_names[int(prediction)]