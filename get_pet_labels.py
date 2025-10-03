#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PROGRAMMER: Ritik Kumar
# DATE CREATED: 10/02/2025

from os import listdir, path

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames of the image files.
    Parameters:
     image_dir - The (full) path to the folder of images
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a List
                    containing pet image label (string)
    """
    if not path.isdir(image_dir):
        print(f"Error: Directory '{image_dir}' does not exist!")
        return {}
    
    try:
        in_files = listdir(image_dir)
    except OSError as e:
        print(f"Error reading directory '{image_dir}': {e}")
        return {}
    
    results_dic = dict()
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    
    for filename in in_files:
        if not filename.startswith('.') and filename.lower().endswith(valid_extensions):
            pet_label = ""
            low_pet_image = filename.lower()
            word_list_pet_image = low_pet_image.split("_")
            
            for word in word_list_pet_image:
                if word.isalpha():
                    pet_label += word + " "
            
            pet_label = pet_label.strip()
            
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
            else:
                print("** Warning: Duplicate files exist in directory:", 
                     filename)
    
    return results_dic