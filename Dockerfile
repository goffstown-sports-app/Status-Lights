# Base image
FROM arm32v7/python:3.6-stretch

# Meta for Docker Hub
LABEL description="🍇 Status lights for each program using LEDs connected to a RPI"
LABEL maintainer="matthewgleich@gmail.com"

# Fixing timezone:
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install Depencies
RUN pip install --no-cache-dir rpi.gpio
RUN pip install firebase_admin

# Copying over files
COPY /src /src
RUN rm -f /src/firestore_creds.json
WORKDIR /src

# Running program
CMD ["python3", "main.py"]
