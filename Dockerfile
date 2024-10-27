FROM python:3.12

RUN mkdir /order

WORKDIR /order

COPY requirements.txt .

RUN pip install  -r requirements.txt

COPY . .

COPY docker/app.sh /order/

RUN chmod a+x /order/app.sh

CMD ["gunicorn", "app.main:app","--workers" ,"4","--worker-class","uvicorn.workers.UvicornWorker","--bind=0.0.0.0:8000"]
