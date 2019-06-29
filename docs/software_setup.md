# Software Setup

After finishing these steps, you'll be all set to program JetRacer.  Once you're finished, run through the [examples](examples.md).

## Step 1 - Flash micro SD card

1. Download the JetCard SD card image [jetcard_v0p0p0.img](https://drive.google.com/open?id=1wXD1CwtxiH5Mz4uSmIZ76fd78zDQltW_) onto a Windows, Linux or Mac *desktop machine*
    
    > You can check it against this [md5sum](https://drive.google.com/open?id=1356ZBrYUWaTgbV50UMB1uCfWrNcd6PEF)

2. Insert a 32GB+ SD card into the desktop machine
3. Using [Etcher](https://www.balena.io/etcher/) select ``jetcard_v0p0p0.img`` and flash it onto the SD card
4. Remove the SD card from the desktop machine

> Please note, the password for the pre-built SD card is ``jetson``

## Step 2 - Power on and connect over USB

1. Insert the configured SD card into the Jetson Nano module

2. Power on by plugging the USB barrel plug adapter into the USB battery pack
3. Connect your Windows, Linux, or Mac machine to the Jetson Nano via micro USB

4. On your Windows, Linux, or Mac machine, open a browser and navigate to ``192.168.55.1:8888``
5. Sign in using the default password ``jetson``

## Step 2 - Connect JetRacer to WiFi

1. Open a terminal in Jupyter Lab by clicking ``File`` -> ``New`` -> ``Terminal``

2. In the terminal, type the following command to list available WiFi networks, and find the ``ssid_name`` of your network.

    ```bash
    sudo nmcli device wifi list
    ```
3. Connect to  the selected WiFi network

    >  It should be on the same network that you will be webprogramming from

    ```bash
    sudo nmcli device wifi connect <ssid_name> password <password>
    ```
4. Note down the WiFi IP address (``inet``) of the WiFi interface ``wlan0`` returned by the following command.  We'll call this ``jetson_ip_address``
    
    ```bash
    ifconfig
    ```

## Step 4 - Connect to JetRacer over WiFi

1. Unplug the micro USB cable from the Jetson Nano

2. Close the previous Jupyter Lab browser tab
3. Open a new browser tab and navigate to ``http://<jetson_ip_address>:8888``
4. Sign in with the password ``jetson``
    
## Step 5 - Install Python packages

>  Ensure that the Jetson Nano is connected to internet

1. Open a terminal and call the following to install the [JetCam](http://github.com/NVIDIA-AI-IOT/jetcam) Python package.

    ```bash
    cd $HOME
    git clone https://github.com/NVIDIA-AI-IOT/jetcam
    cd jetcam
    sudo python3 setup.py install
    ```
    
2. Execute the following command to install the [torch2trt](http://github.com/NVIDIA-AI-IOT/torch2trt) Python package

    ```bash
    cd $HOME
    git clone https://github.com/NVIDIA-AI-IOT/torch2trt
    cd torch2trt
    sudo python3 setup.py install
    ```
    
2. Execute the following in a terminal to install the [JetRacer](http://github.com/NVIDIA-AI-IOT/jetracer) package
 
     ```bash
     cd $HOME
     git clone https://github.com/NVIDIA-AI-IOT/jetracer
     cd jetracer
     sudo python3 setup.py install
     ```
 
## Step 6 - Set the Jetson Nano to 5W mode

To prevent the Jetson Nano from drawing more power than the battery can supply, we set it to 5W mode

1. Open a terminal and call the following to set 5W mode

    ```bash
    sudo nvpmodel -m1
    ```
    
## Next

Next, follow run through the [examples](examples.md).
