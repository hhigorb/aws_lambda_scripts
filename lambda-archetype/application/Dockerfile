FROM public.ecr.aws/lambda/python:3.11

WORKDIR /var/task

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY app.py ./
COPY scripts scripts/

CMD ["app.handler"]