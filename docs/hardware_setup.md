# JetRacer - Hardware Setup

## Tools

## Phase 1 - Car disassembly
### Step 1 - Remove shroud from car

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60310435-c165b600-9907-11e9-858b-238e801b11ab.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60310436-c165b600-9907-11e9-88d1-fd009d015eda.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60310437-c1fe4c80-9907-11e9-8862-f0249a61c680.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60310439-c1fe4c80-9907-11e9-8495-990fa6ae926e.JPG" height=128/>

1. Remove the 4 pins securing the shroud

2. Remove the shroud from the chassis

### Step 2 - Remove ESC and RC receiver from car

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60311224-37b7e780-990b-11e9-92b1-04fd1bc78b41.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60311225-37b7e780-990b-11e9-9738-aab32effaf32.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60311226-37b7e780-990b-11e9-9454-9f54187a61af.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60311228-38507e00-990b-11e9-9bb5-53256784ea85.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60311229-38507e00-990b-11e9-890b-3123dcdf4cea.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60311231-38507e00-990b-11e9-832d-fdb3b696f336.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60311233-38e91480-990b-11e9-86be-5b01f8e4a9d2.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60311234-38e91480-990b-11e9-9277-3f71895a40c7.JPG" height=128/>

1. Remove the two screws securing the electronics hub to the chassis

2. Pry the electronics hub from the chassis
3. Remove the ESC and RC receiver from the electronics hub
4. Disconnect the two servo cables from the RC receiver
5. Remove the foam adhesive from the RC receiver

## Phase 2 - Car wiring
### Step 1 - Connect Jetson to servo driver

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60311869-ec530880-990d-11e9-9b9b-efabfcef251e.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60315002-a56b1000-9919-11e9-8a53-2d941cc1b139.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60311872-eceb9f00-990d-11e9-8770-3021aa6b11b3.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60311873-eceb9f00-990d-11e9-9872-cae74856b125.JPG" height=128/>

1. Select 4 female-to-female jumper cables from the bundle

2. Attach the jumpers to the servo driver pins ``VCC`` (white), ``SDA`` (gray), ``SCL`` (purple) and ``GND`` (black)
3. Attach the other end of the jumpers to the Jetson Nano pins ``3.3V`` (white), ``3`` (gray), ``5`` (purple) and ``GND`` (black)

### Step 2 - Connect servo driver to multiplexer

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60312424-23c2b480-9910-11e9-824e-7fb36213dd65.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60312425-23c2b480-9910-11e9-94af-ccc7b5d9f07a.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60312427-245b4b00-9910-11e9-8781-ba4ec20c0012.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60312429-245b4b00-9910-11e9-84d5-f3ccf10fcf86.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60312430-245b4b00-9910-11e9-8244-22c40b3b5851.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60312431-245b4b00-9910-11e9-8a6d-f6f1ae954ab2.JPG" height=128/>

1. Connect channel ``0`` on the servo driver to channel ``S1`` on the multiplexer

    > Pay attention to the orientation of the cable for these steps!
    
2. Connect channel ``1`` on the servo driver to channel ``S2`` on the multiplexer

### Step 3 - Connect RC receiver to multiplexer

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60313003-4d7cdb00-9912-11e9-98cb-5890120a7949.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60313004-4d7cdb00-9912-11e9-90bd-2fbe3bee0a05.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60313006-4d7cdb00-9912-11e9-86a9-bbc0dc62b94f.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60313007-4d7cdb00-9912-11e9-84e3-03944f236987.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60313008-4d7cdb00-9912-11e9-9894-eac89f324822.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60313009-4e157180-9912-11e9-984a-afbf62bbb15d.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60313010-4e157180-9912-11e9-858c-6a463433f53f.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60313012-4e157180-9912-11e9-9743-5647a3c5599b.JPG" height=128/>

1. Connect channel ``3`` on the RC receiver to ``SEL`` on the multiplexer

2. Connect channel ``2`` on the RC receiver to ``M2`` on the multiplexer
3. Connect channel ``1`` on the RC receiver to ``M1`` on the multiplexer

