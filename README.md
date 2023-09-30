# Edge Detection

## Mean Blurr Edge Detection

If we were to consider an edge to be a line of pixels which are different from their surroundings.
Would it be enough to detect said edges by testing which pixels are sufficiently different from their neighbours?
When an image is blurred, a pixel should change most when the adjacent pixels are most different from itself.
Could we then approach this by blurring an image and comparing each pixel with it's own blurred self, as a measure of how likely it'd be for it to be an edge pixel?
Let's see what happens when we try with this image:
![Original](images/zebra.jpg)
