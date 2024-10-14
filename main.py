import os
from dotenv import load_dotenv
import time
from web.scraper import LionScraper, TorobScraper
from data.data_processor import DataProcessor
from data.sheet_manager import SheetManager
from web.web_updater import WebUpdater

load_dotenv()  # Load environment variables from .env file

def main():
    # Initialize components
    lion_scraper = LionScraper()
    torob_scraper = TorobScraper()
    data_processor = DataProcessor()
    sheet_manager = SheetManager('google_sheets_credentials.json', os.getenv('SPREADSHEET_URL'))
    web_updater = WebUpdater(os.getenv('ADMIN_USERNAME'), os.getenv('ADMIN_PASSWORD'))

    # Process each worksheet
    for worksheet in sheet_manager.get_worksheets():
        print(f"Processing worksheet: {worksheet.title}")
        
        # Get data from sheet
        data = sheet_manager.get_sheet_data(worksheet)
        
        # Scrape data
        for row in data:
            lion_data = lion_scraper.scrape(row['Lion_Link'])
            torob_data = torob_scraper.scrape(row['Torob_Link'])
            
            # Update sheet with scraped data
            sheet_manager.update_scraped_data(worksheet, row['row_index'], lion_data, torob_data)
        
        # Process data
        processed_data = data_processor.process(data)
        
        # Update sheet with processed data
        sheet_manager.update_processed_data(worksheet, processed_data)
        
        # Update web
        web_updater.update_products(processed_data)
        
        time.sleep(5)  # Pause between worksheets to avoid rate limiting

if __name__ == "__main__":
    main()
