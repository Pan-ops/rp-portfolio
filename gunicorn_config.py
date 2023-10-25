bind = '/etc/systemd/system/gunicorn.socket'
user = 'pan'
chdir = '/home/pan/rp-portfolio'
bind = '10.0.0.4:8000'
worker = 3
