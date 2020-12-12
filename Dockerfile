FROM debian:buster-slim

RUN apt-get update && apt-get install -y \
	gimp \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
	python3.7 \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
	python2 \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
	gimp-python \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*


COPY ./src/python-fu-cartoon.py /usr/lib/gimp/2.0/plug-ins/
RUN chmod +x /usr/lib/gimp/2.0/plug-ins/python-fu-cartoon.py

#RUN gimp -i -b '(python-fu-cartoon RUN-NONINTERACTIVE "doge.jpeg")' -b '(gimp-quit 0)'


COPY ./src /app
ENTRYPOINT ["python", "/app/app.py"]
