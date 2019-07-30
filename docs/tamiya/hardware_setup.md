# Hardware Setup - Tamiya TT02

Follow these instructions to build JetRacer - Tamiya TT02 version.  After you've finished, move on to the [software setup](../software_setup.md).

## Tools

* Phillips screwdriver set
* Hex screwdriver
* Drill with 3mm and 6mm drill bits
* Countersink drill bit
* Pliers
* Wire strippers

## Phase 1 - TT-02 chassis setup
### Step 1 - Drilling mount holes to TT-02 chassis

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60310435-c165b600-9907-11e9-858b-238e801b11ab.JPG" height=128/>


1. Remove the 4 pins securing the shroud
2. Remove the shroud from the chassis

### Step 2 - Countersink 

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60311224-37b7e780-990b-11e9-92b1-04fd1bc78b41.JPG" height=128/>

1. Remove the two screws securing the electronics hub to the chassis
2. Pry the electronics hub from the chassis
3. Remove the ESC and RC receiver from the electronics hub
4. Disconnect the two servo cables from the RC receiver
5. Remove the foam adhesive from the RC receiver

## Phase 2 - Mounting things on base plate
### Step 1 - RC Servo Mux

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60311869-ec530880-990d-11e9-9b9b-efabfcef251e.JPG" height=128/>

1. Select 4 female-to-female jumper cables from the bundle
2. Attach the jumpers to the servo driver pins ``VCC`` (white), ``SDA`` (gray), ``SCL`` (purple) and ``GND`` (black)
3. Attach the other end of the jumpers to the Jetson Nano pins ``3.3V`` (white), ``3`` (gray), ``5`` (purple) and ``GND`` (black)

### Step 2 - Servo Motor Driver

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60312424-23c2b480-9910-11e9-824e-7fb36213dd65.JPG" height=128/>

1. Connect channel ``0`` on the servo driver to channel ``S1`` on the multiplexer

    > Pay attention to the orientation of the cable for these steps!
    
2. Connect channel ``1`` on the servo driver to channel ``S2`` on the multiplexer

### Step 3 - Jetson Nano Developer Kit

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60313003-4d7cdb00-9912-11e9-98cb-5890120a7949.JPG" height=128/>

1. Connect channel ``3`` on the RC receiver to ``SEL`` on the multiplexer
2. Connect channel ``2`` on the RC receiver to ``M2`` on the multiplexer
3. Connect channel ``1`` on the RC receiver to ``M1`` on the multiplexer

### Step 4 - Camera

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60314883-1bbb4280-9919-11e9-9f76-c561c9de9cb2.JPG" height=128/>

1. Connect the servo to ``OUT1`` on the multiplexer
2. Connect the ESC to ``OUT2`` on the multiplexer

### Step 5 - Wifi antennas

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60314883-1bbb4280-9919-11e9-9f76-c561c9de9cb2.JPG" height=128/>

1. Connect the servo to ``OUT1`` on the multiplexer
2. Connect the ESC to ``OUT2`` on the multiplexer

## Phase 3 - Wiring

### Step 1 - Car to RC Servo Mux

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60316400-2d074d80-991f-11e9-8f4c-49cbf84b3fb8.JPG" height=128/>

1. Attach ESC to the base plate as indicated
    > Notice the two slots on the base plate for the ESC
2. Press down firmly to secure the ESC

### Step 2 - RC Servo Mux to RX

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60316395-2d074d80-991f-11e9-80dc-63c819b76963.JPG" height=128/>

1. Attach the RC receiver to the base plate as indicated
2. Press down firmly to secure the RC receiver

### Step 3 - RC Servo Mux to Servo Motor Driver

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60317621-bcfbc600-9924-11e9-9cb5-af886100dd48.JPG" height=128/>

1. Remove the 4 screws indicated to expose holes used to mount the base plate

### Step 4 - Servo Motor Driver to Jetson

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60317630-bd945c80-9924-11e9-8139-5d7f5b8ad6a9.JPG" height=128/>

1. Select 4 ``M3x20mm standoffs``, 2 ``M2x38mm`` screws and 2 ``M2x30mm`` screws

2. Attach the base plate to the RC car chassis as indicated
3. Fasten the base plate using a hex screwdriver

### Step 5 - Jetson to Camera

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60318103-976fbc00-9926-11e9-90fc-d17feb20796e.JPG" height=128/>

> If the servo cable is not long enough to reach around the base plate, please route it as follows

1. Remove the servo cable from ``OUT1`` on the multiplexer that we attached previously
2. Route the servo wire through the slot base plate as indicated
3. Reconnect the servo cable to ``OUT1`` on the multiplexer

### Step 6 - Wi-fi card to Jetson

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60318997-d9e6c800-9929-11e9-8606-c1f020710518.JPG" height=128/>

1. Select 10 of the ``M2x6mm`` screws
2. Fasten the multiplexer to the base plate
3. Fasten the servo driver to the base plate
4. Fasten the Jetson Nano to the base plate

### Step 7 - Wi-fi antennas to Wi-fi card

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60319810-87f37180-992c-11e9-87a5-745b7bb57a13.JPG" height=128/>

1. Attach the two antennas to the WiFi card
2. Remove the Jetson Nano module from the developer kit board as indicated
3. Remove the M2 connector securing screw on the developer kit base board
4. Insert the WiFi card into the M2 connector slot
5. Reattach the screw to secure the WiFi card
6. Reattach the Jetson Nano module to the developer kit board

### Step 8 - USB Battery to Jetson

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60320486-b4a88880-992e-11e9-93ad-65ea2f051572.JPG" height=128/>

1. Attach the camera to the Jetson Nano developer kit as indicated
    > Be careful when loosing the camera connector to not break it
2. Attach the camera mount to the base plate using 4 ``M2x6mm`` screws
3. Attach the camera to the camera mount using 4 ``M2x6mm`` screws

## Phase 4 - Final Assembly

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60320486-b4a88880-992e-11e9-93ad-65ea2f051572.JPG" height=128/>

1. Attach the camera to the Jetson Nano developer kit as indicated
    > Be careful when loosing the camera connector to not break it
2. Attach the camera mount to the base plate using 4 ``M2x6mm`` screws
3. Attach the camera to the camera mount using 4 ``M2x6mm`` screws


## Hardware setup complete!

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60377764-33a0ce00-99ce-11e9-8aa4-688d0a05dc01.JPG" height=256/>

## Next

Next, follow the [software setup](../software_setup.md).
