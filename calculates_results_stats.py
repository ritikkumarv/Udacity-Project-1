#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PROGRAMMER: Ritik Kumar
# DATE CREATED: 10/03/2025

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run.
    Parameters:
      results_dic - Dictionary with classification results
    Returns:
      results_stats_dic - Dictionary containing results statistics
    """        
    results_stats_dic = dict()
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0       
    
    for key in results_dic:
        try:
            if len(results_dic[key]) < 5:
                print(f"Warning: Incomplete data for '{key}', skipping...")
                continue
                
            if results_dic[key][2] == 1:
                results_stats_dic['n_match'] += 1
            if sum(results_dic[key][2:]) == 3:
                results_stats_dic['n_correct_breed'] += 1
            if results_dic[key][3] == 1:
                results_stats_dic['n_dogs_img'] += 1
                if results_dic[key][4] == 1:
                    results_stats_dic['n_correct_dogs'] += 1
            else:
                if results_dic[key][4] == 0:
                    results_stats_dic['n_correct_notdogs'] += 1
        except (IndexError, TypeError) as e:
            print(f"Error processing results for '{key}': {e}")
            continue
    
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - 
                                          results_stats_dic['n_dogs_img']) 
    
    if results_stats_dic['n_images'] > 0:
        results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / 
                                          results_stats_dic['n_images']) * 100.0
    else:
        results_stats_dic['pct_match'] = 0.0
    
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / 
                                                 results_stats_dic['n_dogs_img']) * 100.0    
        results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / 
                                                  results_stats_dic['n_dogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0
        results_stats_dic['pct_correct_breed'] = 0.0
    
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                    results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0
    
    return results_stats_dic