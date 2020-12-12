# Visualize_PasVOC_on_images
This is a tool which can visualize coordinates of bounding box on .xml file under PasVOC type on images

You have to put all images on **JPEGImages** folder and all label files .xml on **Annotations** folder

The output of this tool are images with bounding boxes and class names

To get output, open cmd and type the following command:

```
python main.py -r <prepared folder> -s <output folder>
```

For example, I create a hcm03 folder:
* hcm03
  * JPEGImages
    * image1.jpg
    * image2.jpg
  * Annotations
    * image1.xml
    * image2.xml

And I want to save solved image on folder output
Run following command:

```
python main.py -r hcm03 -s output
```

## Input:
![Input](/hcm03/JPEGImages/000000193.jpg)

## Output:
![Output](/output/000000193.jpg)


