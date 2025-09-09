# Image Steganography Tool

A Python GUI tool to hide and extract secret messages from images using LSB (Least Significant Bit) technique.

## ✅ Features

- Hide text messages in PNG or BMP images
- Extract messages from encoded images
- Simple GUI using Tkinter
- Supports drag-and-drop-like file selection
- Lossless PNG/BMP format support

## 💻 How to Run

1. **Clone or Download** the repo
2. Install the required Python libraries
3. Run the tool

## 🔐 How It Works

- Converts message to binary
- Embeds each bit into the least significant bit of image pixels (RGB)
- Uses a termination flag (`11111110`) to mark the end

## 📁 Supported Formats

- PNG
- BMP

## 📤 Deliverables

- GUI Tool (`main.py`)
- Dependencies (`requirements.txt`)

---

**Note:** Do **not** use JPEG images — they use lossy compression which will destroy hidden data.
