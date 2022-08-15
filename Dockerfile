# 
FROM python:3.10.6-slim-bullseye

# 
WORKDIR /hafo

# 
COPY ./requirements.txt /hafo/requirements.txt

# RUN  pip install --upgrade pip
# 
RUN pip install --no-cache-dir --upgrade -r /hafo/requirements.txt

# 
COPY ./app /hafo/app

# 
CMD ["uvicorn", "app.main:app","--reload", "--host", "0.0.0.0", "--port", "8001"]

EXPOSE 8001
