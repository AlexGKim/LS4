import matplotlib.pyplot as plt
import matplotlib
import numpy


matplotlib.use('macOSX')

from scipy.stats import norm

m_Ia = -19.25
sig_Ia = 0.12
m_IIL = -17.98
sig_IIL= 0.34

def mixturemodel(cont = 0.98):
	n=100000
	r = norm.rvs(size=n)
	n_IIL= round(n*(1-cont))
	r[:n_IIL]=m_IIL + r[:n_IIL]*sig_IIL
	r[n_IIL:] = m_Ia + r[n_IIL:]*sig_Ia
	return r.std()

def contmodel(eff = 1):
	return numpy.tanh(2/eff**2)

if __name__ == "__main__":

	eff = numpy.arange(0,1.0001,0.05)
	purity = contmodel(eff)

	fig, ax1 = plt.subplots()
	color = 'tab:red'
	ax1.set_xlabel('efficiency')
	ax1.set_ylabel('purity', color=color)
	ax1.plot(eff, purity, color=color)
	ax1.tick_params(axis='y', labelcolor=color)

	ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

	color = 'tab:blue'
	std = [mixturemodel(1-p) for p in purity]
	std=numpy.array(std)
	ax2.set_ylabel('FOM', color=color)  # we already handled the x-label with ax1
	ax2.plot(eff, eff/std**2, color=color,label="Slight IIL contamination")
	ax2.tick_params(axis='y', labelcolor=color)

	plt.plot(eff,eff/sig_Ia**2,linestyle='dashed', color=color,label="No contamination (spec)")

	plt.legend()
	plt.show()

    # conts = numpy.arange(0.95,1.0001,0.005)
    # std = [mixturemodel(cont) for cont in conts]
    # std=numpy.array(std)
    # plt.plot(conts,std**2)
    # plt.show()