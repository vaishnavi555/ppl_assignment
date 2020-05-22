MAX = 100; 
  
def luDec(mat, n): 
  
    lower = [[0 for x in range(n)]  
                for y in range(n)]; 
    upper = [[0 for x in range(n)]  
                for y in range(n)]; 
                  
    # Decomposing matrix into Upper  
    # and Lower triangular matrix 
    for i in range(n): 
  
        # Upper Triangular 
        for k in range(i, n):  
  
            
            sum = 0; 
            for j in range(i): 
                sum += (lower[i][j] * upper[j][k]); 
  
             
            upper[i][k] = mat[i][k] - sum; 
  
        # Lower Triangular 
        for k in range(i, n): 
            if (i == k): 
                lower[i][i] = 1; # Diagonal as 1 
            else: 
  
                
                sum = 0; 
                for j in range(i): 
                    sum += (lower[k][j] * upper[j][i]); 
  
          
                lower[k][i] = int((mat[k][i] - sum) /
                                       upper[i][i]); 
  
	print("Lower Triangular\t\tUpper Triangular"); 
  
    # Displaying the result : 
    for i in range(n): 
          
        # Lower 
        for j in range(n): 
            print(lower[i][j], end = "\t");  
        print("", end = "\t"); 
  
        # Upper 
        for j in range(n): 
            print(upper[i][j], end = "\t"); 
        print(""); 
  
# Driver code 
mat = [[2, -1, -2], 
       [-4, 6, 3], 
       [-4, -2, 8]]; 
  
luDec(mat, 3); 
