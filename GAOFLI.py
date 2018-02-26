import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

	
def addCross (i,j,matrix):
	cross = np.array([[0,1,0],[1,1,1],[0,1,0]])
	matrix[i:i+3,j:j+3]=cross[:]
	
def survival(i,j,matrix,size):
    matrix2=matrix.copy()
    N=size
    total=int((matrix2[i,(j-1)%N] + matrix2[i,(j+1)%N] + matrix2[(i-1)%N,j] + matrix2[(i+1)%N,j] + matrix2[(i-1)%N, (j-1)%N] +  matrix2[(i-1)%N, (j+1)%N] + matrix2 [(i+1)%N, (j-1)%N] + matrix2 [(i+1)%N, (j+1)%N]))
    
    return total
   

def refresh(framNum, image, matrix, matrix_size):
    nMatrix = matrix.copy()
    for i in range (matrix_size):
        for j in range (matrix_size):
            nonei=survival(i,j,matrix,matrix_size)
            if matrix[i,j] == 1:
                if (nonei < 2) or (nonei > 3):
                    nMatrix[i,j] =  0
            else:
                if nonei == 3:
                    nMatrix[i,j] = 1
                    
    image.set_data(nMatrix)
    matrix[:]=nMatrix[:]
    return image

def main():
    matrix_size = 32
    refresh_rate = 50
    matrix = np.array([])
    matrix = np.zeros(matrix_size*matrix_size).reshape(matrix_size,matrix_size)
    start = np.random.uniform(0,matrix_size/2,2)
    addCross(int(start[0]),int(start[1]),matrix)
    f, axes = plt.subplots()
    image = axes.imshow(matrix, interpolation = 'nearest')
    an= animation.FuncAnimation(f, refresh, fargs=(image, matrix, matrix_size), interval = refresh_rate)
    plt.show()

if __name__ =='__main__':
    main()