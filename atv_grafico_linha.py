try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

x = [1, 2, 3, 4, 5, 6, 7]
y = [100, 95, 110, 105, 120, 115, 130]

plt.plot(x, y)
plt.title("Smartphone")
plt.xlabel("Tempo (dias)")
plt.ylabel("Estoque")
plt.show()
