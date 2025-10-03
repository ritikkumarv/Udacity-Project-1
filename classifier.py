#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PROGRAMMER: Ritik Kumar
# DATE CREATED: 10/03/2025

import ast
from PIL import Image
import os

try:
    import torchvision.transforms as transforms
    from torch.autograd import Variable
    import torchvision.models as models
    from torch import __version__
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    print("Warning: PyTorch/torchvision not installed. Please install with: pip install torch torchvision")

if TORCH_AVAILABLE:
    try:
        from torchvision.models import ResNet18_Weights, AlexNet_Weights, VGG16_Weights
        resnet18 = models.resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
        alexnet = models.alexnet(weights=AlexNet_Weights.IMAGENET1K_V1)
        vgg16 = models.vgg16(weights=VGG16_Weights.IMAGENET1K_V1)
    except (ImportError, AttributeError):
        resnet18 = models.resnet18(pretrained=True)
        alexnet = models.alexnet(pretrained=True)
        vgg16 = models.vgg16(pretrained=True)
    
    model_dict = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}
else:
    model_dict = {}

imagenet_classes_dict = {}
imagenet_file = 'imagenet1000_clsid_to_human.txt'

if os.path.isfile(imagenet_file):
    try:
        with open(imagenet_file) as imagenet_classes_file:
            imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())
    except Exception as e:
        print(f"Error loading ImageNet classes from '{imagenet_file}': {e}")
else:
    print(f"Warning: ImageNet classes file '{imagenet_file}' not found!")

def classifier(img_path, model_name):
    """
    Classifies an image using a pre-trained CNN model.
    Parameters:
      img_path - Path to the image file
      model_name - Name of the CNN model to use (resnet, alexnet, or vgg)
    Returns:
      Classification label as string
    """
    if not TORCH_AVAILABLE:
        return "pytorch_not_installed"
    
    if model_name not in model_dict:
        print(f"Error: Model '{model_name}' not found. Available: {list(model_dict.keys())}")
        return "invalid_model"
    
    if not os.path.isfile(img_path):
        print(f"Error: Image file '{img_path}' not found!")
        return "file_not_found"
    
    if not imagenet_classes_dict:
        print("Error: ImageNet classes dictionary not loaded!")
        return "imagenet_classes_missing"
    
    try:
        img_pil = Image.open(img_path)

        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        
        img_tensor = preprocess(img_pil)
        img_tensor.unsqueeze_(0)
        img_tensor.requires_grad_(False)

        model = model_dict[model_name]
        model = model.eval()
        
        output = model(img_tensor)
        pred_idx = output.data.numpy().argmax()

        return imagenet_classes_dict[pred_idx]
    
    except Exception as e:
        print(f"Error classifying image '{img_path}': {e}")
        return "classification_error"
