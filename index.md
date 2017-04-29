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

## Agni: A simple front vs side x-ray classification model

<center>
    <img src="assets/Agni.jpg" alt="The Hindu deity Agni: One of the guardian deities of direction" style="width: 400px;"/>
    <figcaption style="font-size: 9pt">The Hindu deity Agni: One of the guardian deities of direction (<i>wikimedia commons</i>)</figcaption>
</center>

Deep learning has been used extensively to automatically process and classify medical scans. As a contribution to this field we open-source Agni, a simple yet accurate model that automatically determines if a given patient x-ray is facing forwards (frontal) or sideways (lateral).

# Data

As data we use the open [Montgomery County chest x-ray database](http://archive.nlm.nih.gov/repos/chestImages.php). Since this data doesn't have patient orientation information we manually labeled 173 frontal and 123 lateral images. To allow for a smaller neural network we rescaled x-rays to 128x128 px. Since we have few training samples we synthesised more the data by randomly rotating images in the range of -30 degrees to +30 degrees and flipping them along their vertical axis.

<center>
    <img src="assets/frontandside.jpg" alt="Sample x-rays from the Mongomery dataset" style="width: 400px;"/>
    <figcaption style="font-size: 9pt">Sample x-rays from the Mongomery dataset</figcaption>
</center>


# How it works

Convolutional neural networks (convnets) are a deep learning technique that use a hierarchy of filter banks to extract visual features as an input for a classifier. Structurally Agni is a convnet with four convolutional layers and two dense affine layers. In particular our architecture is based on the widely used VGG model where pooling (downsampling) occurs after every two convolutional layers.

To find filter bank weights that extract good features, weights are iteratively adjusted such that Agni best predicts the orientation of a given x-ray and orientation label pair. The extent to which a prediction is correct is measured using a loss function. Since our problem has two classes (frontal and lateral), we use binary cross-entropy loss. To adjust weights such that loss is minimised we use [Adam](https://arxiv.org/abs/1412.6980), a modern gradient descent optimiser.

A 100 iterations/epochs of training were sufficient for our model to converge to a near zero valuation loss:

<p style="float: left; font-size: 9pt; text-align: center; width: 48%; margin-right: 1%; margin-bottom: 0.5em;">
  <img src="assets/acc.png" style="width: 100%"/>
  Valuation accuracy during training (smoothed curve in bold).
</p>

<p style="float: right; font-size: 9pt; text-align: center; width: 48%; margin-right: 1%; margin-bottom: 0.5em;">
  <img src="assets/loss.png" style="width: 100%"/>
  Valuation loss over 100 iterations (smoothed curve in bold)</p>
<p style="clear: both;"/>


# Performance

Our model achieves a false positive rate of 1% and true positive rate of 99%. We also achieved a log-loss of 0.1 compared to previous work which achieves a false positive rate of and a true positive rate of . Our work is therefore comparable to previous work but is much simpler. Our model uses 2 convolutional layers instead of Googlenet which uses 22 convolutional layers and is therefore both more memory and computationally efficient.

Here is a confusion matrix of front vs side classifications:

<table align="center" style="width:75%;font-size: 11pt">
<caption style="font-size: 9pt">Confusion matrix</caption>
  <tr>
    <th></th>
    <th><p><b>True frontal</b></p></th>
    <th><p><b>True lateral</b></p></th>
  </tr>
  <tr>
    <td><p><b>Predicted frontal</b></p></td>
    <td><p>1</p></td>
    <td><p>1</p></td>
  </tr>
  <tr>
    <td><p><b>Predicted lateral</b></p></td>
    <td><p>1</p></td>
    <td><p>1</p></td>
  </tr>
</table>


Since we're dealing with data that has binary classes there is a trade-off between false positive rate and false negative rate depending on our threshold. To quantify the continuum of these values we plot a ROC curve:

# Future extensions

This project can easily be extended to an arbitrary binary medical scan classifier (PET scan slides, MRIs slides, ...). Feel free to fork this project and classify your own data!

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
