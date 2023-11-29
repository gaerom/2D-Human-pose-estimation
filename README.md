# Human pose estimation  
## Approaches in pose estimation  
Two common approaches are employed in estimating the poses of individuals in a given image.  

### Top-down approaches  
The processing is done from low to high resolutions, follow the detection of the individual instances in the image first using a bounding box object detector and then focus on determining their poses.  

### 🔥 Suffer from...  
1) If the detection of indiciduals fails, there is no possibility of recovering.
2) It is vulnerable when multiple individuals are nearby.
3) The computational cost depends on the number of people in the image.


### Botton-up approaches  
The processing is done from high to low resolutions. It starts by localizing identity free semantic entities and then grouping them into person instance.  

### 💡 Bottom-up approaches overcame 1)early commitment and showed detached run-tome complexity from the number of people in the image.  
🔥 But, bottom-up approaches face challenges in **grouping body parts when there is a large overlap between people. **

