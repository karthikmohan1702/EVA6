## Contents

- [Objective](#objective)
- [DETR](#detr)
- [Encoder Decoder Architecture](#encoder-decoder-architecture)
- [Bipartite Loss](#bipartite-loss)
- [Object Queries](#object-queries)
- [Model monitoring metrics](#model-monitoring-metrics)
- [Model results](#model-results)
- [References](#references) 


### Objective

- Explain DETR
- Explain encoder-decoder architecture
- Explain bipartite loss, and why we need it
- Explain object queries
- Model results


### DETR

DETR(Detection Transformer) is an end to end object detection model that does object classification and localization i.e boundary box detection and also an important new approach to object detection and panoptic segmentation. It is a simple encoder-decoderTransformer with a novel loss function that allows us to formulate the complex object detection problem as a set prediction problem. It is very simple compared to other Transformer models used for vision

The architecture of DETR has three main components, which are a 

- CNN backbone to extract a compact feture representation 
- Encoder-decoder transformer
- Feed-Forward Networks.


![image](https://user-images.githubusercontent.com/47082769/129408138-9241e7fc-be06-444f-81af-2bb7dd1bdca9.png)



### Encoder Decoder Architecture

After the model flattens and supplements it with a positional encoding before passing it into a transformer encoder. A transformer decoder then takes as input a small fixed number(N) of learned positional embeddings, which we call object queries, and additionally attends to the encoder output. We pass each output embedding of the decoder to a shared feed forward network (FFN) that predicts either a detection (class and bounding box) or a ∅(no object) class.


![image](https://user-images.githubusercontent.com/47082769/129408447-d67b443e-8295-4105-b503-61e5f76fb1cc.png)


### Bipartite Loss

Unlike other object detection models label bounding boxes (or point, like methods in object as points) by matching multiple bounding boxes to one ground truth box, DETR is using bipartite matching, which is one-vs-one matching.
By performing one-vs-one matching, its able to significantly reduce low-quality predictions, and achieve eliminations of output reductions like NMS.


### Object Queries

An intuitive way of understanding the object queries is by imagining that each object query is a person. And each person can ask the, via attention, about a certain region of the image. So one object query will always ask about what is in the center of an image, and another will always ask about what is on the bottom left, and so on


### Model monitoring metrics

Model was trained for only **10 epochs**

1. Mean Average Precision (mAP)
![image](https://user-images.githubusercontent.com/47082769/129409703-662b732d-323b-4778-a6ce-9387d818e7d1.png)


2. Classification, Bounding box loss
![image](https://user-images.githubusercontent.com/47082769/129410236-a904b9b6-fc58-4e14-b818-6e17ea2a091d.png)


3. Class, Cardinality error
![image](https://user-images.githubusercontent.com/47082769/129410302-5055c3f3-6311-4056-8141-1e2454a0fd68.png)


### Model results

![image](https://user-images.githubusercontent.com/47082769/129409311-e6034a80-108b-4943-82d8-891606ad7add.png)

![image](https://user-images.githubusercontent.com/47082769/129409363-354c2024-005e-4655-bf92-bd827a3dfd89.png)


### References

- https://opensourcelibs.com/lib/finetune-detr
- https://colab.research.google.com/github/woctezuma/finetune-detr/blob/master/finetune_detr.ipynb
- https://arxiv.org/pdf/2005.12872.pdf
- https://medium.com/lsc-psd/detr-object-detection-with-transformer-a97104ea1723
- https://analyticsindiamag.com/how-to-detect-objects-with-detection-transformers/
- https://ai.facebook.com/blog/end-to-end-object-detection-with-transformers/
- https://medium.com/analytics-vidhya/end-to-end-object-detection-with-transformers-detr-by-facebook-ai-833f4086280a
- https://medium.com/swlh/object-detection-with-transformers-437217a3d62e
- https://www.cellstrat.com/2020/08/07/end-to-end-object-detection-with-transformers/




















