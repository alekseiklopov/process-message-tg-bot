FROM python:3.7
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get dist-upgrade -y
RUN pip3 install --upgrade pip
RUN pip3 install pyTelegramBotAPI
ENV TG_TOKEN=${TG_TOKEN}
COPY . .
EXPOSE 4000
CMD ["python3", "./main.py"]
