# Base image
FROM arm32v7/python:3.6-stretch

# Fixing timezone:
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install Depencies
RUN pip install --no-cache-dir rpi.gpio
RUN pip intall firebase_admin

# Copying over files
COPY /src /src
RUN rm -f /src/firestore_creds.json
WORKDIR /src

# Running program
CMD ["python3", "main.py"]
