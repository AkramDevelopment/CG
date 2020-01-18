# Cyber Gladiators
## Online Platform

---------


### Setup

Start mysql and create a database named `CG`, then:

macOS:
```
# install homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# add python to your path
echo 'export PATH="/usr/local/opt/python/libexec/bin:$PATH"' >> ~/.profile

# install python3
brew install python

# install virtualenv
pip3 install virtualenv

# setup env
./bin/setup.sh
```

linux:
```
sudo apt-get install python-dev default-libmysqlclient-dev libssl-dev
pip3 install virtualenv
./bin/setup.sh
```

---------

### Running
```
# Start Backend
./bin/run.sh
```

### Setup MySQL on Linux
```
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
```

