FROM python
WORKDIR /myproject
COPY . .
RUN pip install -r requirements--no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_DEBUG=True
CMD ["python" , "flask-hello.py"]
 