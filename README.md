## Approaches in pose estimation  
Two common approaches are employed in estimating the poses of individuals in a given image.  

### 1️⃣ Top-down approaches  
The processing is done from low to high resolutions, follow the detection of the individual instances in the image first using a bounding box object detector and then focus on determining their poses.  

#### 🔥 Suffer from...  
1) If the detection of indiciduals fails, there is no possibility of recovering.
2) It is vulnerable when multiple individuals are nearby.
3) The computational cost depends on the number of people in the image.


### 2️⃣ Botton-up approaches  
The processing is done from high to low resolutions. It starts by localizing identity free semantic entities and then grouping them into person instance.  

#### 💡 Bottom-up approaches overcame 1) early commitment and showed detached run-tome complexity from the number of people in the image.  
🔥 But, bottom-up approaches face challenges in **grouping body parts when there is a large overlap between people.** 


<br/><br/>

## Tasks
I implemented some tasks...  
1) Draw pose landmarks and connection lines(image)
2) Draw pose landmarks and connection lines on webcam
3) Squat counting using pose landmarks

## Results  
<img src="https://github.com/gaerom/2D-Human-pose-estimation/assets/92725975/62aa41f3-3a8f-47b5-821c-64afb82a0757" alt="pose_result" width="150"/> ![result](https://github.com/gaerom/2D-Human-pose-estimation/assets/92725975/2d410210-ff98-4e93-8483-8dfd5178dbc2)
