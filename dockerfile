FROM python

WORKDIR /usr/app/
COPY /python/app /usr/app/

RUN pip install -r requirements.txt
CMD python app.py