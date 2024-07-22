# YahooFinanceScraper

YahooFinanceScraper is a command-line tool designed to extract and save key statistical data from publicly listed companies on Yahoo Finance. It retrieves information such as market capitalization, enterprise value, P/E ratios, and other financial indicators, and stores them in a CSV file.

## Features

- Fetches financial data from Yahoo Finance.
- Targets specific company tickers.
- Saves extracted data into a CSV file.
- Simple usage via command line.

## Prerequisites

Before you begin using YahooFinanceScraper, ensure you have Python 3.6+ installed on your machine. You will also need the following libraries:
- BeautifulSoup4
- requests
- click
- csv

You can install all necessary dependencies with pip:

```bash
pip install beautifulsoup4 requests click
```

## Installation

Clone the GitHub repository using:

```bash
git clone https://github.com/Tamachiii/YahooFinanceScraper.git
```

## Usage

To use the script, navigate to the project folder and run the script file by passing the company's ticker as an argument:

```bash
python finance_scraper.py [TICKER]
```

Example:

```bash
python finance_scraper.py GOOG
```

This will extract financial data for Google and save the results in `goog_finance_data.csv`.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Discord: tamachiii

Project Link: [https://github.com/Tamachiii/YahooFinanceScraper](https://github.com/Tamachiii/YahooFinanceScraper)
