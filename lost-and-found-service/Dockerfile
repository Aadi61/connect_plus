FROM python
WORKDIR /app
RUN apt-get update && apt-get install -y gcc
RUN pip install flask pymongo flask_cors boto3
COPY . .
EXPOSE 5000
CMD ["python","app.py"]
