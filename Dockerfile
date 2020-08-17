FROM python:3
COPY . /app
WORKDIR /app
RUN pip install -r install.txt
ENTRYPOINT ["python"]
CMD ["solution.py"]