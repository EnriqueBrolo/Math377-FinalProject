# Math 377 Project

## Modeling Victoria's Growth Using Logistic Growth & the P–S Model

## How to Use

1. **Clone Repo**
```bash
git clone https://github.com/EnriqueBrolo/Math377-FinalProject/edit/master/README.md
cd Math377-FinalProject
```

2.**Edit Values**

Change S/R values in csv file depending on the resource in: 
```bash
math377/data.csv
```

Label each resource, then set S-Values and R-Values in the following format:
```
#ResourceName
s_a,s_b,r_a,r_b
```
Example:
```
#Water
0.00050395,0.000205,216.7, 250
```
3.**Run graphs.py**
```bash
python graphs.py
```
