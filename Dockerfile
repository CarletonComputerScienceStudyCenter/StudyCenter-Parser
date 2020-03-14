FROM python:3

ADD parse.py /

#RUN pip install pystrich

CMD [ "python", "./parse.py" ]