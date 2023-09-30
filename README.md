# Edge Detection

## Mean Blurr Edge Detection

If we were to consider an edge to be a line of pixels which are different from their surroundings.\
Would it be enough to detect said edges by testing which pixels are sufficiently different from their neighbours?\
When an image is blurred, a pixel should change most when the adjacent pixels are most different from itself.\
Could we then approach this by blurring an image and comparing each pixel with it's own blurred self, as a measure of how likely it'd be for it to be an edge pixel?\
Let's see what happens when we try it with this image:\
![Original](images/zebra.jpg)\
\
Blurr it, setting each pixel equal to the mean of those pixels around it:\
![Blurred](images/generated/Mean-zebra/blurred.jpg)\
\
Compute the difference between each original pixel and its blurred self\
![Difference](images/generated/Mean-zebra/diff.jpg)\
\
Let's apply a linear scale so that we use the entire 8bit range of each pixel.\
Thus, enhancing the gap between those pixels which where most different from those which were just a little\
![LinearScale](images/generated/Mean-zebra/scaled.jpg)\
\
