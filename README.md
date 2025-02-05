# Telegram Medical Data Warehouse

This project involves building a data warehouse to store and analyze data on Ethiopian medical businesses by scraping information from Telegram channels and integrating object detection using YOLO. The system includes data extraction, cleaning, transformation, storage, and exposure via a FastAPI-based API for seamless access and analysis.


## Project Structure


```
├── notebooks
│   ├── 1.0.data-prepocessing-and-exploration.ipynb 
│   ├── 2.0-database-setup.ipynb
│   ├── 3.0-object-detection.ipynb
│   ├── README.md                 
│   ├── __init__.py               
│        
├── src
│   ├── README.md                 
│   ├── __init__.py               
│   ├── preprocess.py               
│   ├── scrape.py            
│   ├── visualize.py           
│   ├── create_db.py           
│   ├── predict.py           
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
│   │   ├── detections_results.csv
│   │   ├── telegram_messages.db
│
├── logs            
│   ├── data_cleaning.log
│   ├── data_scraper.log
│   ├── database_setup.log
│
├── assets            
│   ├── fonts
│   │   ├── NotoSerifEthiopic_Condensed-Regular.ttf
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
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

## Running the Application

Start the FastAPI app with Uvicorn:
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

- Replace `main` with the filename of your FastAPI app (e.g., `app.py`).
- The `--reload` flag enables automatic restarts on code changes (useful for development).

## Accessing the API

Once the server is running, open the following URLs in your browser:
- API Docs (Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Alternative API Docs (ReDoc): [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)


## Contributing

Feel free to open an issue or submit a pull request.