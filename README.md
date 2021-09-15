# JetRacer

> 6/01/2021 - JetPack 4.5.1 based image is updated. It is pre-configured for JetRacer. Detail [here](https://github.com/NVIDIA-AI-IOT/jetracer/blob/master/docs/software_setup.md#latest-release--but-not-yet-fully-verified--).

<img src="https://user-images.githubusercontent.com/4212806/67442981-ce459e00-f5b7-11e9-9c8a-14ab360decb8.gif" height=256>

JetRacer is an autonomous AI racecar using NVIDIA Jetson Nano.  With JetRacer you will

* Go fast - Optimize for high framerates to move at high speeds

* Have fun - Follow examples and program interactively from your web browser

By building and experimenting with JetRacer you will create fast AI pipelines and push the boundaries of speed.

To get started, follow the [setup](#setup) below.

## Cars

There are two different JetRacer cars that you can build.  They differ primarily in size and speed.  Which one to pick depends on your use case

|  Latrax Rally | Tamiya TT02 |
|--------------|---------------|
| <img src="https://user-images.githubusercontent.com/25759564/67250038-b1c22e00-f41e-11e9-82d2-bbb17526310b.jpg" width=256>  | <img src="https://user-images.githubusercontent.com/25759564/67250039-b1c22e00-f41e-11e9-931f-98c1729550d0.jpg" width=320>  | 
| 1/18th scale |  1/10th scale |
| Moderate Speed  |  High Speed  |
| ~$400 total build cost | ~$600 total build cost |
| Compact and portable |  Large and easy to modify |
| Soldering required |  No soldering required  |
| Base car pre-assembled | Base car assembly required |

If you have any questions, please reach out by [creating an issue](../..//issues).


## Examples

JetRacer comes with a couple examples to get you up and running.  The examples are in the format of Jupyter Notebooks, which are interactive documents which combine text, code, and visualization.  Once you've completed the notebooks, start tweaking them to create your own racing software!

### Example 1 - Basic motion

In this example you'll learn to progam JetRacer programatically from your web browser.  Learn more in the [examples](docs/examples.md) documentation.

<img src="https://user-images.githubusercontent.com/4212806/60383497-68d90a80-9a26-11e9-9a18-778b7d3a3221.gif" height=300/>

### Example 2 - Road following

In this example, you'll teach JetRacer how to follow a road using AI.  After training the neural network using the [interactive training notebook](notebooks/interactive_regression.ipynb), you'll optimize the model using NVIDIA TensorRT and deploy for a live demo. Learn more in the [examples](docs/examples.md).

<img src="https://user-images.githubusercontent.com/4212806/60383389-bd7b8600-9a24-11e9-9f64-926e5edb52cc.gif" height=300/>

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

## See also

* [JetBot](http://github.com/NVIDIA-AI-IOT/jetbot) - An educational AI robot based on NVIDIA Jetson Nano

* [JetCam](http://github.com/NVIDIA-AI-IOT/jetcam) - An easy to use Python camera interface for NVIDIA Jetson
* [JetCard](http://github.com/NVIDIA-AI-IOT/jetcard) - An SD card image for web programming AI projects with NVIDIA Jetson Nano
* [torch2trt](http://github.com/NVIDIA-AI-IOT/torch2trt) - An easy to use PyTorch to TensorRT converter
