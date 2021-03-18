import matplotlib.pyplot as plt
import pandas as pd


def CreateChart(dataset, fname):
    pos_list = []
    neg_list = []
    for name in dataset:
        pos_list.append(dataset[name][0])
        neg_list.append(dataset[name][1])

    data = {'Positive': pos_list,
            'Negative': neg_list
           }

    df = pd.DataFrame(data,columns=['Negative','Positive'], index = [i for i in dataset])
    plt.style.use('seaborn')
    df.plot.barh()
    plt.title('Chart')
    plt.ylabel('Search')
    plt.xlabel('Quantity')
    plt.savefig('Charts/'+fname+'.png', bbox_inches='tight')