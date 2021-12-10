
# Use fix_mikrotik branch
git clone ---branch fix_mikrotik git@github.com:AAm-kun/netmiko.git\
sudo pip install -r requirement.txt\
python3 setup.py build\
sudo python3 setup.py install

# Or

change 
https://github.com/jgmel/netmiko/blob/d408eb532cbd2b5ee407ff1fa854978784886571/netmiko/base_connection.py

and 

https://github.com/jgmel/netmiko/blob/7fcd32732f06c19b59e6b7a3a40622795c84e2e3/netmiko/mikrotik/mikrotik_ssh.py

here is the issue link

https://github.com/ktbyers/netmiko/issues/1600

