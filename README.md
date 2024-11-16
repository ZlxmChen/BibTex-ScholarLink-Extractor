# Scholar Link & Bibliographic Extractor

This project is a Python script that automates the extraction of citation links and bibliographic information from Google Scholar. It utilizes Selenium for web scraping and provides options to either overwrite or append results to output files.

## Features

- Extracts citation links from Google Scholar based on input queries (Support fuzzy search).
- Fetches bibliographic data in `.bib` format for each citation.
- Supports appending or overwriting results in the output files.
- Handles empty lines and failed queries gracefully.

## Features Incoming
- Support for GB/T 7714
- Enhance fuzzy search result
## Requirements

- Python 3.7 or higher
- Google Chrome browser (Safari browser is incoming!)
- ChromeDriver (compatible with your Chrome version)

### Python Libraries

Install the required libraries using pip:

```bash
pip install selenium
```
## Usage

### Code Setup
Clone the repository and update the input/output file paths in the script if needed.
```bash
git clone https://github.com/ZlxmChen/BibTex-ScholarLink-Extractor.git
cd BibTex-ScholarLink-Extractor
```
### ChromeDriver Setup

Download the ChromeDriver version that matches your Chrome browser from the [official website](https://developer.chrome.google.cn/docs/chromedriver/downloads).
Ensure the ChromeDriver executable is in your system's PATH or the same directory as the script.

### Input File Format
The input file (`scholars.txt`) should contain scholar data. Each query can be in a separate line. Empty lines are skipped.

### Output Files
- `links.txt`: Stores the extracted citation links.
- `bib.txt`: Stores bibliographic data in `.bib` format.

### Running the Script
Run the script using Python:
```bash
python main.py
```

### Controlling File Behavior
You can toggle whether the output files are overwritten or appended by changing the `append_mode` variable in the script:

- `True`: Append new results to existing files.
- `False`: Overwrite the existing files with new results.

Example:
```bash
append_mode = True  # Appends to output files
```

## Project Structure
```bash
.
├── main.py   # Main script
├── scholars.txt      # Input file (queries)
├── links.txt         # Output file (citation links)
├── bib.txt           # Output file (.bib bibliographic data)
└── README.md         # Project documentation
```

## Known Issues

- **Timeouts**: Slow internet or changes to Google Scholar's structure may cause timeouts. Increase `WebDriverWait` durations if needed.
- **CAPTCHA**: Excessive queries might trigger CAPTCHA verification. Use delays (`time.sleep`) to reduce the frequency of requests.

## Contributing

Contributions are welcome! If you encounter bugs or have feature suggestions, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## 