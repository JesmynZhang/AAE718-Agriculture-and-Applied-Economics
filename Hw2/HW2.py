import numpy as np
import matplotlib.pyplot as plt
import time

def problem_02(a, b, c):
    array = np.random.uniform(a, b, 100)
    mask = array < c
    return np.sum(mask)
if __name__ == "__main__":
    pass

def problem_03():
    array = np.random.rand(5, 5)
    result = array[[0, 2, 3], :][:, [1, 2, 3, 4]]
    return result
if __name__ == "__main__":
    pass

def problem_04(N):
    array = np.ones((N, N))
    array[1:-1, 1:-1] = 0
    return array
if __name__ == "__main__":
    pass

#Problem_05
def least_squares_error(x, y):
    return np.sum((x - y) ** 2)

if __name__ == "__main__":
   pass

#Problem_06
def normalized_random(N):
    array = np.random.rand(N, N)
    array = array / array.sum(axis=1, keepdims=True)
    return array

if __name__ == "__main__":
    pass

#Problem_07
x1 = np.linspace(0, 10, 1000)
y1 = x1 ** 2

plt.figure()
plt.plot(x1, y1, label="f(x) = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of f(x) = x^2")
plt.legend()
plt.grid(True)
plt.savefig("plot_x_squared.png")  
plt.show()


x2 = np.linspace(-np.pi, np.pi, 1000)
y2_sin = np.sin(x2)
y2_cos = np.cos(x2)

plt.figure()
plt.plot(x2, y2_sin, label="f(x) = sin(x)")
plt.plot(x2, y2_cos, label="g(x) = cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of f(x) = sin(x) and g(x) = cos(x)")
plt.legend()
plt.grid(True)
plt.savefig("plot_sin_cos.png")  
plt.show()


x3 = np.linspace(0, 5, 1000)
y3_arctan = np.arctan(x3)
y3_sigmoid = 1 / (1 + np.exp(-x3))

plt.figure()
plt.plot(x3, y3_arctan, label="f(x) = arctan(x)")
plt.plot(x3, y3_sigmoid, label="g(x) = 1 / (1 + e^-x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of f(x) = arctan(x) and g(x) = 1 / (1 + e^-x)")
plt.legend()
plt.grid(True)
plt.savefig("plot_arctan_sigmoid.png")  
plt.show()

#Problem_08

def sort_times():
    
    array_times = []
    list_times = []

    for _ in range(10):
        L = np.random.randint(0, 10000000, size=10000000).tolist()
        a = np.array(L)
        start = time.time()
        np.sort(a)
        end = time.time()
        array_times.append(end - start)
        start = time.time()
        L.sort()
        end = time.time()
        list_times.append(end - start)

    print("Sorting times for array (10 runs):", array_times)
    print("Sorting times for list (10 runs):", list_times)


    array_times_small_range = []
    list_times_small_range = []
    for _ in range(10):
        L = np.random.rand(10000000).tolist()
        a = np.array(L)

        start = time.time()
        np.sort(a)
        end = time.time()
        array_times_small_range.append(end - start)

        start = time.time()
        L.sort()
        end = time.time()
        list_times_small_range.append(end - start)

    print("Sorting times for array with values between 0 and 1 (10 runs):", array_times_small_range)
    print("Sorting times for list with values between 0 and 1 (10 runs):", list_times_small_range)

sort_times()
