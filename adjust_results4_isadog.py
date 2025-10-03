#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PROGRAMMER: Ritik Kumar
# DATE CREATED: 10/03/2025

from os import path

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images as a dog or not a dog.
    Parameters:
      results_dic - Dictionary with image results
      dogfile - Text file containing valid dog names
    Returns:
      None - results_dic is mutable data type so no return needed.
    """
    if not path.isfile(dogfile):
        print(f"Error: Dog names file '{dogfile}' does not exist!")
        return
    
    dognames_set = set()
    
    try:
        with open(dogfile, "r") as infile:
            for line in infile:
                line = line.strip()
                if line:
                    if line not in dognames_set:
                        dognames_set.add(line)
                    else:
                        print("**Warning: Duplicate dognames", line)
    except IOError as e:
        print(f"Error reading dogfile '{dogfile}': {e}")
        return
    
    for key in results_dic:
        if results_dic[key][0] in dognames_set:
            if results_dic[key][1] in dognames_set:
                results_dic[key].extend((1, 1))
            else:
                results_dic[key].extend((1, 0))
        else:
            if results_dic[key][1] in dognames_set:
                results_dic[key].extend((0, 1))
            else:
                results_dic[key].extend((0, 0))