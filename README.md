# E-commerce Price and Stock Updater

This project automates the process of scraping product information from competitor websites, comparing prices, and updating your e-commerce platform accordingly.

## Features

- Web scraping from multiple sources (customizable)
- Price comparison and stock management
- Google Sheets integration for data storage and processing
- Automated updating of product information on your e-commerce platform

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ecommerce-updater.git
   cd ecommerce-updater
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Google Sheets API credentials:
   - Follow the [Google Sheets API Python Quickstart](https://developers.google.com/sheets/api/quickstart/python) to obtain your credentials.
   - Save the credentials file as `google_sheets_credentials.json` in the project root.

4. Create a `.env` file in the project root and add your configuration:
   ```
   SPREADSHEET_URL=your_google_sheets_url
   ADMIN_USERNAME=your_admin_username
   ADMIN_PASSWORD=your_admin_password
   ADMIN_LOGIN_URL=your_admin_login_url
   ADMIN_UPDATE_URL=your_admin_update_url
   ```

5. Customize the scraper classes in `scraper.py` for your target websites.

6. Modify the `WebUpdater` and `SeleniumManager` classes to match your e-commerce platform's admin interface.

## Usage

Run the main script:

```
python main.py
```

## Customization

To adapt this project for your own e-commerce platform:

1. Scraping:
   - Modify or create new scraper classes in `scraper.py` to target your competitor websites.
   - Update the `scrape` method in each scraper class to extract relevant information.

2. Data Processing:
   - Adjust the `DataProcessor` class in `data_processor.py` to implement your pricing and stock management logic.

3. Google Sheets:
   - Modify the `SheetManager` class in `sheet_manager.py` to match your Google Sheets structure.

4. Web Updating:
   - Update the `WebUpdater` class in `web_updater.py` and the `SeleniumManager` class in `selenium_manager.py` to interact with your e-commerce platform's admin interface.
   - Modify the element locators and URL patterns to match your admin panel's structure.

5. Main Execution:
   - Adjust the `main.py` file to orchestrate the process according to your needs.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
"# PriceStockUpdater" 
