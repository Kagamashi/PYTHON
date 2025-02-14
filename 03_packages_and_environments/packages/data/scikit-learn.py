# scikit-learn
# scikit-learn is a machine learning library that provides simple and efficient tools for data mining and analysis.
from sklearn.linear_model import LinearRegression  # type: ignore
model = LinearRegression()
X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]
model.fit(X, y)
print(model.predict([[5]]))