### Step 4 - Connect multiplexer to ESC and servo

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60314883-1bbb4280-9919-11e9-9f76-c561c9de9cb2.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60314885-1bbb4280-9919-11e9-8eb2-5c1f97b6b6dc.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60314884-1bbb4280-9919-11e9-8c4f-d43a5441fbe7.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60314887-1c53d900-9919-11e9-9d48-3770831164c8.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60314888-1c53d900-9919-11e9-8c84-4a91f0e727af.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60314889-1c53d900-9919-11e9-97aa-9015e4e94aca.JPG" height=128/>

1. Connect the servo to ``OUT1`` on the multiplexer

2. Connect the ESC to ``OUT2`` on the multiplexer

## Phase 3 - Car assembly

### Step 1 - Mount ESC to base plate

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60316400-2d074d80-991f-11e9-8f4c-49cbf84b3fb8.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60316401-2d074d80-991f-11e9-8f3b-82714cfef58f.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60316392-2c6eb700-991f-11e9-89cc-3f9babc37a17.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60316393-2c6eb700-991f-11e9-94e5-4ebe4b2582fd.JPG" height=128/>

1. Attach ESC to the base plate as indicated

    > Notice the two slots on the base plate for the ESC
    
2. Press down firmly to secure the ESC

### Step 2 - Mount RC receiver to base plate

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60316395-2d074d80-991f-11e9-80dc-63c819b76963.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60316445-5627de00-991f-11e9-8408-35b9c1fec8da.JPG" height=128/>

1. Attach the RC receiver to the base plate as indicated

2. Press down firmly to secure the RC receiver

### Step 3 - Expose screw holes used to mount base plate

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60317621-bcfbc600-9924-11e9-9cb5-af886100dd48.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60317622-bcfbc600-9924-11e9-8893-3c46e21ec259.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60317624-bcfbc600-9924-11e9-9b5c-54b6eb311153.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60317625-bcfbc600-9924-11e9-9f2b-830cce4cadb3.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60317628-bd945c80-9924-11e9-9848-36492cc190cd.JPG" height=128/>

1. Remove the 4 screws indicated to expose holes used to mount the base plate

### Step 4 - Mount base plate to RC car

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60317630-bd945c80-9924-11e9-8139-5d7f5b8ad6a9.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60317631-bd945c80-9924-11e9-9eb0-c755fdb6d83f.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60317632-be2cf300-9924-11e9-8bd0-7b05f6f0ef2b.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60317633-be2cf300-9924-11e9-853a-59a2e0875410.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60317634-be2cf300-9924-11e9-83eb-3313d97d535e.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60317610-bc632f80-9924-11e9-9290-9b6ba270a515.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60317611-bc632f80-9924-11e9-94e2-1bacf358ebe4.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60317613-bc632f80-9924-11e9-89ab-a7d3dfec94d7.JPG" height=128/>

1. Select 4 ``M3x20mm standoffs``, 2 ``M2x38mm`` screws and 2 ``M2x30mm`` screws

2. Attach the base plate to the RC car chassis as indicated
3. Fasten the base plate using a hex screwdriver

### Step 5 - Route servo motor wire through base plate

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60318103-976fbc00-9926-11e9-90fc-d17feb20796e.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60318104-976fbc00-9926-11e9-9dc1-9b2f5c9efb0f.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60317768-56c37300-9925-11e9-9ce2-fb43b7a70c4a.JPG" height=128/>

> If the servo cable is not long enough to reach around the base plate, please route it as follows

1. Remove the servo cable from ``OUT1`` on the multiplexer that we attached previously

2. Route the servo wire through the slot base plate as indicated
3. Reconnect the servo cable to ``OUT1`` on the multiplexer

### Step 6 - Mount components to base plate

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60318997-d9e6c800-9929-11e9-8606-c1f020710518.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60318999-da7f5e80-9929-11e9-921b-c63e1bfc1f9e.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60319310-d0aa2b00-992a-11e9-95a0-4e00e010acf9.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60319312-d0aa2b00-992a-11e9-9631-d5c688ea67b7.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60319370-0e0eb880-992b-11e9-8854-1220bd1e806b.JPG" height=128/>

1. Select 10 of the ``M2x6mm`` screws

2. Fasten the multiplexer to the base plate
3. Fasten the servo driver to the base plate
4. Fasten the Jetson Nano to the base plate

