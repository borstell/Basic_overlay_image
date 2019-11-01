# Basic_overlay_image
Create ghost overlay image from two separate images

Based on a snippet of code from [SSLD-images](https://github.com/borstell/SSLD-images). Creates an overlay image from two separate images. Requires [ImageMagick](https://imagemagick.org/index.php).

Run in the command line using e.g. two `.jpg` images (other formats work too):

```
python3 make_overlay.py image1.jpg,image2.jpg
```

The output will share the name with the first image of the input, with an added suffix "`_overlay`" before the file extension – i.e. `image1_overlay.jpg` based on the above example.

![image1](https://raw.githubusercontent.com/borstell/Basic_overlay_image/master/kofta_a.jpg)
+
![image2](https://raw.githubusercontent.com/borstell/Basic_overlay_image/master/kofta_b.jpg)
-->
![output](https://raw.githubusercontent.com/borstell/Basic_overlay_image/master/kofta_overlay.jpg)
