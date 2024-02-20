from pylab import *
from scot.datatools import randomize_phase
np.random.seed(1234)
s = np.sin(np.linspace(0,10*np.pi,1000))
x = np.vstack([s, np.sign(s)])
y = randomize_phase(x)
subplot(2,1,1)
title('Phase randomization of sine wave and rectangular function')
plot(x.T + [1.5, -1.5]), axis([0,1000,-3,3])
subplot(2,1,2)
plot(y.T + [1.5, -1.5]), axis([0,1000,-3,3])
plt.show()