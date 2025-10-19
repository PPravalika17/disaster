FROM python:3.11-slim
WORKDIR /app


# install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# copy app
COPY . /app


EXPOSE 5000


# use gunicorn for production
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]