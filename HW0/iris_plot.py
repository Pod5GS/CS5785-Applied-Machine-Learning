#!/usr/bin/env python
"""
This script read Iris dataset, and output the scatter plot of the dataset.
Be sure the Iris dataset file is in the 'dataset' directory.
"""
from matplotlib import pyplot as plt
import numpy


# This function draw the labels
def draw_label(fig, label, index):
    """
    :param fig: The figure instance
    :param label: The text shown in the subplot
    :param index: The index of subplot
    """
    ax = fig.add_subplot(4, 4, index)
    ax.set_xticks(())  # get rid of x axis
    ax.set_yticks(())  # get rid of y axis
    ax.text(0.5,  # x coordinate, 0 leftmost positioned, 1 rightmost
            0.5,  # y coordinate, 0 topmost positioned, 1 bottommost
            label,  # the text which will be printed
            horizontalalignment='center',  # set horizontal alignment to center
            verticalalignment='center',  # set vertical alignment to center
            fontsize=20,  # set font size
            )


# This function read Iris dataset into arrays and draw the scatter plot
def iris_plot():
    attributes = []  # N * p array
    labels = []  # label of each line of data
    for line in open("F:\Cornell Tech\HW\CS5785-AML\HW0\dataset\iris.data.txt"):
        if not line.split():
            continue
        attributes.append(line.split(',')[:4])  # first 4 elements are attributes
        labels.append(line.split(',')[-1].strip('\n'))  # last element is label, strip the '\n'
    attributes = numpy.array(attributes)  # convert N * p array to Numpy array
    for i in range(len(labels)):  # assign colors for each label
        if labels[i] == 'Iris-setosa':
            labels[i] = 'r'
        elif labels[i] == 'Iris-versicolor':
            labels[i] = 'g'
        else:
            labels[i] = 'b'
    fig = plt.figure(figsize=(15., 15.))  # set figure size
    fig.suptitle('Iris Data(red=setosa, green=versicolor, blue=virginica)', fontsize=30)  # set figure title
    count = 1  # variable used to track current sub figure to draw
    for x in range(4):
        for y in range(4):
            if x == y:  # when x equal to y, draw label
                if x == 0:
                    draw_label(fig, 'Sepal.Length', count)
                elif x == 1:
                    draw_label(fig, 'Sepal.Width', count)
                elif x == 2:
                    draw_label(fig, 'Petal.Length', count)
                elif x == 3:
                    draw_label(fig, 'Petal.Width', count)
            else:  # else draw the scatter plot of every 2 combinations of those 4 attributes
                xs = numpy.array(attributes.T[y])
                ys = numpy.array(attributes.T[x])
                ax = fig.add_subplot(4, 4, count)
                ax.scatter(xs, ys, c=labels)
            count += 1
    fig.savefig('plot.png')  # save the figure

if __name__ == '__main__':
    iris_plot()
