from matplotlib import pyplot as plt



class Plotting():

	def plotthis(self,x,y):
		
		plt.plot([x],[y])
		plt.savefig('my_plot.png')
		# Display the plot:

main = Plotting.plotthis()
