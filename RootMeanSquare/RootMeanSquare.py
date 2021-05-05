#!/usr/bin/env python-real

import os
import sys
import slicer
import numpy as np
try:
    import tables
except:
    slicer.util.pip_install('tables')
    import tables

def main(signal, samplingRate):
    N = int(np.ceil(samplingRate * 50e-3)) # length of sub samples
    signal = signal[int(np.remainder(len(signal),N)):] # cut signal so can be devided by N
    X = np.reshape(signal, (-1,N)) # split signal into samples of length N and put them into matrix
    rms = np.sqrt(np.mean(X**2, axis=1)) # root mean square value
    rms_median = np.median(rms)
    rms_std = np.std(rms)
    stableParts = (rms < (rms_median+3*rms_std)) & (rms > (rms_median-3*rms_std))
    edges = [0] + np.argwhere(np.logical_not(stableParts)).flatten().tolist() + [len(stableParts)]
    longest = int(np.argmax(np.diff(edges)))
    X = X[edges[longest]+3:edges[longest+1]-3][:]
    stableSignal = X.flatten()
    return np.sqrt(np.mean(stableSignal**2))


if __name__ == "__main__":
    dataFile = tables.open_file(sys.argv[-1],'r')
    outValue = main(dataFile.get_node('/data')[:], dataFile.get_node('/sr')[:][0])
    returnParameterFile = open(sys.argv[-2], "w")
    returnParameterFile.write("rootMeanSquare = %.2f" % (outValue))
    returnParameterFile.close()
