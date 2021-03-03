<p align="center">
<a href="https://dscommunity.in">
	<img src="https://github.com/Data-Science-Community-SRM/template/blob/master/Header.png?raw=true" width=80%/>
</a>
	<h2 align="center"> Cartoonify </h2>
	<h4 align="center"> < Insert Project Description Here > <h4>
</p>

---
[![DOCS](https://img.shields.io/badge/Documentation-see%20docs-green?style=flat-square&logo=appveyor)](INSERT_LINK_FOR_DOCS_HERE) 
  [![UI ](https://img.shields.io/badge/User%20Interface-Link%20to%20UI-orange?style=flat-square&logo=appveyor)](INSERT_UI_LINK_HERE)

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
<img src = "https://github.com/Data-Science-Community-SRM/cartoonify/tree/master/images" width="500" height="300">
</p>
Here is the picture after pencil sketch
<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/cartoonify/blob/master/images/pencil%20sketch.PNG" width="500" height="300">
</p>

# Pencil Edge Filter
Pencil Edges filter creates a new image that contains only significant edges and white background. After grayscale and gaussian blur, we apply Laplacian filter to detect the edges.
Here is the original picture:
<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/cartoonify/tree/master/images" width="500" height="300">
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

## Functionalities
- [ ]  < insert functionality >
- [ ]  < insert functionality >
- [ ]  < insert functionality >
- [ ]  < insert functionality >

<br>


## Instructions to run

* Pre-requisites:
	-  < insert pre-requisite >
	-  < insert pre-requisite >

* < directions to install > 
```bash
< insert code >
```

* < directions to execute >

```bash
< insert code >
```

## Contributors

<table>
<tr align="center">


<td>

Anushka Garg

<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/cartoonify/blob/anushka/images/Anushka.jpeg" width="190" height="300">
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

John Doe

<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/template/blob/master/logo-light.png?raw=true"  height="120" alt="Your Name Here (Insert Your Image Link In Src">
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

