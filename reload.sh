ps aux |grep gunicorn |grep assist433 | awk '{ print $2 }' |xargs kill -HUP

