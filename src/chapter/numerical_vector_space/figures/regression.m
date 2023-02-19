x = linspace(0, 2, 20)
e = randn(1, 20) ./ 10
y = x .^ 2 - 1.5 .* x + e + 0.5
csvwrite("./regression.csv", transpose(y))
