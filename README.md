
# Beijing Xinfadi Project

This project is designed to automate data scraping, processing, and email notifications related to data collected from the Beijing Xinfadi Market.

## Features
1. **Data Scraper**: Collects data from the web.
2. **Data Processor**: Cleans and processes raw data.
3. **Email Sender**: Sends email reports based on the processed data.
4. **Main Script**: Coordinates the entire workflow.

## Project Structure
- `data_scraper.py`: Handles the collection of data from specified online sources.
- `data_processor.py`: Processes and cleans the collected data.
- `email_sender.py`: Sends email reports using the processed data.
- `main.py`: The central script that ties all the components together.

## Requirements
- Python 3.x
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `smtplib`
  - `email-validator`

To install the dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/shanghaizhoushus/beijingxinfadi_project.git
   ```
2. Navigate to the project folder:
   ```bash
   cd beijingxinfadi_project
   ```
3. Run the main script to initiate the workflow:
   ```bash
   python main.py
   ```

## License
This project is licensed under the MIT License. Feel free to modify and use it as needed.

## Contribution
Contributions are welcome! If you want to contribute to the project, feel free to fork the repository and create a pull request.

## Contact
For questions or suggestions, please reach out at [zhoushus@foxmail.com].
