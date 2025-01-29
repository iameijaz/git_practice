"""
# MohrCirc3D.py
# Python program to plot Mohr's circle of stresses for 3D stress state
# Lecture: ST4CMS, WS2024/25
# Lecture 14, Exercise 12 - Mini Project
#
# The aim of this mini project is to bring together all competencies learnt in ...
# ... the Python part of the lecture
# 
# For more details on the task, students are required to use the accompanying material
#
# @author: A. Prakash
"""
# First import all required modules
#import sys
from sys import argv
import os
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eig

def readData(fname):
  """
  Function to read in stress tensor and volume from a file
  For more details on the data format in the file, refer to the accompanying documentation
  
  Hint: Read the file with native Python - this should be sufficient ...
  ... since the size of the file is rather small
  
  Input:
      fname: Name of the file which contains the stress and volume data
  Output:
      Stress: numpy array containing the stress of the corresponding Gauss point
      Volume: Volume of the Gauss point (scalar) 
  """
  with open(fname,'r') as file:
      content=file.read()
      if "#" in file:
          Vol=file.split(':')[1].strip()
      else:
          Stress = [[float(num) for num in line.split(' ')] for line in file]
  return np.array(Stress),Vol
  


def scaleStress(Sigma,sFac):
  """
  Function to scale stresses, e.g., from MPa to GPa
  Note that the function is to be a generic function that performs the scaling of ...
  ... any given stress tensor by a desired scaling factor.
  This function can hence also be used to convert from one system of units to another.
  
  Input:
    Sigma: Stress tensor (2D numpy array)
    sFac:  scaling factor or conversion factor (scalar)
  Output:
    scaledSig: scaled stress tensor, i.e., Sigma*Fac
  """
  scaledSig=np.multiply(Sigma,sFac)
  
  return scaledSig



def AvgStress(n,SigArr,VolArr):
  """
  Function to average >>>n<<< stress tensors using their volume.
  
  Input:
    n:      Number of Gauss points, i.e., number of stress tensors using which ...
            ... the average stress tensor is to be computed
    SigArr: Array of stress tensors, with each stress tensor being a 2D array
    VolArr: Array containing volume of individual Gauss points ...
            ... must be an array of size (nx1)
  Output:
    SigAvg: Averaged stress tensor
  """
  # Summation Sigma_i * V_i // Summation V_i
  SigAvg=np.einsum(SigmaArr,VolArr)
  #SigAvg=np.dot(SigArr,VolArr)/np.sum(VolArr) # Reshape ...
  return SigAvg



def EigVal(Sigma):
  """
  Function to compute and sort the eigenvalues of a given second order tensor
  Note that these eigenvalues will be used for plotting the Mohr's circle
  
  Input:
    Sigma: Stress tensor for which eigen values are to be computed
  Output:
    Sig_eigval: SORTED (ascending) Eigen values of the stress tensor
  """
  eigVals,eigenVectors=eig(Sigma)
  Sig_eigval = eigVals.argsort()[::-1]
  return Sig_eigval



def plotMohrsCircle(SigmaEigVal,foutNamePNG):
  """
  Function to plot the Mohr's circle for a 3D stress state
  HINT: Refer to the comment lines in the main body of the function.
        This should provide you with a sense of orientation as to what to do next.
  
  Input:
    SigmaEigVal:  Eigen values (sorted, ascending) of the stress tensor ...
                  ... for which the Mohr's circle is to be plotted
    foutNamePNG:  Name of the PNG file to save the plot
  Output:
    NONE
  """
  # First calculate the center and radii of the three circles
  # For the equations, refer to the accompanying documentation
  # Note: Eigenvalues are sorted in the ascending order!
  # i.e. S3,S2,S1
  # S1>S2>S3
  C1 =0.5*(S2+S3)
  R1 = 0.5*(S2-S3)
  C2 = 0.5*(S1+S3)
  R2 = 0.5*(S1-S3)
  C3 = 0.5*(S1+S2)
  R3 = 0.5*(S1-S2)
  print(C2,R2)
  print(C3,R3)
  print(C1,R1)
  
  # Discretize angle to plot the circle
  # and create the fig and axes environments
  #theta = #
  #fig   = 
  #ax    = 
  
  #First plot C2 (major circle)
  # Use the theta discretization done before! 
  # Remember: x=R*cos(theta)
  #           y=R*sin(theta)
  # NOTE: Theta is in degrees
  # Fill the area inside the circle







  
  #Now plot the other two circles, i.e., C1 and C3...
  #...using the same procedure as before
  #










  
  #Now for some decorations
  #Annotate your figure correctly
  # Use the font sizes defined below for labels and ticks!
  # Provide the right labels (including units)
  labelfontsize=24
  ticklabelsize=16





  plt.savefig(foutNamePNG, format='png')
  
  return
  

