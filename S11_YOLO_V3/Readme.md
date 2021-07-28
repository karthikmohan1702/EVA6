## Contents

- [Objective](#objective)
- [Part 1](#part-1)
- [Part 2](#part-2) 
- [References](#references) 



## Objective

**Part 1 - OpenCV Yolo**

1. Run this code [OpenCV Yolo](https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/) on your laptop or Colab.
2. Take an image of yourself, holding another object which is there in COCO data set (search for COCO classes to learn). 
3. Run this image through the code above. 

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


## Part 1

**Opencv result**

- Jupyter Notebook to run the model is placed [here](https://github.com/karthikmohan1702/EVA6/blob/main/S11_YOLO_V3/yolo_opencv/)

![yolo_opencv_op](https://user-images.githubusercontent.com/47082769/127197197-255202ee-4440-4250-8ee3-5b3e6bf1db9e.png)


## Part 2

- YoloV3 model istrained on the Industrial equipment dataset classes:
      - Hardhat
      - Boots
      - Mask
      - Vest
- Jupyter Notebook to run the model is placed [here](https://github.com/karthikmohan1702/EVA6/blob/main/S11_YOLO_V3/yolov3/)
- YoloV3 was implemented on the video & its output is placed [here](https://github.com/karthikmohan1702/EVA6/blob/main/S11_YOLO_V3/yolov3/)
- Also result is uploaded on [Youtube](https://www.youtube.com/watch?v=cSzYJinIFCE)
- Inference on image

![image](https://user-images.githubusercontent.com/47082769/127312942-64f1196f-761c-44d6-8a48-50e701116f50.png)

![image](https://user-images.githubusercontent.com/47082769/127312956-93f7ee26-7326-42df-bcee-9c8d5b08e958.png)

![image](https://user-images.githubusercontent.com/47082769/127312970-efaeb08e-160f-4c5d-a697-581c0100ab70.png)

![image](https://user-images.githubusercontent.com/47082769/127312987-d1e34170-4517-46e3-807c-8adb56138dcb.png)

![image](https://user-images.githubusercontent.com/47082769/127313048-e7510904-34b3-42ad-99ad-2df8b0538aa8.png)

![image](https://user-images.githubusercontent.com/47082769/127313068-a8593fe6-b3a1-4db8-891d-8d6942bfa3c9.png)

![image](https://user-images.githubusercontent.com/47082769/127313091-7be8a055-da65-4e54-8ec6-e36977641050.png)

![image](https://user-images.githubusercontent.com/47082769/127313115-42555871-6679-4d9d-a110-f94a91e8c5bf.png)

![image](https://user-images.githubusercontent.com/47082769/127313140-3cdcfa40-07b8-4b57-8cf8-bec116ce7b7a.png)

![image](https://user-images.githubusercontent.com/47082769/127313160-7028b525-8772-44fa-853d-adca39fdb8a2.png)

![image](https://user-images.githubusercontent.com/47082769/127313176-63261da9-2790-4fa5-b589-774a1da3aed6.png)

![image](https://user-images.githubusercontent.com/47082769/127313182-ca38f879-2dcb-4b63-9909-633967cbb678.png)

![image](https://user-images.githubusercontent.com/47082769/127313194-d05fa0fd-3a45-41df-ae67-e7ca45e9b50c.png)

![image](https://user-images.githubusercontent.com/47082769/127313203-7c7777eb-7344-40cb-a2f9-4563f8a00ac8.png)

![image](https://user-images.githubusercontent.com/47082769/127313216-fa075b63-5136-41b5-ac38-b7175d6913f0.png)



## References

- https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/
- https://github.com/theschoolofai/YoloV3
- https://drive.google.com/file/d/1sVSAJgmOhZk6UG7EzmlRjXfkzPxmpmLy/view
- https://en.wikibooks.org/wiki/FFMPEG_An_Intermediate_Guide/image_sequence


