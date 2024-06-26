# Pascal Triangle Solution

`def pascal_triangle(n)`

- Create an array of array with default value of 1's
- Starting from the third row( since both 1st and 2nd row are [1] and [1,1] respectively)
- Add the two previous item to get the next item
- Append 1 to the array
- Return the array
