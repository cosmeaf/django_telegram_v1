# django_telegram_v1
# django_telegram_v1


Good,

make the git clone and after doing so, run the commands below:

git clone https://github.com/cosmeaf/django_telegram_v1.git

cd django_telegram_v1

python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:80
