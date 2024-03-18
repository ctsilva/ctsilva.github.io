# Final Project

### Description of StreetAware dataset

While researchers try to better understand the dynamics of urban environemnts, novel methods and datasets 

Description of StreetAware

[StreetAware](https://drive.google.com/drive/u/1/folders/1BPtiIF8gBOoZANAGkwDjJUYakpCUYHM1)

### Project suggestions:

1. **Spatial People ReID**: Person re-identification (Re-ID) is focused on identifying a specific person across various cameras. This can be extremely useful in 3D reconstruction scenarios to acquire the 3D geometry of particular assets from the scene. Recently, these techniques have benefited from advancements in deep learning to make more accurate predictions. One standard approach is extracting vector representations (embeddings) and performing pairwise comparisons to match correspondent people on different camera views. However, issues can arise throughout this process, and interactive visualization tools can help users understand the root causes of these issues. One example is how one would summarize the matches by looking at them in aggregated formats, such as in [Dendropmap](https://arxiv.org/pdf/2205.06935.pdf), where the users can visually inspect the quality of image clusters by looking at aggregated visualizations of image mosaics belonging to each cluster. The same happens in the [Embedding Projector](https://arxiv.org/abs/1611.05469) tool, which allows users to understand the structure of different embedding spaces. Applying such techniques to the StreetAware data is challenging as it represents a real-world situation.  

2. **Temporal Tracking**: Multi-object temporal tracking (MOT) aims to detect and track all the objects in a scene over time. It keeps a unique identifier for each object, allowing object matching across video frames. Recently, novel techniques such as BotSort, Bytetrack, and StrongSort have shown remarkable results. However, understanding failure patterns remains a challenge. While these techniques can work reasonably well on the StreetAware dataset, understanding details of under what conditions the models are more likely to fail is still an open question. For example, are trackings working as expected when the intersections are crowded? Does shadow influence the tracking of different pedestrians? Also, are trackings consistent when the bounding box of two pedestrians have a large overlap? These analyses can hugely benefit works trying to summarize trajectories to understand the temporal dynamics of urban environments. 

3. **Objects relationship** Novel open-vocabulary object detectors, such as SAM and Detic, can quickly discover almost any object in a given scene. Over time, these models can help us uncover the relationship between different objects, such as the likelihood of two objects appering together in a scene. Also, visualizing the distribution of objects appearing in the scene and understanding the correlation between them can lead domain experts to interesting insights. Moreover, leveraging such models to find accessibility-related situations in the data is also a potential and impactful application of these models. 

4. **Gait Estimation/Ability Estimation**

4. **Car Pose Estimation**


