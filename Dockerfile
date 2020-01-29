FROM python:3.7
RUN apt update
RUN apt upgrade -y
RUN apt dist-upgrade -y
RUN pip3 install --upgrade pip
RUN pip3 install tensorflow
RUN pip3 install opencv-python
RUN pip3 install numpy
RUN apt install git -y
RUN apt install python3-opencv -y
RUN pip3 install git+https://github.com/faustomorales/keras-ocr.git#egg=keras-ocr
RUN pip3 install mtcnn
COPY . .
EXPOSE 4000
CMD ["python", "./src/main.py"]

