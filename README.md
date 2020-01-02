Solving partial differential equation (2d heat equation) numerically using finite-difference method 
<h1>Finite-difference method </h1>

Сonditions
 
Thin rectangular plate has been put into environment that is being exposed to temperature.</br>
The plate is isolated from everywhere except the edges, there constant temperatures are maintained.

Little thickness of the plate and its isolation allow us to consider heat distribution as one taking place on the (x,y) plane.</br>
In a plate with a static position temperature distribution is discribed with Laplace's Heat Equation:

![alt text](https://raw.githubusercontent.com/deepwebhoax/finiteDifferencesDE/master/img1.png)
           
where  Т(x, y) – temperature in the point (x, y).

The numerical solution to this equation we get using finite-difference method.

Example of a problem:</br>
Calculate temperatures in points

![alt text](https://raw.githubusercontent.com/deepwebhoax/finiteDifferencesDE/master/img2.png)

Results provided by my program:

![alt text](https://raw.githubusercontent.com/deepwebhoax/finiteDifferencesDE/master/img3.png)
