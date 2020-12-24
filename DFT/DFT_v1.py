import numpy as np
import matplotlib.pyplot as plt
class fourrier_transform:
    def __init__ (self,data):
        self.N=len(data)
        self.data=np.array(data)
        
    def exp_complex(self,value):
        real=np.cos(value)
        img=np.sin(value)
        return np.array([real,img])
    def DFT(self):
        data=self.data
        N=self.N
        Y_real,Y_img=np.zeros(N),np.zeros(N)
        Y_real,Y_img=self.run_DFT(Y_real,Y_img,N)

    def run_DFT(self,Y_real,Y_img,N):
        data=self.data
        for n in range(0,N):
            for k in range(0,N):
                power=-2*np.pi/N
                complex_output=data[k]*self.exp_complex(power*n*k)
                Y_real[n]+=complex_output[0]
                Y_img[n]+=complex_output[1]
        self.Y_real=Y_real
        self.Y_img=Y_img
        return Y_real,Y_img
    def plot_real(self):
        fig,ax=plt.subplots(1,1)
        ax.plot(np.arange(self.N),self.Y_real)
        ax.grid(True)
    def plot_img(self):
        fig,ax=plt.subplots(1,1)
        ax.plot(np.arange(self.N),self.Y_img)
        ax.grid(True)
    def plot(self,range_x=False):
        fig,ax=plt.subplots(1,1)
        self.Y_mod=(self.Y_img**2+self.Y_real**2)**0.5
        ax.plot(np.arange(self.N),self.Y_mod,'-o')
        ax.grid(True)
        if range_x:
            ax.set_xlim(range_x)
            
        ax.legend()