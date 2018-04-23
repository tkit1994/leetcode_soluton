# 416.Hamming Distance

## Descripthon

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.Given two integers x and y, calculate the Hamming distance

## Note

![](https://latex.codecogs.com/gif.latex?0&space;<&space;x,&space;y&space;<&space;2^{31})

## Example

```python
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
```

```python
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
```