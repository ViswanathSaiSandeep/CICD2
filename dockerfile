FROM python:3.8-slim
WORKDIR /dockdir
COPY . .
CMD [ "python", "program.py" ]