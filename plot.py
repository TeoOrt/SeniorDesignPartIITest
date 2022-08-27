from matplotlib import pyplot as plt
import getinfo
import os


class Plotting():
	def __init__(self):
		self.x = [2,34,342]
		self.y = [1,2,3]
	def plotthis(self,**kwargs):
		self.args = kwargs
		plt.plot([self.y,self.x])
		plt.xlabel('Power Consumed')
		plt.ylabel('Power Generated')
		
		plt.savefig(f'/Users/teo/Desktop/SeniorDesignP2/Test/static/{self.args["projectname"]}')
		


main = Plotting().plotthis(projectname = 'PhotoVoltaics')