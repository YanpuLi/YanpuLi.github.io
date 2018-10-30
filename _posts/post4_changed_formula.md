line 44:
The problem becomes:

<img src="https://latex.codecogs.com/svg.latex? 
p^* = {min_{w,b}} {\theta (w)} = {min_{w,b}} max_{(\alpha}_i >0) (\mathcal  {L}(w, b, \alpha))}" title="p" />
 
The dual problem is:

<img src="https://latex.codecogs.com/svg.latex? d^* = max_{{\alpha}_i >0} {min_{w,b}} {\mathcal  {L}(w, b, \alpha)}" title="p" />

Details of this transformation is shown at the end of this blog.

line 97:

The corresponding Lagrange formula:
<img src="https://latex.codecogs.com/svg.latex? {\mathcal  {L}(w, \alpha, \beta)} = f(w) + \sum^k_{i=1} {\alpha_i*g_i(w)} + \sum^l_{i=1} {{\beta}_i*h_i(w)}" title="p" />

The problem becomes: 

<img src="https://latex.codecogs.com/svg.latex? \theta_p{(w)} = max_{\alpha, \beta: \alpha_i >0} {\mathcal  {L}(w, \alpha, \beta)}" title="p" /> with θ<sub>p</sub>(w) = f(w), if w satisfies the constraints, otherwise, θ<sub>p</sub>(w) = ∞. So our goal is to minimize θ<sub>p</sub>(w), which is <img src="https://latex.codecogs.com/svg.latex? min_w {\theta}_p{(w)} = {min_w} max_{\alpha, \beta: {\alpha}_i >0} {\mathcal  {L}(w, \alpha, \beta)}" title="p" />

Set the duality problem:

<img src="https://latex.codecogs.com/svg.latex? {\theta}_D{(\alpha, \beta)} = min_w {\mathcal  {L}(w, \alpha, \beta)}" title="p" />

<img src="https://latex.codecogs.com/svg.latex? max_{\alpha, \beta: {\alpha}_i >0} {{\theta}_D{(\alpha, \beta)}} = max_{\alpha, \beta: {\alpha}_i >0} min_w {\mathcal  {L}(w, \alpha, \beta)}" title="p" />

<img src="https://latex.codecogs.com/svg.latex? d^* = max_{\alpha, \beta: {\alpha}_i >0} min_w {\mathcal  {L}(w, \alpha, \beta)}" title="p" />

<img src="https://latex.codecogs.com/svg.latex? p^* = {min_w} max_{\alpha, \beta: {\alpha}_i >0} {\mathcal  {L}(w, \alpha, \beta)}" title="p" />

<img src="https://latex.codecogs.com/svg.latex? d^* <= p^* " title="p" />