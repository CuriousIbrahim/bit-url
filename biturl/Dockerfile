FROM python:3.8.6

WORKDIR /usr/src/biturl

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# ENTRYPOINT uwsgi uwsgi.ini
