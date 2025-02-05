# Telegram Medical Data Warehouse

This project involves building a data warehouse to store and analyze data on Ethiopian medical businesses by scraping information from Telegram channels and integrating object detection using YOLO. The system includes data extraction, cleaning, transformation, storage, and exposure via a FastAPI-based API for seamless access and analysis.


## Project Structure


```
├── notebooks
│   ├── 1.0.data-prepocessing-and-exploration.ipynb 
│   ├── README.md                 
│   ├── __init__.py               
│        
├── src
│   ├── README.md                 
│   ├── __init__.py               
│   ├── preprocess.py               
│   ├── scrape.py            
│   ├── visualize.py           
│
├── scripts            
│   ├── __init__.py
│   ├── scrape.sh          

│
├── tests
│   ├── __init__.py  
│
├── data            
│   ├── processed
│   │   ├── cleaned_data.csv
│
├── logs            
│   ├── data_cleaning.log
│   ├── data_scraper.log
│
├── assets            
│   ├── fonts
│   │   ├── NotoSerifEthiopic_Condensed-Regular.ttf
│
│
├── .env                   
├── .gitignore                 
├── README.md                   
├── requirements.txt    
```

## Installation

1. Clone the repository (if applicable):
   ```sh
   git clone https://github.com/Naod-Demissie/Telegram-Medical-Data-Warehouse.git
   cd Telegram-Medical-Data-Warehouse
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Contributing

Feel free to open an issue or submit a pull request.