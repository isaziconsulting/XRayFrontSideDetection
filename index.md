<style>
table{
    border-collapse: collapse;
    border-spacing: 0;
    border:2px solid #fafafa;
    width:200px;
    font-style: italic;
    font-size: 15px;
}

th{
    border:2px solid #fafafa;
}

td{
    border:1px solid #fafafa;
}
</style>

<style>
body {
  font-size: 17px;
  }
</style>

<table align="right">
  <tr>
    <td><b>Author:</b></td>
    <td>Jason Perlow</td>
  </tr>
</table>

<br/>

----------

## Agni: A simple front vs side classification model

![alt text](https://upload.wikimedia.org/wikipedia/commons/f/fe/Agni_god_of_fire.jpg "Agni: the Hindu god of fire")

Deep learning has been used extensively to automatically process and classify medical scans. As contribution to this field we open-source code that automatically determines if a given xray faces forwards (frontal) vs sideways (lateral) using convolutional neural networks.

![alt text](assets/frontandside.jpg "lateral and frontal xrays")

# How it works

Convolutional neural networks (convnets) are a deep learning technique that use a hierarchy of filter banks to extract visual features as an input for a classifier. Our model uses a convnet with four convolutional layers and two dense affine layers. For our model we adopt the structure of the VGG model which pools after every two convolutional layers.

To find weights for filter banks that extract good features . As a loss function we use binary cross-entropy and the Adam as our gradient descent optimiser.

# Data

Our data is the open Montgomary database. We manually labeled 173 frontal and 123 lateral images. We rescaled xrays to 128x128 px images. We augmented the data by rotating images in the range of -30 degrees to +30 degrees.

# Performance

Our model acheives 99% accuracy and a log-loss of 0.1 compared to previous work which achieves accuracy and . Our work is therefore comparable to previous work but with fewer parameters. Our model uses 2 convolutional layers instead of Googlenet which uses 22 convolutional layers and is therefore both more memory and computationally efficient.

# Follow Us

<!-- display the social media buttons in your README -->
[![alt text][1.1]][1]
[![alt text][2.1]][2]
[![alt text][3.1]][3]

<!-- links to social media icons -->
<!-- no need to change these -->

<!-- icons with padding -->
[1.1]: http://i.imgur.com/tXSoThF.png (twitter icon with padding)
[2.1]: http://i.imgur.com/P3YfQoD.png (facebook icon with padding)
[3.1]: http://i.imgur.com/0o48UoR.png (github icon with padding)

<!-- links to your social media accounts -->
<!-- update these accordingly -->

[1]: https://twitter.com/isaziconsulting
[2]: https://www.facebook.com/Isazi-Consulting-240193656434498/
[3]: https://github.com/isaziconsulting
