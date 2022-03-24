#!/usr/bin/env bash
# configure nginx server

apt update
apt-get -y install nginx
ufw allow 'Nginx HTTP' 2> /dev/null
# echo 'Hello World!' > /usr/share/nginx/html/index.html
# echo 'Hello World!' >  /var/www/html/index.nginx-debian.html
mkdir -p /data/web_static/releases 2> /dev/null
mkdir /data/web_static/shared
mkdir /data/web_static/releases/test
touch /data/web_static/releases/test/index.html
echo 'Hello World\n\nWelcome to nginx' > /data/web_static/releases/test/index.html

if [ -f '/data/web_static/current' ]
then
	rm -f /data/web_static/current
fi

ln -s /data/web_static/releases/test /data/web_static/current

g_id=$(getent passwd ubuntu | cut -d: -f3)
group=$(getent group $g_id | cut -d: -f1)

for file in ls -R /data
do
	chown ubuntu:$group $file
done

sed -i '/location \// i \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sed -i '/listen 80 default_server;/ a \\trewrite ^/redirect_me https://github.com/dnjoe96 permanent;' /etc/nginx/sites-available/default
sed -i '/listen 80 default_server;/ a \\trewrite ^/redirect_me/ https://github.com/dnjoe96 permanent;' /etc/nginx/sites-available/default
touch /var/www/html/custom_404.html && echo "Ceci n'est pas une page" > /var/www/html/custom_404.html
sed -i '/listen 80 default_server;/ a \\terror_page 404 /custom_404.html;' /etc/nginx/sites-available/default
sed -i '/server_name _;/ a \\tadd_header X-Served-By $HOSTNAME;' /etc/nginx/sites-available/default
service nginx restart
exit 0
