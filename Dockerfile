FROM python:3.11.3

WORKDIR /ldustatsback

COPY requirements.txt /ldustatsback
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . /ldustatsback

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]