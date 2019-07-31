# JetRacer

<img src="https://user-images.githubusercontent.com/25759564/62127658-741e9080-b287-11e9-8ab9-f4e7e31404b1.png" height=256>

JetRacer is an autonomous AI racecar using NVIDIA Jetson Nano.  With JetRacer you will

* Go fast - Optimize for high framerates to move at high speeds

* Have fun - Follow examples and program interactively from your web browser

By building and experimenting with JetRacer you will create fast AI pipelines and push the boundaries of speed.

To get started, follow the [setup](#setup) below.

## Setup

To get started with JetRacer, follow these steps

1. Order parts from the bill of materials

    - [Latrax version](docs/latrax/bill_of_materials.md)
    - [Tamiya version](docs/tamiya/bill_of_materials.md)

2. Follow the hardware setup

    - [Latrax version](docs/latrax/hardware_setup.md)
    - [Tamiya version](docs/tamiya/hardware_setup.md)
3. Follow the [software setup](docs/software_setup.md)
4. Run through the [examples](docs/examples.md)

## Examples

### Example 1 - Basic motion

In this example you'll learn to progam JetRacer programatically from your web browser.  Learn more in the [examples](docs/examples.md) documentation.

<img src="https://user-images.githubusercontent.com/4212806/60383497-68d90a80-9a26-11e9-9a18-778b7d3a3221.gif" height=300/>

### Example 2 - Road following

In this example, you'll teach JetRacer how to follow a road using AI.  After training the neural network using the [interactive training notebook](notebooks/interactive_regression.ipynb), you'll optimize the model using NVIDIA TensorRT and deploy for a live demo. Learn more in the [examples](docs/examples.md).

<img src="https://user-images.githubusercontent.com/4212806/60383389-bd7b8600-9a24-11e9-9f64-926e5edb52cc.gif" height=300/>

## See also

* [JetBot](http://github.com/NVIDIA-AI-IOT/jetbot) - An educational AI robot based on NVIDIA Jetson Nano

* [JetCam](http://github.com/NVIDIA-AI-IOT/jetcam) - An easy to use Python camera interface for NVIDIA Jetson
* [JetCard](http://github.com/NVIDIA-AI-IOT/jetcard) - An SD card image for web programming AI projects with NVIDIA Jetson Nano
* [torch2trt](http://github.com/NVIDIA-AI-IOT/torch2trt) - An easy to use PyTorch to TensorRT converter
