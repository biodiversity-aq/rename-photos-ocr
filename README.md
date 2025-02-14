# Rename Photos with OCR

This script automates the renaming of specimen photos by extracting labels using Optical Character Recognition (OCR). It uses **PaddleOCR** to detect text and **OpenCV** to correct image rotation before processing.

## Features

- Automatically extracts text labels from images using OCR
- Corrects rotated images before text extraction
- Replaces spaces and invalid filename characters in extracted text
- Handles duplicate filenames by appending sequential numbers
- Copies and renames images into a separate folder

## Caveats

- OCR may not recognise "_" well. Sometimes it is omitted, sometimes it is recognised as other character such as ".", "/". Manual inspection of extracted label is advised.
- The script was used to extract **printed** text labels from image and not handwriting.

## Installation

### Prerequisites
Make sure you have **Python 3.8 or higher** installed. Then, install the required dependencies:

```sh
pip install -r requirements.txt
```

Or manually install the required libraries:
```sh
pip install paddleocr opencv-python numpy
```

## Usage

### 1. Prepare Your Images
- Place the images you want to rename inside the `photos/` folder.

### 2. Run the Script
Run the script using:
```sh
python src/rename_images.py
```

### 3. Check the Renamed Files
- The renamed images will be saved inside the `renamed/` folder.
- The filenames will be based on the extracted labels.
- If duplicate labels exist, sequential numbers (e.g., `_1`, `_2`) will be appended.

## Folder Structure
```
rename-photos-ocr/
│── photos/               # Input images (place your images here)
│── renamed/              # Output directory (renamed images)
│── src/                  # Source code directory
│   ├── rename_images.py  # Main script
│── requirements.txt      # Dependencies list
│── README.md             # Project documentation
│── .gitignore            # Ignore unnecessary files
```

## Example Output

Before:

![photos/IMG_2137.JPG](./photos/IMG_2137.JPG =250x)

File was `photos/IMG_2137.JPG`

After OCR and renaming:
```
renamed/AAV3FF_00161.jpg
```

## License
This project is licensed under the MIT License.

## Acknowledgments
Developed with assistance from ChatGPT.

