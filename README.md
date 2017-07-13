# Agni - X-ray Front vs Side Detection

A simple x-ray classifier to differentiate front (frontal) vs side (lateral) x-rays developed at isazi Consulting.

See our [blog post](https://isaziconsulting.github.io/XRayFrontSideDetection/) for a conceptual overview of this project.

## Requirements

* numpy
* Keras
* scikit-image

## Code

Code is contained in `src` and is split into two files `test_Agni.py` and `train_Agni.py`.

The required directory structure is as follows:

```
src/
  test_Agni.py
  train_Agni.py
  agni.hdf5
  logs/
data/
  train/
    front/
    side/
  valid/
    front/
    side/
```
