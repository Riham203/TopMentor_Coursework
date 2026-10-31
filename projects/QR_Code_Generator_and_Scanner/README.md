# QR Code Generator and Scanner

## Project Overview

This project is a Python-based **QR Code Generator and Scanner** that allows users to generate QR codes from text and scan QR codes using images or a live webcam feed.

It combines QR code generation, image processing, and computer vision to create and decode QR codes using Python libraries.

The generated QR code in this project contains the text:

`HI, Its Riham`

## Features

### 1. QR Code Generator

- Generates QR codes from custom text or data.
- Uses high error correction for better readability.
- Allows customization of QR code size and border.
- Saves the generated QR code as a PNG image.
- Displays the generated QR code inside the Jupyter Notebook.

### 2. QR Code Scanner – Image-Based

- Reads QR codes from image files.
- Detects and decodes QR code content using OpenCV.
- Displays the extracted text.
- Draws a bounding box around the detected QR code.
- Shows the scanned image using Matplotlib.

### 3. QR Code Scanner – Live Webcam

- Accesses the computer's webcam.
- Scans QR codes in real time.
- Extracts and displays decoded QR code data.
- Highlights detected QR codes with a green boundary.
- Displays decoded text on the camera feed.
- Press `q` to exit the scanner.

## Tools & Technologies

- **Python** – Programming language
- **qrcode** – QR code generation
- **Pillow (PIL)** – Image creation and processing
- **OpenCV** – QR code detection and computer vision
- **Pyzbar** – QR code decoding from webcam frames
- **NumPy** – Image and array operations
- **Matplotlib** – Image visualization
- **Jupyter Notebook** – Development environment

## Project Structure

```text
QR_Code_and_Scanner/
│
├── QR_Code_and_Scanner.ipynb
├── my_qr_code.png
└── README.md
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
```

### 2. Navigate to the Project Folder

```bash
cd TopMentor_Coursework/projects/QR_Code_and_Scanner
```

Adjust the folder name if your actual GitHub project folder uses a different name.

### 3. Install Dependencies

Run the following command in your terminal or Jupyter Notebook:

```bash
pip install "qrcode[pil]" opencv-python pyzbar matplotlib Pillow numpy
```

**Note:** Pyzbar may require the ZBar system library to be installed separately, depending on your operating system.

## How to Run

### Step 1: Open the Notebook

Open `QR_Code_and_Scanner.ipynb` using Jupyter Notebook or VS Code.

### Step 2: Generate a QR Code

Run the QR Code Generator section.

You can change the data to encode by modifying:

```python
data = "HI, Its Riham"
```

The generated QR code will be saved as:

```text
my_qr_code.png
```

### Step 3: Scan a QR Code from an Image

Run the image-based scanner section:

```python
scan_qr_code("my_qr_code.png")
```

The program detects the QR code, extracts its content, and displays the image with a highlighted boundary.

### Step 4: Scan QR Codes Using a Webcam

Run the live webcam scanner section.

- Allow camera access if prompted.
- Show a QR code in front of the camera.
- The decoded content will appear in the terminal and on the video feed.
- Press `q` to exit.

## Key Learning Outcomes

- Generating QR codes programmatically.
- Understanding QR code error correction.
- Processing images using OpenCV.
- Detecting and decoding QR codes.
- Accessing webcam input using Python.
- Using NumPy for image coordinate processing.
- Visualizing images with Matplotlib.
- Building real-time computer vision applications.

## Author

**Riham**

GitHub: [Riham](https://github.com/Riham203)
