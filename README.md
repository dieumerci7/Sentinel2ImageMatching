# Sentinel-2 Image Matching

This project focuses on developing an algorithm for matching Sentinel-2 satellite images. The algorithm involves keypoint detection and image matching, providing insights into the corresponding points between different images.

## Files and Directory Structure

- `algorithm.py`: Contains the keypoint detection and image matching algorithm.
- `inference.py`: Python script for performing image matching between two input images.
- `demo.ipynb`: Jupyter notebook demonstrating the functionality of the image matching algorithm.

### Running the Inference Script

To run the image matching algorithm and generate matches between two images, you can use the `inference.py` script. Here is an example command:

```bash
python inference.py --path1 ./images/T36UYA_20160212T084052_B02.jp2 --path2 ./images/T36UYA_20160212T084052_B03.jp2 --ouput_filename matches_result_thick.jpg --n_matches 10
```

- `path1`: Path to the first image.
- `path2`: Path to the second image.
- `ouput_filename`: Name of the output file for the matches, including the file extension.
- `n_matches`: Number of matches to draw. If greater than the total, all the matches are drawn.
### Demo Notebook
The `demo.ipynb` notebook provides a visual demonstration of how the image matching algorithm works. It includes examples of matching between different bands and different seasons.

### Issues and Limitations
The algorithm works well for matching images from different bands of the same scene.
Matching images from different seasons may have limitations, as shown in the demo.

### Dependencies
OpenCV
Matplotlib
Numpy
Install using
```bash
pip install -r requirements.txt
```
### Acknowledgments
This project uses a images from [Deforestation in Ukraine from Sentinel2 data](https://www.kaggle.com/datasets/isaienkov/deforestation-in-ukraine) dataset.
Feel free to reach out for any questions or improvements!
