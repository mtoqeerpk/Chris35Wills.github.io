#!/usr/bin/env python

"""aspect_quiver.py: Creates a quiver plot of an aspect grid."""

import numpy as np
import matplotlib.pyplot as plt

__author__ = "Chris Williams"
__email__ = "chrwil@bgs.ac.uk"
#__copyright__ = 'Copyright {year}, {project_name}'
#__credits__ = ['{credit_list}']
#__license__ = '{license}'
#__version__ = '{mayor}.{minor}.{rel}'
#__maintainer__ = '{maintainer}'
#__status__ = '{dev_status}'

# Main code

#Example: https://pythonforundergradengineers.com/quiver-plot-with-matplotlib-and-jupyter-notebooks.html

def single_quiver(x_pos,y_pos,x_direct,y_direct, title=''):
	fig, ax = plt.subplots()
	ax.quiver(x_pos,y_pos,x_direct,y_direct, scale=5)
	ax.axis([-2,2,-2,2])
	if title !='':
		plt.title(title)
	plt.show()
	
def how_quiver_works():
	"""Demo how  quiver plot works
	"""
	 
	#Aspect example: If it was 90 deg, that would be
	x_pos = [0]
	y_pos = [0]
	x_direct = [1]
	y_direct = [0]
	title="x_pos:%i x_direct:%i | y_pos:%i y_direct:%i" %(x_pos[0], x_direct[0], y_pos[0], y_direct[0])
	single_quiver(x_pos,y_pos,x_direct,y_direct, title=title)

	#Aspect example: If it was 180 deg, that would be
	x_pos = [0]
	y_pos = [0]
	x_direct = [0]
	y_direct = [-1]
	title="x_pos:%i x_direct:%i | y_pos:%i y_direct:%i" %(x_pos[0], x_direct[0], y_pos[0], y_direct[0])
	single_quiver(x_pos,y_pos,x_direct,y_direct, title=title)

	#Aspect example: If it was 245 deg, that would be
	x_pos = [0]
	y_pos = [0]
	x_direct = [-1]
	y_direct = [0]
	title="x_pos:%i x_direct:%i | y_pos:%i y_direct:%i" %(x_pos[0], x_direct[0], y_pos[0], y_direct[0])
	single_quiver(x_pos,y_pos,x_direct,y_direct, title=title)

	#Aspect example: If it was 90 deg, that would be
	x_pos = [0]
	y_pos = [0]
	x_direct = [0]
	y_direct = [1]
	title="x_pos:%i x_direct:%i | y_pos:%i y_direct:%i" %(x_pos[0], x_direct[0], y_pos[0], y_direct[0])
	single_quiver(x_pos,y_pos,x_direct,y_direct, title=title)

#~~~~~~~~~~~~~~~~~~
# Plot surface aspect (relative to north)

def compassBearing_to_standardPosition__degrees_counterClockwise(bearing_deg):
	"""Vector magnitude and direction calculations assume angle is relative to the x axis (i.e. 0 degrees is at 3 o'clock)
	Adjust compass bearings to be relative to standard poisiton
	Help: https://math.stackexchange.com/questions/492167/calculate-the-angle-of-a-vector-in-compass-360-direction
	"""
	std_pos=(450 - bearing_deg) % 360
	return(std_pos)

def calculate_U_and_V__vector_magnitude_and_direction(angle_degrees, magnitude=1):
	"""Calculates the components of a vector given in magnitude (U) and direction (V) form

	angle: Expected that angles are in standard position (i.e. relative to the x axis or where 3 o'clock is zero and not the compass bearing where 12 o'clock is 0)
	magnitude: defaults to 1
	Help: https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:vectors/x9e81a4f98389efdf:component-form/v/vector-components-from-magnitude-and-direction
	"""
	angle_rad=np.deg2rad(angle_degrees)
	x = magnitude * np.cos(angle_rad) # change in x == U
	y = magnitude * np.sin(angle_rad) # change in y == V
	return(x,y)

#~~~~~~~~~~~~~~~~~~
#http://colaweb.gmu.edu/dev/clim301/lectures/wind/wind-uv

north_bearings=[0,90,180,270,360]

print("Compass bearing : Standard position angle")
for bearing in north_bearings:
	print("%i : %i" %(bearing, compassBearing_to_standardPosition__degrees_counterClockwise(bearing)))

def example_quiver_plots():
	angle=compassBearing_to_standardPosition__degrees_counterClockwise(0)
	x_direct,y_direct=calculate_U_and_V__vector_magnitude_and_direction(angle_degrees=angle)
	single_quiver(x_pos=0,y_pos=0,x_direct=x_direct,y_direct=y_direct)

	angle=compassBearing_to_standardPosition__degrees_counterClockwise(90)
	x_direct,y_direct=calculate_U_and_V__vector_magnitude_and_direction(angle_degrees=angle)
	single_quiver(x_pos=0,y_pos=0,x_direct=x_direct,y_direct=y_direct)

	angle=compassBearing_to_standardPosition__degrees_counterClockwise(180)
	x_direct,y_direct=calculate_U_and_V__vector_magnitude_and_direction(angle_degrees=angle)
	single_quiver(x_pos=0,y_pos=0,x_direct=x_direct,y_direct=y_direct)

	angle=compassBearing_to_standardPosition__degrees_counterClockwise(270)
	x_direct,y_direct=calculate_U_and_V__vector_magnitude_and_direction(angle_degrees=angle)
	single_quiver(x_pos=0,y_pos=0,x_direct=x_direct,y_direct=y_direct)