"""
Main function to manage everything else!
"""

if __name__=="__main__":
  #Provide help on usage of this program
  #if the right number of arguments are not provided ...
  #... or if the flag '-h' is used, we provide the user with usage information
  if(len(argv)<2 or argv[1]=='-h'):
    print('------- MohrCirc3D.py --------')
    print('Usage: python MohrCirc3D.py <FilePrefix> <nMaterialPts> <ext> <#Points>')
    sys.exit()
  #print(len(sys.argv),sys.argv)
  #---------------------------------------------------
  # Capture the user input (command line arguments) into the right variables
  # python MohrCirc.py Gr1 MatPt dat 10 
  fnamePrefix = argv[1] # Gr1
  MatPt       = int(argv[2]) # MatPt
  fnameExt    = argv[3] # dat
  nMatPts     = argv[4] # upto that number ... 10 
  print('Filename Prefix: ',fnamePrefix)
  print('Material Pt: ', MatPt)
  print('Filename extension: ',fnameExt)
  print('Number of materials points: ',nMatPts)
  
  #Conversion factor to be used
  sFac=0.001 #to convert from MPa to GPa
  #Loop over all material points...
  SigArr=[]
  VolArr=[]
  StressArr=[]
  for n in range(1,nMatPts+1):
      #... a) Generate the filename using the format fnamePrefix<number>.fnameExt
      # Here n will start from 1 to n where n is nMatPts
      fileName=f"{fnamePrefix}_{MatPt}{n}.{fnameExt}"
      #... b) Read the stress tensor and volume from the file using >>>readData<<<
      orig_stress_tensor,volume=readData(fileName)
      StressArr.append(orig_stress_tensor)
      VolArr.append(volume)
      #. c) Scale stress values (from MPa to GPa), if desired, using >>>scaleStress<<<
      stress_tensor=scaleStress(orig_stress_tensor,sFac) 
      #... d) Obtain Eigenvalues of the stress tensor using >>>EigVal<<<
      sig_vals=EigVal(stress_tensor) # Values of S1, S2, S3
      SigArr.append(sig_vals)
      #... e) Plot Mohr's circle for the corresponding stress state. Generate a name ...
      #        ... for the image file first and pass it as an argument to >>>plotMohrsCircle<<<
      # plot mohr function
      plotMohrsCircle(SigArr,"scaledStress_MohrCircle.png")
  #Now plot Mohr's circle with the average stress tensor
  #here: volumetric averaging
  #... a) first create a composite array with stress states of all Gauss points
  stress_arr=pass
  #... b) create another composite array with Volume data of all Gauss points
  vol_arr=pass
  #... c) call the function >>>AvgStress<<<
  avg_Stress=AvgStress(stress_arr)
  #... d) Obtain the Eigenvalues of the average  stress tensor
  eigVals=EigVal(avg_Stress)
  #... e) Plot Mohr's circle for the corresponding stress state. Generate a name ...
  #        ... for the image file first and pass it as an argument to >>>plotMohrsCircle<<<
  plotMohrsCircle(eigVals,"AvgStress_MohrCircle.png")







  
  #Now plot Mohr's circle with non-volumetric average stress tensor (arithmetic average)
  #NOTE: Use the same AvgStress function to perform the arithmetic averaging!
  # No modification of the code is required. Think, how you can perform the averaging...
  #... without modifying the code!
  #... a) Obtain the Eigenvalues of the average stress tensor (arithmetic average)
  #... b) Obtain the Eigenvalues of the average  stress tensor
  #... c) Plot Mohr's circle for the corresponding stress state. Generate a name ...
  #        ... for the image file first and pass it as an argument to >>>plotMohrsCircle<<<
  plotMohrsCircle()




  
