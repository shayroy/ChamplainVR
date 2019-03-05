import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_values = [10, 20, 30, 40, 50]

plt.figure(dpi=128, figsize=(10, 6))
plt.plot(squares)
# can show two series on the same graph, in this case the previous and the next line.
plt.scatter(input_values, squares, linewidth=5, c=squares, cmap=plt.cm.Reds)
plt.axis([0, 100, 0, 100])
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)


plt.show()




