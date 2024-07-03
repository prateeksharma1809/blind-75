### Question 1: Airport Limousine Problem
**Problem Description:**

An airport limousine can take multiple riders to the airport at the same time. On the way back to the starting point, the driver may pick up additional riders for the next trip to the airport. A map of rider locations has been created, represented as a square matrix.

The matrix is filled with cells, and each cell will have an initial value as follows:
- A value ≥ 0 represents a path.
- A value of 1 represents a rider.
- A value of -1 represents an obstruction.

**Rules of Motion:**
1. The driver starts at (0, 0) and the airport is at (n-1, n-1). Movement toward the airport is right (→) or down (↓) through valid path cells.
2. After reaching (n-1, n-1), the driver travels back to (0, 0) by moving left (←) or up (↑) through valid path cells.
3. When passing through a path cell containing a rider, the rider is picked up. Once picked up, the cell becomes an empty path cell.
4. If there is no valid path between (0, 0) and (n-1, n-1), then no riders can be collected.
5. The ultimate goal is to collect as many riders as possible.

**Example:**
Consider the following grid:
```
0 1 0
-1 0 1
1 1 1
```
Start at the top left corner. Move right one, collecting a rider. Move down one to the airport. Move down one to the airport. All paths have been cleared.

**Function Description:**
Complete the function `collectMax` in the editor below.

`collectMax` has the following parameter(s):
- `int mat[n]`: an array of integers describing the map

**Returns:**
- `int`: the maximum number of riders that can be collected

**Constraints:**
- \(1 \leq n \leq 100\)
- \(-1 \leq \text{mat}[i][j] \leq 1\)

### Question 2: Closest Pair of Points
**Problem Description:**

In many real-world applications, the problem of finding a pair of closest points arises. In the real world, data is usually distributed randomly. Given `n` points on a plane, randomly generated with uniform distribution, find the squared shortest distance between pairs of these points.

**Example:**
There are 3 points with x coordinates `x = [0, 10, 15]` and y = [0, 10, 20]. The points have the xy coordinates (0, 0), (10, 10), and (15, 20). The closest squared distance between any two pairs of these points is between (10, 10) and (15, 20), which is \((15-10)^2 + (20-10)^2 = 125\).

**Function Description:**
Complete the function `closestSquaredDistance` in the editor below.

`closestSquaredDistance` has the following parameter(s):
- `int x[n]`: each `x[i]` denotes the x coordinate of the ith point
- `int y[n]`: each `y[i]` denotes the y coordinate of the ith point

**Returns:**
- `long`: a long integer that denotes the squared shortest distance between the pairs of points

**Constraints:**
- \(2 \leq n\)
- either \(n \leq 1000\) or \(n = 10^5\)
- values of `x[i]` and `y[i]` are randomly generated with uniform distribution from the range [0, \(10^9\) - 1]