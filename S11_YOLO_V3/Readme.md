## Contents

- [Objective](#objective)
- [Part1](#part1)
- [Part2](#part2)
- [Output](#output) 
- [References](#references) 



## Objective

**Part 1 - OpenCV Yolo**

1. Run this code [OpenCV Yolo](https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/) on your laptop or Colab.
2. Take an image of yourself, holding another object which is there in COCO data set (search for COCO classes to learn). 
3. Run this image through the code above. 
4. Upload the link to GitHub implementation of this
5. Upload the annotated image by YOLO. 

**Part 2 - Training Custom Dataset on Colab for YoloV3**

1. Refer to this Colab File: [LINK](https://colab.research.google.com/drive/1LbKkQf4hbIuiUHunLlvY-cc0d_sNcAgS)
2. Refer to this GitHub [Repo](https://github.com/theschoolofai/YoloV3)
3. Download this [dataset](https://drive.google.com/file/d/1sVSAJgmOhZk6UG7EzmlRjXfkzPxmpmLy/view). This was annotated by EVA5 Students. 
4. Collect and add 25 images for the following 4 classes into the dataset shared:
    
    - Class names are in custom.names file. 
    - You must follow exact rules to make sure that you can train the model. Steps are explained in the README.md file on github repo link above.
    - Once you add your additional 100 images, train the model
    
5. Once above steps are done:
    - Download a very small (~10-30sec) video from youtube which shows your classes. 
    - Use [ffmpeg](https://en.wikibooks.org/wiki/FFMPEG_An_Intermediate_Guide/image_sequence) to extract frames from the video. 
    - Upload on your drive (alternatively you could be doing all of this on your drive to save upload time)
    - Infer on these images using detect.py file. **Modify** detect.py file if your file names do not match the ones mentioned on GitHub. 
    - python detect.py --conf-three 0.3 --output output_folder_name
    - Use  ffmpeg  to convert the files in your output folder to video
    - Upload the video to YouTube. 
    - Also run the model on 16 images that you have collected (4 for each class)


## Output



## References


