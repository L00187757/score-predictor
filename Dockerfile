
FROM python:3.8
WORKDIR  /.ssh/projects/score-predictor
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "flaskapp.py"]

