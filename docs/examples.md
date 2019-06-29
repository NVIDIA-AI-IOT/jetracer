# Examples

Follow these examples to get started with JetRacer

> Ensure JetRacer is connected to WiFi and you've note the IP address as in the [software setup](software_setup.md)

## Example 1 - Basic Motion

In this example we'll show how to control JetRacer programatically from a web browser.

1. Navigate to ``http://<jetson_ip_address>:8888``

2. Sign in with the default password ``jetson``
3. Browse to the folder ``~/jetracer/notebooks`` in the Jupyter Lab file browser
4. Run through the notebook ``basic_motion.ipynb``

## Example 2 - Road Following

### Step 1 - Open the interactive trainer

1. Navigate to ``http://<jetson_ip_address>:8888``

2. Sign in with the default password ``jetson``
3. Browse to the folder ``~/jetracer/notebooks`` in the Jupyter Lab file browser
4. Open the notebook ``interactive_regression.ipynb``

### Step 2 - Run the trainer


>  You may want to use ``5W`` mode to prevent the Jetson Nano from drawing to much current and shutting down. Try opening a terminal and entering ``sudo nvpmodel -m1``.

1. In the cell *Task Definition* set ``TASK = 'road_following'`` to set the task name

2. Also set ``CATEGORIES = ['apex']`` to set the class names of the xy target category
3. Execute all of the remaining cells
4. Place the car in different positions, offsets and orientations along the track
5. Imagine the ideal path the car would follow in these positions overlaid on the camera feed
6. Click on the live camera feed as far along that ideal path as possible, such that the robot would not exit the track or collide with an object
7. Repeat this many times (say 50 to start)
8. Train the model for several epochs (say 10 to start) and see how the model performs
9. Iterate!  Try training a model, visualize the output in the live demo, find scenarios where the model is inaccurate and add data for those points, train again...
10. When you want to demo the model, save it to the path ``road_following_model.pth`` and restart the ``interactive_regression.ipynb`` notebook

### Step 3 - Run optimized live demo

1. Open and follow the notebook ``road_following.ipynb``
