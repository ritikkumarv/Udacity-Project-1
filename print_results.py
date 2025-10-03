#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PROGRAMMER: Ritik Kumar
# DATE CREATED: 10/01/2025

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and incorrectly classified images.
    Parameters:
      results_dic - Dictionary with classification results
      results_stats_dic - Dictionary with results statistics
      model - CNN model architecture used (string)
      print_incorrect_dogs - True prints incorrectly classified dog images
      print_incorrect_breed - True prints incorrectly classified dog breeds
    Returns:
      None - simply printing results.
    """    
    print(f"\n\n*** Results Summary for CNN Model Architecture {model.upper()} ***")
    print(f"{'N Images':<20}: {results_stats_dic['n_images']:>3d}")
    print(f"{'N Dog Images':<20}: {results_stats_dic['n_dogs_img']:>3d}")
    print(f"{'N Not-Dog Images':<20}: {results_stats_dic['n_notdogs_img']:>3d}")
    
    print(" ")
    for key in results_stats_dic:
        if key.startswith("pct"):
            print(f"{key:<20}: {results_stats_dic[key]:>5.1f}")
    
    has_incorrect_classifications = (
        (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
        != results_stats_dic['n_images']
    )
    
    if print_incorrect_dogs and has_incorrect_classifications:
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key in results_dic:
            try:
                if len(results_dic[key]) >= 5:
                    classification_sum = sum(results_dic[key][3:])
                    if classification_sum == 1:
                        print(f"Real: {results_dic[key][0]:>26}   Classifier: {results_dic[key][1]:>30}")
            except (IndexError, TypeError) as e:
                print(f"Error processing '{key}': {e}")
    
    has_incorrect_breeds = (
        results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']
    )
    
    if print_incorrect_breed and has_incorrect_breeds:
        print("\nINCORRECT Dog Breed Assignment:")
        for key in results_dic:
            try:
                if len(results_dic[key]) >= 5:
                    if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                        print(f"Real: {results_dic[key][0]:>26}   Classifier: {results_dic[key][1]:>30}")
            except (IndexError, TypeError) as e:
                print(f"Error processing '{key}': {e}")