import pandas as pd
import matplotlib.pylab as plot
import numpy as np
import getopt
import sys

def main():

	try:
		opts, args = getopt.getopt(sys.argv[1:], shortopts="f:")

	except getopt.GetoptError as err:
		print(err)
		print "Please specify filename of FaST-LMM output."
		sys.exit()

	for o in opts:
		if o[0] in ("-f"):
			filename = str(o[1])

	output = pd.read_table(filename)
	output = output.sort(["Chromosome", "Position"])

	output["Pvalue"] = -np.log(pd.Series(output["Pvalue"]), dtype="float64")
	max_chromosome = output["Chromosome"].max()

	for i in range(1, max_chromosome):
		chr1max = max(output["Position"][output["Chromosome"].isin([i])])
		output["Position"][output["Chromosome"].isin([i+1])] = output["Position"][output["Chromosome"].isin([i+1])] + chr1max

	colors = ["bo", "ro", "yo"]

	for i in range(1, max_chromosome):
		plot.plot(output["Position"][output["Chromosome"].isin([i])], output["Pvalue"][output["Chromosome"].isin([i])], colors[i%3]) 
	plot.savefig("FaSTLMM_Plot.png")


if __name__ == "__main__":
	main()
