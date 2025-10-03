#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PROGRAMMER: Ritik Kumar
# DATE CREATED: 10/03/2025

import argparse
import os

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments.
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    Returns:
     parse_args() - data structure that stores the command line arguments object  
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', 
                        choices=['resnet', 'alexnet', 'vgg'],
                        help='the CNN model architecture')
    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='text file that contains valid dognames')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.dir):
        print(f"Warning: Directory '{args.dir}' does not exist!")
    
    if not os.path.isfile(args.dogfile):
        print(f"Warning: Dog names file '{args.dogfile}' does not exist!")
    
    return args