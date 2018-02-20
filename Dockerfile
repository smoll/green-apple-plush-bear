FROM python:3.4-alpine

ENV CODE_HOME /code
RUN mkdir -p $CODE_HOME
WORKDIR $CODE_HOME

COPY requirements.txt $CODE_HOME
RUN pip install -r requirements.txt

COPY . $CODE_HOME

CMD ["python", "app.py"]
