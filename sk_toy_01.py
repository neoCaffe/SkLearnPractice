''' sklearn toy datasets '''
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_moons, make_circles

#--- Make two interleaving half circles 2個交錯的半圓型 (半月狀)
def mkMoons(nnoise=0.1, nCount=1000, nfig=0):
    X, y = make_moons(noise=nnoise, n_samples=nCount)
    sns.scatterplot(
        x=X[:, 0], y=X[:, 1], hue=y,
        marker='o', s=25, edgecolor='k', legend=False
        ).set_title('make_moons noise '+str(nnoise))
    plt.savefig('moon'+str(nfig)+'.jpg')
    plt.show()

#--- Make a large circle containing a smaller circle 大圓圈內有小圓圈
# factor :Scale factor between inner and outer circle in the range (0, 1)
def mkCircles(nnoise=0.1,nCount=1000, nfactor=0.5, nfig=0):
    X, y = make_circles(noise=nnoise, factor=nfactor, n_samples=nCount)
    sns.scatterplot(
        x=X[:, 0], y=X[:, 1], hue=y,
        marker='o', s=25, edgecolor='k', legend=False
        ).set_title('make_circles noise '+str(nnoise))
    plt.savefig('circle'+str(nfig)+'.jpg')
    plt.show()
    
#--- call function
distance = [0.1, 0.2, 0.5, 0.7, 0.9]
k = 0
for d in distance:
    mkMoons(d,1000,k)
    k += 1
    
k = 0
for d in distance:
    mkCircles(d,1000,0.5,k)
    k += 1
