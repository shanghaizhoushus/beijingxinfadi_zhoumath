# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 21:06:12 2024

@author: zhoushus
"""

import time
from datetime import datetime
from data_scraper import DataScraper
from data_processor import DataProcessor
from email_sender import EmailSender

# Define the scraping and email-sending process as a function
def send_fruit_price():
    driver_path = r"D:/msedgedriver.exe"
    url = 'http://www.xinfadi.com.cn/priceDetail.html'
    today = datetime.now().strftime("%Y-%m-%d")

    # Define the list of products to scrape
    products = [
        {"name": "箱装菠萝", "check": lambda data: True},
        {"name": "火龙果", "check": lambda data: data[6] == "红", "alias": "红心火龙果"},
        {"name": "国产香蕉", "check": lambda data: True},
        {"name": "百香果", "check": lambda data: data[1] == "其他类"}
    ]

    # Step 1: Initialize and set up the scraper
    scraper = DataScraper(driver_path)
    scraper.setup_driver()
    scraper.open_url(url)
    scraper.select_category("//a[contains(text(),'水果')]")

    raw_data = []
    for product in products:
        scraper.search_product(product["name"], 'prodName', 'search')
        raw_data += scraper.extract_table_data('tableBody')

    scraper.close_driver()  # Close the browser

    # Step 2: Process the scraped data
    processor = DataProcessor(products)
    processed_data = processor.process_data(raw_data, today)
    html_table = processor.generate_html_table(processed_data, today)
    
    email = "zhoushus@foxmail.com"

    # Step 3: Send the data via email
    email_sender = EmailSender(
        smtp_server="smtp.qq.com",
        smtp_port=465,
        sender_email=email,
        sender_password=""
    )
    email_sender.send_email(
         receiver_email=email,
         subject=f"今日水果价格 - {today}",
         body=html_table
     )

# Wait until the target time (20:00) every day
def wait_until_target_time(target_hour, target_minute):
    while True:
        now = datetime.now()
        # Check if the current time matches the target
        if now.hour == target_hour and now.minute == target_minute:
            return
        time.sleep(30)  # Check the time every 30 seconds

if __name__ == "__main__":
    while True:
        # Wait for 20:00 (8 PM) daily
        wait_until_target_time(20, 0)

        # Execute the main function
        try:
            send_fruit_price()
            print(f"Task executed successfully at {datetime.now()}")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Prevent multiple triggers within the same minute
        time.sleep(60)

