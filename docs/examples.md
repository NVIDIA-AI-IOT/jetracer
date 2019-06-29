# Examples

Follow these examples to get started with JetRacer

> Ensure JetRacer is connected to WiFi and you've note the IP address as in the [software setup](software_setup.md)

## Example 1 - Basic Motion

In this example we'll show how to control JetRacer programatically from a web browser.

1. Navigate to ``http://<jetson_ip_address>:8888``

2. Sign in with the default password ``jetson``
3. Browse to the folder ``~/jetracer/notebooks`` in the Jupyter Lab file browser
4. Run through the notebook ``basic_motion.ipynb``

## Example 2 - Collision Avoidance

### Step 1 - Open the interactive trainer

1. Navigate to ``http://<jetson_ip_address>:8888``

2. Sign in with the default password ``jetson``
3. Browse to the folder ``~/jetracer/notebooks`` in the Jupyter Lab file browser
4. Open the notebook ``interactive_classification.ipynb``

### Step 2 - Run the trainer

1. In the cell *Task Definition* set ``TASK = 'collision_avoidance'`` to set the task name

2. Also set ``CATEGORIES = ['blocked', 'free']`` to set the class names of the classification task
2. Execute all of the remaining cells
2. Use the final widget to collect an image classification dataset for the categories ``blocked`` and ``free``.  Here are some tips

    * Label scenarios where you think it's safe for JetRacer to move forward as ``free``
    
    * Label scenarios where you think it's unsafe for JetRacer to move forward as ``blocked``
    * Collect about an equal number of ``blocked`` and ``free`` images
    * Vary the types of images by changing lighting, surfaces, angles of objects, etc.
    * Iterate!  Try training a model, visualize the output in the live demo, find scenarios where the model is weak and add data for those points, train again...


>  If the Jetson draws too much power during training and shuts down, you may want to use ``5W`` mode by opening a terminal and entering ``sudo nvpmodel -m1``.

## Example 2 - Object Following
