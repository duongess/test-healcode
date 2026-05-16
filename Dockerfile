# Su dung image python ban mong nhe
FROM python:3.10-slim

# Thiet lap thu muc lam viec mac dinh
WORKDIR /app

# Cai dat cac thu vien can thiet
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Chuyen toan bo ma nguon vao container
COPY . .

# Chay file chinh cua ung dung
CMD ["python", "main.py"]