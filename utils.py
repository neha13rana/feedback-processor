import matplotlib.pyplot as plt 
import base64
from io import BytesIO

def get_plot(x,y,name,i):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.xticks(x,name) 
   
    if(i==1):plt.bar(x,y)
    elif(i==2):plt.plot(x,y)
    elif(i==3):
        plt.pie(y,labels=name)
    
    buff = BytesIO()
    plt.savefig(buff, format='png')
    buff.seek(0)
    img_png = buff.getvalue()
    graph=base64.b64encode(img_png)
    graph=graph.decode('utf-8')
    buff.close()
    return graph