#!/bin/bash
# -*- coding: utf-8 -*-
# PROGRAMMER: Ritik Kumar
# DATE CREATED: 10/03/2025
# PURPOSE: Runs all three models to test which provides the best solution

echo "========================================================"
echo "Running Pet Image Classifier - Batch Testing"
echo "Programmer: Ritik Kumar"
echo "Date: October 3, 2025"
echo "========================================================"
echo ""

# Test all three CNN architectures
echo "========================================================"
echo "Testing Model 1: ResNet"
echo "========================================================"
python3 check_images.py --arch resnet --dogfile dognames.txt > resnet_pet-images.txt
echo "✓ ResNet results saved to: resnet_pet-images.txt"
echo ""

echo "========================================================"
echo "Testing Model 2: AlexNet"
echo "========================================================"
python3 check_images.py --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt
echo "✓ AlexNet results saved to: alexnet_pet-images.txt"
echo ""

echo "========================================================"
echo "Testing Model 3: VGG"
echo "========================================================"
python3 check_images.py --arch vgg --dogfile dognames.txt > vgg_pet-images.txt
echo "✓ VGG results saved to: vgg_pet-images.txt"
echo ""

echo "========================================================"
echo "Batch Testing Complete!"
echo "========================================================"
echo ""
echo "Result files created:"
echo "  - resnet_pet-images.txt"
echo "  - alexnet_pet-images.txt"
echo "  - vgg_pet-images.txt"
echo ""
echo "To view results, use:"
echo "  cat resnet_pet-images.txt"
echo "  cat alexnet_pet-images.txt"
echo "  cat vgg_pet-images.txt"
echo ""
echo "========================================================"


