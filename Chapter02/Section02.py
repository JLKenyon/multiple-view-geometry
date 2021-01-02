
import numpy




# Example 2.3
def example_2_3():
  print('''
*******************************************************************************
* Example 2.3
Where do the following lines intersect?
eq1: -1 * x  +   0 * y  +  1 = 0 
eq2:  0 * x  +  -1 * y  +  1 = 0

             | i  j  k |   ( 1 )
x = l x l' = |-1  0  1 | = ( 1 )
             | 0 -1  1 |   ( 1 )

''')
  result = numpy.cross([-1, 0, 1], [0, -1, 1])
  print(result)
  print("\n")
  
  print("result:")
  print(result[0:2])

  print("The last field in the result should be 1, so this is a real point, not an ideal point")
  print("The first two fields should be [1,1], which is the point in R2 where the lines intersect")

  print('\n\n')



# Example 2.5
def example_2_5():
  print('''
*******************************************************************************
* Example 2.5
Where do the following parallel lines intersect?
eq1: x = 1   =>   -1 * x  +  0 * y  +  1 = 0
eq2: x = 2   =>   -2 * x  +  0 * y  +  1 = 0
             | i  j  k |   ( 0 )
x = l x l' = |-1  0  1 | = ( 1 )
             |-1  0  2 |   ( 0 )
''')
  result = numpy.cross([-1, 0, 1], [-1, 0, 2])
  print("\n")
  print("result:")
  print(result)
  print("The last field in the result should be a 0, so this is an ideal point at infinity, not a real point")
  print("This means that the two lines are parallel.")
  print("The clever aspect is that the same operation, the cross product, gave us a clearly valid answer, of the same type R^3")
  
  



print("Section 2")
example_2_3()
example_2_5()
