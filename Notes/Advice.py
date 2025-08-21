""""
Max Profit: 

since it traverses just from left to right , just update lowest when it finds something lower and change profit accordingly 

observation :
traverse find lower point and compare until the end, if you find a new lowest then you update it 

"""

"""
setZeroes

in place modification in a matrix
Make sure to mark first change later, meaning traverse twice for in place problems
"""

""" 
54. Spiral Matrix 

Layer by Layer traversal : Boundaries indexes

        left to right
            update top
            
        top to bottom
            update right 
        
        if edge case
        right to left
            update bottom
            
        if edge case
        bottom to top
            update left

"""
""" 
1448 Count Good Nodes in Binary tree

Keep track of path max value in a dfs way

"""

""" 
98. Validate Binary Search Tree

Keep a left and right range starting with -infinity and also +infinity and traverse in a dfs way

"""



