echo "BUILD START"
python3.11.3 -m pip install -r requirements.txt
python3.11.3 -m manage.py collectstatic --noinput --clear
echo "BUILD END"