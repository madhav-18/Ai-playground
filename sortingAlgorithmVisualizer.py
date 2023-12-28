from tkinter import *
from tkinter import ttk
import random
from BubbleSort import BubbleSort
from QuickSort import QuickSort
from MergeSort import MergeSort
from InsertionSort import InsertionSort

# Generates a black window; Background for GUI
root = Tk()  # Boots up the tkinter module
root.title('AI-Playground')
root.maxsize(1500, 600)
root.config(bg='White')

# variables & functions
selectedAlgorithm = StringVar()
data = []


# Draws the rectangle that represent the data value onto the canvas
def drawDataArray(data, colorArray):
    canvas.delete("all")  # Delete data values from canvas from previous use of drawDataArray
    canvas_height = 380
    canvas_width = 1400
    bargraph_width = canvas_width / (len(data) + 1)
    offset = 5  # needed so that the bars don't start at the border of the screen
    spacing_between_bars = 5

    normalizedData = [i / max(data) for i in data]
    # to make sure the height of the bars are relative and seeable in the GUI

    for i, height in enumerate(normalizedData):
        # x1, y1 are coordinates of the top left  needed to create the rectangle for each data
        x1 = i * bargraph_width + offset + spacing_between_bars
        y1 = canvas_height - height * 340
        # x2, y2 are coordinates of the bottom right needed to create the rectangle for each data
        x2 = (i + 1) * bargraph_width + offset
        y2 = canvas_height

        canvas.create_rectangle(x1, y1, x2, y2, fill=colorArray[i])
        canvas.create_text(x1, y1, anchor=SW,
                           text=str(data[i]))  # Writes the numbers over the bar representing the data

    # Shows how the data array changes step by step once an algorith has started
    root.update()


# Generates a new random array of data values using the constraints of minValue, maxValue, and arraySize
def GenerateNewArray():
    canvas.delete("all")  # Delete data values from canvas from previous use of drawDataArray

    global data

    minValue = int(minValueScale.get())
    maxValue = int(maxValueScale.get())
    arraySize = int(arraySizeScale.get())

    data = []

    for _ in range(arraySize):
        data.append(random.randrange(minValue, maxValue + 1))

    drawDataArray(data, ['#FAF7F0' for x in range(len(data))])


# Calls upon the sorting algorithm the user has chosen to use
def StartSortingAlgorithm():
    global data

    # If data is empty then return out of it 
    if not data:
        return

    if algorithmList.get() == 'Quick Sort':
        QuickSort(data, 0, len(data) - 1, drawDataArray, sortingSpeedScale.get())

    elif algorithmList.get() == 'Bubble Sort':
        BubbleSort(data, drawDataArray, sortingSpeedScale.get())

    elif algorithmList.get() == 'Merge Sort':
        MergeSort(data, drawDataArray, sortingSpeedScale.get())

    elif algorithmList.get() == 'Insertion Sort':
        InsertionSort(data, drawDataArray, sortingSpeedScale.get())

    # After going through the double for loop, the array should be sorted therefore all bars should be blue
    drawDataArray(data, ['#CDFCF6' for x in range(len(data))])


# Generates the background User Interface area of the GUI
UserInterfaceFrame = Frame(root, width=1400, height=200, bg='#293462')
UserInterfaceFrame.grid(row=0, column=0, padx=0, pady=0)

# Generates the background / canvas where the bars of data will be drawn on 
canvas = Canvas(root, width=1400, height=380, bg='#FEDB39', highlightthickness=0)
canvas.grid(row=1, column=0, padx=0, pady=0)

# User Interface Area - Text Boxes, Buttons, etc.

Label(UserInterfaceFrame, text="Choose Algorithm --> ", bg='#FEDB39').grid(row=0, column=0, padx=5, pady=5,
                                                                           sticky=W)  # W for west aka left
#Drop Down Section
algorithmList = ttk.Combobox(UserInterfaceFrame, textvariable=selectedAlgorithm,
                             values=['Bubble Sort', 'Quick Sort', 'Merge Sort', 'Insertion Sort'])
algorithmList.grid(row=0, column=1, padx=5, pady=5)
algorithmList.current(0)  # chooses Bubble Sort by default since it is in index 0

#Speed Section
sortingSpeedScale = Scale(UserInterfaceFrame, from_=0.1, to=5.0, length=200, digits=2, resolution=0.1,
                          orient=HORIZONTAL, label="Sorting Speed [sec]", bg="#DFD3C3")
sortingSpeedScale.grid(row=0, column=2, padx=5, pady=5)

#Starting algorithm
Button(UserInterfaceFrame, text="Start Sorting Algorithm", command=StartSortingAlgorithm, bg="Green", borderwidth=8).grid(row=0,
                                                                                                           column=3,
                                                                                                           padx=5,
                                                                                                           pady=5)

# Array section
arraySizeScale = Scale(UserInterfaceFrame, from_=3, to=100, resolution=10, orient=HORIZONTAL, label="Array Size",bg="#DFD3C3")
arraySizeScale.grid(row=1, column=0, padx=5, pady=5)

# Min scale value section
minValueScale = Scale(UserInterfaceFrame, from_=0, to=10, resolution=1, orient=VERTICAL, label="Min Value", bg="#DFD3C3")
minValueScale.grid(row=1, column=1, padx=5, pady=5)

# Max scale value section
maxValueScale = Scale(UserInterfaceFrame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value", bg="#DFD3C3")
maxValueScale.grid(row=1, column=2, padx=5, pady=5)

# Button to Generate New Random Array of Data Values
Button(UserInterfaceFrame, text="Generate New Random Array", command=GenerateNewArray, bg='#FD841F', borderwidth=8).grid(row=1, column=3,
                                                                                                        padx=5, pady=5)

root.mainloop()
