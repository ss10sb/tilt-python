### Requirements

##### Pip
* wheel

##### OS (pybluez[ble])
* python-dev
* pkg-config
* libbluetooth-dev 
* libglib2.0-dev 
* libbooth-python-dev 
* libbooth-thread-dev 

Increase the swap size (on a pi) or compiling pybluez[ble] will fail.

`sudo nano /etc/dphys-swapfile`

`CONF_SWAPSIZE=1024`

```
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
```
