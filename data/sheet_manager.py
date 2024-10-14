import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

class SheetManager:
    def __init__(self, credentials_path, spreadsheet_url):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
        self.client = gspread.authorize(creds)
        self.sheet = self.client.open_by_url(spreadsheet_url)

    def get_worksheets(self):
        return self.sheet.worksheets()

    def get_sheet_data(self, worksheet):
        return worksheet.get_all_records()

    def update_scraped_data(self, worksheet, row_index, lion_data, torob_data):
        if lion_data:
            self._update_cell_with_backoff(worksheet, row_index, 15, str(lion_data[0]))  # Lion_Price
            self._update_cell_with_backoff(worksheet, row_index, 16, str(lion_data[1]))  # Lion_Stock
        if torob_data:
            self._update_cell_with_backoff(worksheet, row_index, 8, str(torob_data))  # Torob_Price

    def update_processed_data(self, worksheet, processed_data):
        for row in processed_data:
            self._update_cell_with_backoff(worksheet, row['row_index'], 18, str(row['Final_Price']))
            self._update_cell_with_backoff(worksheet, row['row_index'], 19, str(row['Final_Stock']))

    def _update_cell_with_backoff(self, worksheet, row, col, value):
        retries = 0
        while retries < 8:  # Max 8 retries
            try:
                worksheet.update_cell(row, col, value)
                break
            except gspread.exceptions.APIError as e:
                if e.response.status_code == 429:  # Quota exceeded error
                    print(f"Quota exceeded. Retrying in {2 ** retries} seconds...")
                    time.sleep(2 ** retries)
                    retries += 1
                else:
                    raise  # Re-raise other API errors
        else:
            print("Max retries exceeded. Unable to update cell.")
