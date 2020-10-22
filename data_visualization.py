import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def show_values_on_bars(axs):
    def _show_on_single_plot(ax):
        for p in ax.patches:
            _x = p.get_x() + p.get_width() / 2
            _y = p.get_y() + p.get_height()
            value = int(p.get_height())
            ax.text(_x, _y, value, ha="center")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)


def show_values_on_bars(ax, type):
    for p in ax.patches:
        _x = p.get_x() + p.get_width() / 2
        _y = p.get_y() + p.get_height()
        if type == 'int':
            value = int(p.get_height())
        else:
            value = '{:.2f}'.format(p.get_height())
        ax.text(_x, _y, value, ha="center")



url_to_test = 'https://raw.githubusercontent.com/TannerGilbert/Tensorflow-Object-Detection-API-Train-Model/master/images/test_labels.csv'
url_to_training = 'https://raw.githubusercontent.com/TannerGilbert/Tensorflow-Object-Detection-API-Train-Model/master/images/train_labels.csv'

#tabelka pierwsza test
df = pd.read_csv(url_to_test, error_bad_lines=False)


unique_classes = df['class'].drop_duplicates()
unique_pictures = df['filename'].drop_duplicates()
nr_of_boxes = len(df)

test_data = [len(unique_classes), len(unique_pictures), nr_of_boxes]

test_table = pd.Series(test_data)
test_table.index = ['Liczba klas', 'Ilość unikalnych zdjęć', 'Ilość bounding boxów']
print('Testy')
print(test_table)

#tabelka pierwsza trening
df2 = pd.read_csv(url_to_training, error_bad_lines=False)

unique_classes = df2['class'].drop_duplicates()
unique_pictures = df2['filename'].drop_duplicates()
nr_of_boxes = len(df2)

training_data = [len(unique_classes), len(unique_pictures), nr_of_boxes]

training_table = pd.Series(training_data)
training_table.index = ['Liczba klas', 'Ilość unikalnych zdjęć', 'Ilość bounding boxów']
print('\nTrening')
print(training_table)


#Zadanie 2.1 Ilość bounding boxów dla każdej klasy
sns.set_style("whitegrid")

counts = df["class"].value_counts().reset_index()
counts['type'] = 'test'
counts2 = df2["class"].value_counts().reset_index()
counts2['type'] = 'training'
c = counts.append(counts2, ignore_index = True)
print(c)

g1 = sns.barplot(x='index', y='class', hue='type', data=c)
g1.set(xlabel='Klasy', ylabel='Bounding boxy', title='Ilość bounding boxów dla każdej klasy')


g1.legend(loc='right', bbox_to_anchor=(1.25, 0.5), ncol=1)
#g2 = sns.barplot(x='index', y='class', hue='type', data=counts2)
show_values_on_bars(g1, type='int')

# Zad 2.2 - Ilość unikalnych zdjęć dla każdej klasy
h = df.groupby(['class', 'filename']).size().reset_index() #  grupowanie po klasach oraz zdjeciach
h = h['class'].value_counts().reset_index()
h['type'] = 'test'

h_training = df2.groupby(['class', 'filename']).size().reset_index()
h_training = h_training['class'].value_counts().reset_index()
h_training['type'] = 'training'

h = h.append(h_training, ignore_index = True)


#gg = sns.barplot(x='index', y='class', hue='type', data=h)
#gg.set(xlabel='Klasy', ylabel='Liczba zdjeć', title='Ilość unikalnych zdjęć dla każdej klasy')
#gg.legend(loc='right', bbox_to_anchor=(1.25, 0.5), ncol=1)
#show_values_on_bars(gg, type='int')




plt.show()
