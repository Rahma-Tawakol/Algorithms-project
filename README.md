 Project description:
 
 i. Counting sort algorithm

 Input: An array (A) of size n, where elements are integers in the range 0 to K.
 Output: A sorted array (B)
 
 Steps:
 1- Find the maximum value in array A.
 2- Initialize the counting array C and the output array B.
 3- Count occurrences of each element.
 4- Compute the cumulative count to determine the position of elements in the sorted array.
 5- Place elements in their correct positions in array B.
 6- Print the sorted array.

 Time Complexity: O(n+K)
 Space Complexity: O(n+K)


 Example 
 Input:
 A = [4, 2, 2, 8, 3, 3, 1, 5, 7, 5]

 Output:
 Sorted Array: [1, 2, 2, 3, 3, 4, 5, 5, 7, 8]


 ***********************************************************************************


 ii.Prim’s algorithm

 Input: A connected, undirected graph G = (V,E) with V vertices and E edges.
 Output: The edges of the MST.
 
 Steps:
 1- Start with vertex u as a starting point.
 2- Maintain a priority queue to store edges based on their weights.
 3- Use a boolean array to track visited vertices.
 4- Repeat until all vertices are included in the MST.
 5- Return the edges of the MST.
 
 Time Complexity: O(ElogV)
 Space Complexity: O(V+E)


 Example 
 Input:
 graph = {
    0: [(1, 1), (3, 2)],
    1: [(1, 0), (3, 2), (6, 3)],
    2: [(3, 0), (3, 1), (4, 3)],
    3: [(6, 1), (4, 2)]
 }

 Output:
 Edges in MST: [(0, 1, 1), (0, 2, 3), (2, 3, 4)]

