# Add domain configuration in nginx sites enabled

sudo ln -s ${`pwd`}/$1 /etc/nginx/sites-enabled/$1
sudo nginx -t
# sudo service nginx reload