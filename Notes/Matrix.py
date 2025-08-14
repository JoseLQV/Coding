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