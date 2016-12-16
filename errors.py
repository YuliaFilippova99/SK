def y(t):
    v0 = 5  
    g = 9.81
    return v0 * t - 0.5 * g * t ** 2
t = 0.6
print(y(t))
t = 0.9
print(y(t))

# 1 ст. - SyntaxError: invalid syntax
# 2 ст. - Ничего не изменилось
# 3 ст. - Ничего не изменилось
# 4 ст - SyntaxError: invalid syntax

