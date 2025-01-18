import numpy as np

def graidentDecent(x,y):
    m_carr = b_carr =0
    epocs = 1000
    learning_rate = 0.001
    n = len(x)
    for i in range(epocs):
        y_predict = m_carr*x+b_carr
        md = -(2/n)*sum(x*(y-y_predict))
        bp=  -(2/n)*sum(y-y_predict)
        m_carr= m_carr - learning_rate * md
        b_carr = b_carr - learning_rate * bp
        print("m {}, b {},epocs {}".format(m_carr,b_carr,i))

x= np.array([1,2,3,4,5])
y= np.array([5,7,9,11,13])

graidentDecent(x,y)