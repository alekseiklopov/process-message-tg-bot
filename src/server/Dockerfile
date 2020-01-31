FROM python:3.7
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get dist-upgrade -y
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir tensorflow
RUN pip3 install opencv-python
RUN pip3 install Flask
RUN pip3 install imutils
RUN pip3 install numpy
RUN pip3 install Pillow
RUN apt-get install git -y
RUN apt-get install python3-opencv -y
RUN pip3 install mtcnn
COPY . .
EXPOSE 4000
CMD ["python3", "./main.py"]

