# Pet Image Classifier

A Python application that uses pre-trained CNN models to classify pet images and determine if they are dogs or not.

## Programmer
**Name:** Ritik Kumar  
**Date Created:** October 3, 2025

## Project Description
This project classifies pet images using pre-trained CNN models (ResNet, AlexNet, or VGG) and compares the results against true labels. It also determines whether images correctly classify dogs and dog breeds.

## Features
- Supports multiple CNN architectures: ResNet, AlexNet, VGG
- Automatic pet label extraction from filenames
- Dog breed classification
- Statistical analysis of classification results
- Detailed error reporting

## Requirements
- Python 3.6 or higher
- PyTorch
- torchvision
- Pillow (PIL)

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage with default settings (VGG model, pet_images folder):
```bash
python check_images.py
```

Specify a different model:
```bash
python check_images.py --arch resnet
```

Specify a different image directory:
```bash
python check_images.py --dir /path/to/images/
```

Specify a different dog names file:
```bash
python check_images.py --dogfile custom_dognames.txt
```

### Command Line Arguments
- `--dir`: Path to folder of pet images (default: 'pet_images/')
- `--arch`: CNN model architecture - choices: resnet, alexnet, vgg (default: 'vgg')
- `--dogfile`: Text file containing valid dog names (default: 'dognames.txt')

## Project Structure
```
.
├── check_images.py                      # Main script
├── get_input_args.py                    # Command line argument parsing
├── get_pet_labels.py                    # Extract labels from filenames
├── classify_images.py                   # Classify images using CNN
├── adjust_results4_isadog.py            # Determine if classification is a dog
├── calculates_results_stats.py          # Calculate statistics
├── print_results.py                     # Print results
├── classifier.py                        # CNN classifier wrapper
├── print_functions_for_lab_checks.py    # Helper functions for checking
├── dognames.txt                         # Valid dog breed names
├── imagenet1000_clsid_to_human.txt      # ImageNet class labels
├── requirements.txt                     # Python dependencies
└── pet_images/                          # Folder containing pet images
```

## File Naming Convention
Image files should follow this naming pattern:
```
Breed_name_number.jpg
```
Example: `Golden_retriever_05223.jpg`

The script extracts the breed name by:
1. Converting filename to lowercase
2. Splitting by underscores
3. Keeping only alphabetic words
4. Joining words with spaces

## Output
The script provides:
1. Number of images processed
2. Number of dog images
3. Number of non-dog images
4. Percentage of correct matches
5. Percentage of correct dog classifications
6. Percentage of correct breed classifications
7. Percentage of correct non-dog classifications
8. Lists of incorrect classifications (if any)

## Error Handling
The application includes comprehensive error handling for:
- Missing files and directories
- Invalid model names
- Missing dependencies
- File read/write errors
- Classification failures

## Notes
- The first run may take longer as it downloads pre-trained model weights
- Ensure all image files are valid and readable
- The dognames.txt file should contain one dog breed per line
- Hidden files (starting with '.') are automatically skipped

## Troubleshooting

**PyTorch not found:**
```bash
pip install torch torchvision
```

**PIL/Pillow errors:**
```bash
pip install --upgrade Pillow
```

**Model download issues:**
Ensure you have a stable internet connection for the first run to download model weights.

## License
See LICENSE file for details.
