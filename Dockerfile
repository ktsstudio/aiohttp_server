FROM python:3.7
RUN apt update && apt -y install gettext-base
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x run.sh
CMD ["./run.sh"]