FROM resin/rpi-raspbian:jessie

# Install Python, pip and the camera module firmware
RUN apt-get update
RUN apt-get install -y python python-dev libraspberrypi-bin python-pip
RUN pip install rpi.gpio
RUN pip install PIL --allow-external PIL --allow-unverified PIL
RUN pip install picamera
ADD . /app
CMD modprobe bcm2835-v4l2 && python /app/PIRSHOT.py