def plotMat(X):
	"""Plot matrix and label cells based on values
	"""
	fig, ax = plt.subplots()
	#imshow portion
	ax.imshow(X, interpolation='nearest')

	#text portion
	diff = 1.
	min_val = 0.
	rows = X.shape[0]
	cols = X.shape[1]
	col_array = np.arange(min_val, cols, diff)
	row_array = np.arange(min_val, rows, diff)
	x, y = np.meshgrid(col_array, row_array)
	for col_val, row_val in zip(x.flatten(), y.flatten()):
	    c = '+' if X[row_val.astype(int),col_val.astype(int)] < 0.5 else '-' 
	    ax.text(col_val, row_val, c, va='center', ha='center')



	#set tick marks for grid
	ax.set_xticks(np.arange(min_val-diff/2, cols-diff/2))
	ax.set_yticks(np.arange(min_val-diff/2, rows-diff/2))
	ax.set_xticklabels([])
	ax.set_yticklabels([])
	ax.set_xlim(min_val-diff/2, cols-diff/2)
	ax.set_ylim(min_val-diff/2, rows-diff/2)
	ax.grid()
	plt.show()


<<<<<<< all good above


#~~~~~~~~~
# Create faux aspect grid
#aspect_grid=360*(np.random.random_sample((11, 11)))
aspect_grid=360*(np.random.random_sample((3, 3)))

aspect_grid=np.array([[ 216,  226,  151],
       [  74,  323,  268],
       [ 177,  204,   84]])
print("Aspect value (deg N): ", np.floor(aspect_grid))

## Plot aspect grid
#cmap = 'twilight_shifted'#'twilight'#, 'twilight_shifted'
#plt.imshow(np.floor(aspect_grid), cmap=cmap, origin='lower')
#plt.colorbar(label="Aspect (degrees N)")
#plt.title("Random aspect values")
#plt.show()


#flip_arrow
#aspect_grid=aspect_grid-180

#~~~~~~~
# Create quiver plot
def array_indices(arr, indexing='xy'):
	"""Calculates index positions of each cell in array
	These can be used to map to e.g. when creating a quiver plot

	indexing: Giving the string 'ij' returns a meshgrid with
		matrix indexing, while 'xy' returns a meshgrid with Cartesian indexing.
		In the 2-D case with inputs of length M and N, the outputs are of shape
		(N, M) for 'xy' indexing and (M, N) for 'ij' indexing.
	"""
	nrows, ncols = arr.shape
	nx = 1
	ny = 1
	x = np.linspace(0, ncols-1, ncols)
	y = np.linspace(0, nrows-1, nrows)
	#y = np.linspace(nrows-1, 0, nrows) # note that the largest vlue is first
	xi, yi = np.meshgrid(x, y, indexing=indexing)
	return(xi, yi)

x,y=array_indices(aspect_grid, indexing='xy')
print(x)
print(y)


x_change,y_change=calculate_U_and_V__vector_magnitude_and_direction(aspect_grid.flatten())

##x = x positions (i.e. of each cell)
##y = y positions (i.e. of each cell)
##x_norm = U
##v_norm = V
#plt.quiver(x, y, y_change, x_change, pivot='middle')

# All together now...
cmap = 'twilight_shifted'#'twilight'#, 'twilight_shifted'
plt.imshow(np.floor(aspect_grid), cmap=cmap, origin='lower')
plt.colorbar(label="Aspect (degrees N)")
plt.quiver(x, y, y_change, x_change, pivot='middle')
plt.title("Random aspect values")
plt.show()


#	# Important:
#	* we are plotting the aspect grid with the origin in the bottom left
#	* the x and y coordinates (first two arguments of quiver) were calculted assuming xy indexing (not ij) << see array_indices()
#	* the U and V arguments are passed to quiver such that the first argument ("U" as expected by quiver) is y_change and the second argument ("V") is x_change << see calculate_U_and_V__vector_magnitude_and_direction()
#	
#	
#	Why does the folowing quiver statment map correctly:
#	
#	plt.quiver(x, y, y_change, x_change, pivot='middle')
#	
#	whereas what I would expect doesn;t map correctly?:
#	
#	plt.quiver(x, y, x_change, y_change, pivot='middle')
#	
#	
#	
#	# Next steps for web GIS mapping
#	Output U and V at the xy coordiantes taken from the grid as a shapefile
#	Plot U and V with line symbology
#	Serve as a WMS in UKSO

