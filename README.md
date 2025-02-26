# AICourseProjects

1. **Project 1: Route Finding using Search Algorithms**  
2. **Project 2: Closed Form Linear Regression**

---

## Project 1: TSP Solution with Search Algorithms

### 📋 Problem Statement
Implementation of the Traveling Salesman Problem (TSP) solution using three search algorithms:
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Uniform Cost Search (UCS)

In this project, the program reads two lines of input:
- **Input:**  
  - Start city (line 1)  
  - Destination city (line 2)

- **Output:** For each algorithm, the following details are printed:
  - Path cost
  - Optimal route
  - Number of expanded nodes
  - Maximum nodes in memory
  - Search execution time (in milliseconds)

**Example Input:**
```
New York
Los Angeles
```

**Example Output:**
```
BFS:
- Cost: 2451
- Path: New York -> Los Angeles
- Number of Nodes: 1
- Number of Nodes in Memory: 1
- Time: 10ms
```

---

## Project 2: Closed Form Linear Regression

### 📋 Problem Statement
House price prediction using closed-form linear regression on area-price data. The training dataset provides:
- **Column 1:** Area of houses (e.g., in square feet)
- **Column 2:** Price of each house

### 📈 Key Components
1. **Loss Function:**  
   Define the loss function for Linear Regression as:
   ```  
   J(w) = 1/(2m) Σ (y_i - wx_i)^2  
   ```
2. **Step Size Analysis:**  
   Explore loss values around optimal weights by varying the weight (slope) within a defined interval.
3. **Visualizations:**  
   - **Loss vs. Step Size Plot:** Illustrates the change in loss as the weight varies.
   - **Regression Plot:** Overlays the best-fit regression line on the training data points.


