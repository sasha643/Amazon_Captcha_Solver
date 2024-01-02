# Amazon CAPTCHA Solver

## Overview

This Python script is designed to perform web scraping on Amazon's search page. It incorporates the [easyocr](https://github.com/JaidedAI/EasyOCR) library for optical character recognition (OCR) to overcome CAPTCHAs encountered during the process.

## Prerequisites

- Python 3.x
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [Selenium](https://www.selenium.dev/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Installation

1. **Install the required Python packages:**

    ```bash
    pip install easyocr selenium beautifulsoup4
    ```

2. **Download and install the Microsoft Edge WebDriver:**

    [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

3. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/amazon-web-scraping.git
    ```

4. **Navigate to the project directory:**

    ```bash
    cd amazon-web-scraping
    ```

5. **Run the script:**

    ```bash
    python amazon_scraper.py
    ```

## Configuration

- Ensure you have the appropriate version of the Microsoft Edge WebDriver installed.
- Adjust the `easyocr.Reader` parameters based on your specific OCR requirements.
- Customize the script for handling CAPTCHAs and form submissions as needed.

## Acknowledgments

- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [Selenium](https://www.selenium.dev/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

## Contributing

1. **Fork the repository.**
2. **Create a new branch (`git checkout -b feature/new-feature`).**
3. **Make your changes.**
4. **Commit your changes (`git commit -am 'Add new feature'`).**
5. **Push to the branch (`git push origin feature/new-feature`).**
6. **Create a new pull request.**
