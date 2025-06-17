# -*- coding: utf-8 -*-
"""
author: Maier Christoph
date: 17.06.2025

This module is a selection of functions for the manipulation of generated
measurement data with an oscilloscope.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl5

def read_csv_1trace(filename, header_num):
    
    data = []
    time = []
    yval = []
            
    with open(filename, 'r') as file:
        for cnt in range(header_num):
            first_line = file.readline()
        for line in file:
            line = line.strip()
            data.append(line)
                
                

            
            
    print(data)
    print('\n')
    
                    

    #dev_type = header[0][1]

    
    for cnt in range(len(data)):
        time.append(data[cnt][0])
        yval.append(data[cnt][1])
                            
    return [time, yval]

