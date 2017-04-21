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

Deep learning has been used extensively to automatically process and classify medical scans. To this end we open-source code that automatically determines if a given xray faces forwards (frontal) vs sideways (lateral).

# How it works

Convolutional neural networks (convnets) are a deep learning technique that use a hierarchy of filter banks to extract visual features as an input for a classifier. In our model we use a convnet with two convolutional layers and two dense affine layers. 

To find weights for filter banks that extract good features we train out model on 173 manually labelled images. As a loss function we use binary cross-entropy and the Adam as our gradient descent optimiser. 

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

