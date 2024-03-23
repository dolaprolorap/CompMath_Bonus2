from sympy import symbols, sin, ceiling, latex, plot, Mod 

x = symbols("x")

# Гладкая и негладкая функции
smooth_func = sin(x)  
unsmooth_func = (-1) ** (Mod(ceiling(x), 2))

# Их подписи на легенде
smooth_label = f"${latex("sin(x)")}$"
unsmooth_label = "$(-1)^{ceil(x) \ mod \ 2}$"

def lagrange_poly(dots, func):
    def l(dots, j):
        monom = 1 + 0 * x
        for i in range(len(dots)):
            if i != j:
                monom *= ((x - dots[i]) / (dots[j] - dots[i]))
        return monom
    lagrange = 0 + 0 * x
    for i in range(len(dots)):
        lagrange += func.subs(x, dots[i]) * l(dots, i)
    return lagrange

def make_dots(domain, dots_count):
    l, r = domain
    if dots_count == 2:
        return [l, r]
    h = (r - l) / (dots_count - 1)
    return [l + i * h for i in range(dots_count)]

# Исходная функция
func = unsmooth_func
# Название исходной функции на легенде графика
plot_label = unsmooth_label
# Область определения функции
domain = [-5, 5]
# Количетво точек
dots_cnt = 40

p1 = plot(func, (x, -5, 5), xlim=(-8, 8), ylim=(-8, 8), xlabel="", ylabel="", show=False, legend=True, label=plot_label)
p2 = plot(lagrange_poly(make_dots(domain, dots_cnt), func), (x, -5, 5), show=False, line_color='red', label=f'Lagrange ({dots_cnt} dots)')
p1.append(p2[0])
p1.show()
