# Yuka Barcode Generator

**Yuka-Barcode-Gen** is a Python program that provides a workaround for an exclusive feature on the Yuka app by web scraping the UPC number of an item from the Target website and generating a barcode for easy scanning.

## Features

- Scrapes UPC numbers from Target product pages.
- Generates barcodes for use in the Yuka app.
- Simple and easy-to-use command-line interface.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/gitedmond/Yuka-Barcode-Gen.git
   cd Yuka-Barcode-Gen
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script with a Target product URL:

   ```bash
   python yukabarcode.py "https://www.target.com/p/product-url"
   ```

2. The generated barcode will be saved as an image file.

## Requirements

- Python 3.x
- Required libraries listed in `requirements.txt`

## Contributing

Feel free to submit issues or feature requests via GitHub Issues. Contributions are welcome!

