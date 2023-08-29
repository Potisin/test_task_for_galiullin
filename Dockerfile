FROM python:3.10

RUN mkdir /test_task_for_galiullin

WORKDIR /test_task_for_galiullin

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh