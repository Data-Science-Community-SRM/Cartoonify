<p align="center">
<a href="https://dscommunity.in">
	<img src="https://github.com/Data-Science-Community-SRM/template/blob/master/Header.png?raw=true" width=80%/>
</a>
	<h2 align="center"> Cartoonify </h2>
	<h4 align="center"> 
	As you might know, sketching or creating a cartoon doesn’t always need to be done manually. Nowadays, many apps can turn your photos into cartoons. But what if I tell you, that you can create your own effect with few lines of code? Yes, Open CV as you know (or even if you don’t) is a very powerful tool with immense possibilities. It can be used to recognize objects, detect, and produce high-resolution images. In this project, we will show you how to give a cartoon-effect to an image in Python by utilizing OpenCV.</h4>
</p>

---
[![DOCS](https://img.shields.io/badge/Documentation-see%20docs-green?style=flat-square&logo=appveyor)](https://github.com/Data-Science-Community-SRM/cartoonify/blob/master/README.md) 
  [![UI ](https://img.shields.io/badge/User%20Interface-Link%20to%20UI-orange?style=flat-square&logo=appveyor)](https://github.com/Data-Science-Community-SRM/cartoonify/blob/master/images/discord%20preview.png)


## Preview
# Bilateral Filter
 Filtering is perhaps the most fundamental operation of image processing and computer vision. Bilateral Filter helps in smoothing and reducing all the noise from our image and also preserve the edges at the same time unlike gaussian blur. The weight is based on the Euclidean distance of pixels and also on radiometric differences such as color intensity, range etc.
 This is our image:
<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/cartoonify/blob/anushka/images/taj.jpg" width="500" height="300">
</p>
Image after Bilateral Filter
<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/cartoonify/blob/anushka/images/taj_bilateral.jpg" width="500" height="300">
</p>


# Pencil Sketch Filter
Pencil Sketch converts our image into an image which appears to be sketched by pencil. So in order to apply Pencil sketch, we first use grayscale and gaussian Blur on our image and for the final sketched image, we divide the original grayscale image with the blurred grayscale image. Dividing the image gives us a ratio of change between each pixel of two images. The stronger the blurry effects, the more the value of each pixel changes with respect to its origin and hence, it gives us sharper pencil sketch.
Below is a pictorial illustration.
Here is the original picture:
<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/cartoonify/blob/master/images/scenery.PNG" width="500" height="300">
</p>
Here is the picture after pencil sketch
<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/cartoonify/blob/master/images/pencil%20sketch.PNG" width="500" height="300">
</p>

# Pencil Edge Filter
Pencil Edges filter creates a new image that contains only significant edges and white background. After grayscale and gaussian blur, we apply Laplacian filter to detect the edges.
Here is the original picture:
<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/cartoonify/blob/master/images/scenery.PNG" width="500" height="300">
</p>
Here is the picture after pencil edge
<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/cartoonify/blob/master/images/pencil%20edge.PNG" width="500" height="300">
</p>

# Detail Enhancement Filter
Enhancing image details without introducing artifacts has been attracting much attention in image processing community. Detail Enhancement filter gives a cartoon effect by sharpening the image, soothing the colours and enhancing the edges. First we convert the image into a grayscale image and then instead of using gaussian blur, median blur is applied. Adaptive threshold is then applied to detect the edges of the image. Finally, we use the result of adaptive threshold as a mask and then merge the result of detail enhancement based on the value of the mask to create a sharp effect with a well defined edge.

The result:
<p align="center">
<img src = "https://user-images.githubusercontent.com/64346030/109815435-a3606500-7c55-11eb-8cf2-47af016551de.png" width="500" height="300">
</p>
Image after Detail Enhancement Filter
<p align="center">
<img src = "https://user-images.githubusercontent.com/64346030/109815427-a196a180-7c55-11eb-97c7-cc8c70fbd769.png" width="500" height="300">
</p>

# Discord Bot

This Project has been deployed as a bot through Discord. The bot has be coded with Python and the bot runs on Repl.it server, Repl.it is an online code editor and has its own cloud storage for storing your Repositories which is really very helpful.  

### Command's for the Bot :
- The commands for the bot precede with ` $ `  sign and commands can be tagged with the `@username` of the person in the server.
- ` $ filter1 ` Returns the Pencil Sketch of the profile picture of the user.
- ` $ filter2 ` Returns the B/W Detail Enhanced profile picture of the user.
- ` $ filter1 @username ` Returns the Pencil Sketch of the profile picture of the tagged person.
- ` $ filter2 @username ` Returns the B/W Detail Enhanced profile picture of the tagged person.

### Preview
<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/cartoonify/blob/d33d2f5fd7badb62c2eb289385bbfd089eeb7daa/images/discord%20preview.png" width="500" height="700">
</p>


<br>


# Instructions to Run

* Pre-requisites:
    - [ ] Python to understand the working of Filters.
    - [ ] Discord Bot Commands.
* Directions to Install: 
	- [ ] Download the ZIP file of this repository to your local system.
	- [ ] Create a repository in repl.it
	- [ ] Insert the bot commands which are present in [main.py ](https://github.com/Data-Science-Community-SRM/cartoonify/blob/ae1dcad5bfb0926b34355685ac9e181d195056c7/main.py) file.
	- [ ] Setup the flask app to keep the bot awake.
* Directions to Execute:
	- [ ]   Run the Repository on repl.it and setup [Up Time Robot](https://uptimerobot.com/), To keep the bot awake when you are away.
	- [ ] Add the bot to your discord server.
	- [ ] Now you can execute your commands.

## Contributors

<table>
<tr align="center">


<td>

Anushka Garg

<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/cartoonify/blob/anushka/images/Anushka.jpeg" width="200" height="200">
</p>
<p align="center">
<a href = "https://github.com/anushkagarg5653"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/anushka-garg-b6759318a/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>


<td>

Ankita Kokkera

<p align="center">
<img src = "https://user-images.githubusercontent.com/64346030/109815968-37cac780-7c56-11eb-862f-408338278912.jpeg"  width="200" height="200" alt="Ankita">
</p>
<p align="center">
<a href = "https://github.com/ankitasankars"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/ankita-k-4b943611a/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>

<td>

Rakesh J

<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/cartoonify/blob/master/images/Rakesh.jpg"  width="200" height="200" alt="Rakesh">
</p>
<p align="center">
<a href = "https://github.com/stagnito"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/rakesh-j-35174618b">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>

<td>

Rusali Saha

<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/cartoonify/blob/master/images/Rusali.png"  width="150" height="200" alt="Rusali">
</p>
<p align="center">
<a href = "https://github.com/person3"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/person3">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>
</tr>
  </table>
  
## License
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

<p align="center">
	Made with :heart: by <a href="https://dscommunity.in">DS Community SRM</a>
</p>

