# Runge--Kutta

The project numerically solves a system of first order ordinary differential equations using the 4th order Runge-Kutta method with initial Cauchy conditions. More details can be found in the [Description.pdf](Description.pdf). This is an implementation for a specific equation. To solve an arbitrary problem, you need to change the code.

## Run

Take the files [`models.py`](Python/models.py) and [`main.py`](Python/main.py).



Type in console with Python 3.8

```shell

mkdir pics

python main.py

```

The result of the script will be graphics in the folder `pics/`.



Dependencies may be required:

```shell

pip install numpy

pip install matplotlib

```