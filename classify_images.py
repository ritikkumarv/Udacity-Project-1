#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PROGRAMMER: Ritik Kumar
# DATE CREATED: 10/03/2025

from classifier import classifier
from os import path

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds results to dictionary.
    Parameters: 
      images_dir - The (full) path to the folder of images
      results_dic - Results Dictionary
      model - CNN model architecture (resnet, alexnet, or vgg)
    Returns:
      None - results_dic is mutable data type so no return needed.         
    """
    for key in results_dic:
        try:
            image_path = path.join(images_dir, key)
            model_label = classifier(image_path, model)
            model_label = model_label.lower()
            model_label = model_label.strip()
            truth = results_dic[key][0]
            
            truth_words = set(truth.split())
            model_words = set(model_label.split())
            
            if truth_words.issubset(model_words) or truth in model_label:
                results_dic[key].extend([model_label, 1])
            else:
                results_dic[key].extend([model_label, 0])
        except Exception as e:
            print(f"Error classifying image '{key}': {e}")
            results_dic[key].extend(["error", 0])