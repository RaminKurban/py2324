from fastapi import FastAPI
import datetime

app = FastAPI()


@app.get("/")
def root():
    return "time and date service on fastapi"


@app.get("/time")
def time():
    time_now = datetime.datetime.now().strftime('%H:%M:%S')
    time_string = f'Точное время {time_now}.'
    return time_string


@app.get("/date")
def time():
    date_now = datetime.datetime.now().strftime('%Y %m %d')
    date_string = f'Точная дата {date_now}.'
    return date_string