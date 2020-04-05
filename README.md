# Vein Detection System
  
### What exactly?
  
A prototype of a system that can be used to detect a persons vein and the point of entry of the needle. The code in this repository has the the software aspect of the project. However, the project was implemented on a rasberry pi with infrared lights as a stand alone system.
  
### Okay... But do we need this?
  
The insertion of a needle into the vein is termed as Venipuncture. It is the most commonly performed invasive routine. It establishes access to the venous blood stream and is performed for various reasons(injections, blood retrieval, saline, etc)
  
But the problem lies in the fact that it's not straightforward. The process is carried out by a trained person using touch and sight. The person check the vein and then inserts the needle. But what if my veins are not visible? What if i have tattoos all over my arm? And with the high number of needle insertion on a daily basis, this small problem becomes huge.
  
First stick failure rates, the rate at which a needle is not inserted correctly, have been estimated to range from 20% to 33%. In children or elderly, it is as high as 50-70%. Multiple attempts have to be made just to get the needle inserted correctly.
  
  <insert image>
  
#### How serious is it?
  
The adverse effects fall under three classes
1. Vasovagal injuries: Sudden reflex stimulation of Vagus Nerve (~5%)
2. Pain and Bruising: Least serious, most common (~15% on average)
3. Nerve Damage: Potentially disabling (1 in 5000 approx.)

And with the huge population these numbers range in thousands on a daily basis.

### The Solution we came up with
  
An interesting property of Haemoglobin in blood is that it absorbs Infrared light. A property we leveraged upon. Using Near Field Infrared Light, we were able to take an image of the veins and process it to obtain the skeleton of the veins. These veins were identified by contouring. These contours were fed back to the video stream of the hand to show the Hand with veins on it.
  
The vein branches and a point of insertion is generally at the point of branching. This point is determined using KNN, the more dense points are considered as point of insertion.

### Flow of the System
  
  <insert image>
  
1. The user enhances the contrast of the image to suit the environment.  
2. An image is then captured of the hand, which is converted to grayscale and enhanced using CLAHE(Histogram equalization).  
3. The enhanced image is then Blurred using Median Blur to reduce the noise in the image.  
4. Adaptive thresholding methods are implemented (SIFT, SURF) to seperate the vein points from the image.  
5. The contours are extracted from the image which is the skeletal for the veins.  
6. This skeletal is superimposed on the video stream of the image to present the vein.

### Results of the experiment 
  
Several failed experiments are also provided in the repository. These helped in coming up with the improved implementation. Below is the result of the experiment on my hand! :D
  
  <image>
  
### Learning
  
This was a super fun project. Took a lot of timem effort and team work to get things done. My intial code burnt the first raspberry pi. But then I learnt my lesson, went online and did lessons on image processing and then implemted the working version of this project.

#### More to be update... Soon...
