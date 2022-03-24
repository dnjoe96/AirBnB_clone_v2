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

sed -i '/location \// i \\tlocation /hbnb_static {\n\t\troot /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sed -i '/listen 80 default_server;/ a \\trewrite ^/redirect_me https://github.com/dnjoe96 permanent;' /etc/nginx/sites-available/default
sed -i '/listen 80 default_server;/ a \\trewrite ^/redirect_me/ https://github.com/dnjoe96 permanent;' /etc/nginx/sites-available/default
touch /var/www/html/custom_404.html && echo "Ceci n'est pas une page" > /var/www/html/custom_404.html
sed -i '/listen 80 default_server;/ a \\terror_page 404 /custom_404.html;' /etc/nginx/sites-available/default
sed -i '/server_name _;/ a \\tadd_header X-Served-By $HOSTNAME;' /etc/nginx/sites-available/default
service nginx restart

Install Nginx if it not already installed
Create the folder /data/ if it doesn’t already exist
Create the folder /data/web_static/ if it doesn’t already exist
Create the folder /data/web_static/releases/ if it doesn’t already exist
Create the folder /data/web_static/shared/ if it doesn’t already exist
Create the folder /data/web_static/releases/test/ if it doesn’t already exist
Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static