### Step 7 - Connect WiFi card

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60319810-87f37180-992c-11e9-87a5-745b7bb57a13.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60319811-888c0800-992c-11e9-9b39-01b0df050d69.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60319812-888c0800-992c-11e9-8570-e6991fc1ce4d.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60319813-888c0800-992c-11e9-9280-de99940abd95.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60319815-888c0800-992c-11e9-9884-1bab46691048.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60319816-89249e80-992c-11e9-8c5b-7287c798221c.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60319817-89249e80-992c-11e9-98d8-0628f0b53d43.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60319818-89249e80-992c-11e9-8411-96abda0a94e7.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60319819-89249e80-992c-11e9-8cee-9d53e81df454.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60319821-89249e80-992c-11e9-8374-ee5d0ce24fe5.JPG" height=128/>

1. Attach the two antennas to the WiFi card

2. Remove the Jetson Nano module from the developer kit board as indicated
3. Remove the M2 connector securing screw on the developer kit base board
4. Insert the WiFi card into the M2 connector slot
5. Reattach the screw to secure the WiFi card
6. Reattach the Jetson Nano module to the developer kit board

### Step 8 - Connect camera

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60320486-b4a88880-992e-11e9-93ad-65ea2f051572.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60320259-07ce0b80-992e-11e9-82ae-bf8b7fa09b85.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60320260-07ce0b80-992e-11e9-92f7-fd6e4c83d264.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60320788-a3ac4700-992f-11e9-99d9-1dba9f1897f1.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60320789-a3ac4700-992f-11e9-8280-c689d609c18b.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60320790-a3ac4700-992f-11e9-9afc-f48c9f4a176e.JPG" height=128/>

1. Attach the camera to the Jetson Nano developer kit as indicated

    > Be careful when loosing the camera connector to not break it
    
2. Attach the camera mount to the base plate using 4 ``M2x6mm`` screws
3. Attach the camera to the camera mount using 4 ``M2x6mm`` screws

### Step 9 - Mount USB battery pack

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60321112-b1ae9780-9930-11e9-8f84-24cc304af5f9.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60321113-b1ae9780-9930-11e9-9462-685e0d9e9464.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60321114-b1ae9780-9930-11e9-80bf-84522d1ce708.JPG" height=128/>

1. Attach the USB battery pack to the underside of the base plate as indicated

### Step 10 - Attach USB barrel plug

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60322349-14556280-9934-11e9-8c25-4394eddda4e2.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60322350-14556280-9934-11e9-8c31-70982af7e08e.JPG" height=128/>

1. Attach the 2 pin jumper to ``J48`` on the Jetson Nano developer kit to enable barrel plug power

2. Insert the barrel plug into the Jetson Nano developer kit

    > Before powering on, you'll need to follow the [software setup](software_setup.md) to configure the SD card
    
## Phase 4 - RC transmitter modification

## Step 1 - Dissasmble radio

<a></a>
<img src="https://user-images.githubusercontent.com/25759564/60376010-fc77f000-99c0-11e9-9e2a-478a5da88062.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60376011-fc77f000-99c0-11e9-827f-77e4df18516f.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60376014-fda91d00-99c0-11e9-8a45-ca3ef0f4831c.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60376015-fe41b380-99c0-11e9-9915-d31b6d32e692.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60376016-fe41b380-99c0-11e9-9f2f-892026211c67.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60376019-feda4a00-99c0-11e9-9aa9-89d6ea78532b.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60376020-ff72e080-99c0-11e9-907e-1ccd5c805a20.JPG" height=128/>
<img src="https://user-images.githubusercontent.com/25759564/60376023-ff72e080-99c0-11e9-8bad-3bc2d4577207.JPG" height=128/>

1. Remove the 5 screws securing radio halves with a phillips screwdriver

2. Peel off the radio stick joining the two halves
3. Place the radio sticker on one half of the radio
4. Remove the battery cover
5. Separate the radio into halves

## Step 2 - Drill hole in RC transmitter for manual override switch

<a></a>
<img src="" height=128/>
<img src="" height=128/>
<img src="" height=128/>
<img src="" height=128/>
<img src="" height=128/>
<img src="" height=128/>
<img src="" height=128/>
<img src="" height=128/>
<img src="" height=128/>

## Step 3 - 
