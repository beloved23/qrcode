source ~/Envs/qrcode/bin/activate

pkill -f 'scannerr.wsgi'

echo starting gunicorn
exec gunicorn scannerr.wsgi -b 0.0.0.0:3000  --daemon\
     --workers=10 -t 2300 \
     --worker-connections 12

