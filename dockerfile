FROM python:3.10-alpine

RUN apk --update add gcc build-base freetype-dev libpng-dev openblas-dev postgresql-dev

WORKDIR /app/

COPY ./req.txt /app/

RUN pip install -r req.txt

COPY ./ /app/

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]