import numpy as np
from matplotlib import pyplot as plt

def main():
    pts = np.random.randn(200,2)
    labels = [("r" if np.linalg.norm(p) < 1.0 else "b") for p in pts]
    for pt,label in zip(pts,labels):
        plt.scatter(pt[0],pt[1],c=label)
    theta = np.linspace(0,2*np.pi)
    plt.plot(np.sin(theta),np.cos(theta),c='k')
    xaxis = plt.Line2D([-3,3],[0,0],c='g')
    yaxis = plt.Line2D([0,0],[-3,3],c='g')
    ax = plt.gca()
    ax.add_line(xaxis)
    ax.add_line(yaxis)
    plt.gcf().savefig('kernelTrick.eps')
    plt.show()

    for pt,label in zip(pts,labels):
        plt.scatter(pt[0]**2,pt[1]**2,c=label)
    xaxis = plt.Line2D([-10,10],[0,0],c='g')
    yaxis = plt.Line2D([0,0],[-10,10],c='g')
    divisor = plt.Line2D([-1,2],[2,-1],c='k')
    ax = plt.gca()
    ax.add_line(xaxis)
    ax.add_line(yaxis)
    ax.add_line(divisor)
    plt.gcf().savefig('kernelTrick_T.eps')
    plt.show()

if __name__ == "__main__":
    main()
