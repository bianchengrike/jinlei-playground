# Latex code 

# $$
# \begin{align*}
# H(X, Y) - H(Y)
# 			 &= - \sum\limits_{x \in X} \sum\limits_{y \in Y} p(x, y) \log{p(x,y)} + \sum\limits_{y \in Y} p(y) \log{p(y)} \\
# 			 &= - \sum\limits_{x \in X} \sum\limits_{y \in Y} p(x, y) \log{p(x,y)} + \sum\limits_{y \in Y} \big(\sum\limits_{x \in X} p(x,y) \big) \log{p(y)} \\
#        &=  - \sum\limits_{x \in X} \sum\limits_{y \in Y} p(x, y) \log{p(x,y)} + \sum\limits_{x \in X} \sum\limits_{y \in Y} p(x,y) \log{p(y)} \\
#        &= - \sum\limits_{x \in X} \sum\limits_{y \in Y} p(x, y) \log{\frac{p(x,y)}{p(y)}} \\
#        &= - \sum\limits_{x \in X} \sum\limits_{y \in Y} p(x, y) \log{p(y|x)}
# \end{align*}
# $$




# $$
# \begin{align*}
# H(Y|X) &= \sum\limits_{x \in X} p(x) H(Y|X=x) \\
#        &=  \sum\limits_{x \in X} p(x) \times \big( - \sum\limits_{y \in Y} p(y|x) \log{p(y|x)} \big) \\
#        &= - \sum\limits_{x \in X} p(x) \sum\limits_{y \in Y} p(y|x) \log{p(y|x)} \\
#        &= - \sum\limits_{x \in X} \sum\limits_{y \in Y} p(x, y) \log{p(y|x)}
# \end{align*}
# $$



