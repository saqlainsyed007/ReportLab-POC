# ReportLab-POC

Install Requirements:
```
pip install -r requirements.txt
```

Create a reportlab account:
```
https://www.reportlab.com/accounts/register/
```

Install reportlab using registered credentials
```
pip install rlextra -i https://www.reportlab.com/pypi/
```

Migrate DB:
```
python manage.py migrate
```

Run server:
```
python manage.py runserver 0:8000
```

Generate sample pdf:
```
http://localhost:8000/pdf/create
```
