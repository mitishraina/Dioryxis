# DIORYXIS
Dioryxis is a simple implementation of PERCEPTRON model designed to solve logical operations(AND, OR, XOR) and demonstrate the limitations of single-layer perceptron.

## What is a perceptron?
A Perceptron is a type of artificial neuron used in machine learning. It’s the building block of more complex neural networks. A single perceptron performs binary classification by taking a weighted sum of its inputs, passing it through an activation function (usually a step function), and outputting either 0 or 1. It's essentially a linear classifier.

### How it works?
1. Input: A vector of values(features)
2. Weights: Parameters that adjust the input values
3. Bias: A constant value added to the weighted sum of shift the decision boundary
4. Activation Funciton: A step function that determines if the perceptron should activate or not.

# Note:
One thing that noticed while building was that total_loss of XOR initially started from -2, but then after running it a few times, it went like 2, 2, 2, 2 and so. This is where i noticed that perceptron struggles with XOR, Why?  

Unlike OR and AND, XOR is not linearly separable, so a single layer cant solve it. And how did i reach this conclusion? 
I plotted a simple hyperplane where i couldn't draw a straight line that perfectly separates the output classes(0's & 1's) based on their input value.  

So, overall I got fluctuating loss values suggesting that the perceptron is failing to converge properly on the XOR gate. 

## How to run?

1. Clone the repo:
```bash
git clone https://github.com/yourusername/Dioryxis.git
cd Dioryxis
```
2. Create a conda environment & activate
```bash
conda create -p venv
```

then

```bash
conda activate venv/
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Open terminal and type
```bash
jupyter notebook
```
This will fire up jupyter notebook in your browser, after this inside notebook directory, run Perceptron.ipynb cell by cell.

