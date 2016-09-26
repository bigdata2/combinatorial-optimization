# Problem Description
A combinatorial optimization problem to assign products to customers based on suitability score.

A marketing department has just negotiated a deal with several local merchants that will allow it to offer exclusive discounts on various products to its top customers every day. The catch is that it can only offer each product to one customer and it may only offer one product to each customer.

Each day the marketing department will get the list of products that are eligible for these special discounts. It then have to decide which products to offer to which of our customers. A team of statisticians has developed a mathematical model for determining how likely a given customer is to buy an offered product by calculating what it call the "suitability score" (SS). The algorithm to calculate the SS between a customer and a product is this: 

1. If the number of letters in the product's name is even then the SS is the number of vowels (a, e, i, o, u, y) in the customer's name multiplied by 1.5. 
2. If the number of letters in the product's name is odd then the SS is the number of consonants in the customer's name. 
3. If the number of letters in the product's name shares any common factors (besides 1) with the number of letters in the customer's name then the SS is multiplied by 1.5. 

Your task is to implement a program that assigns each customer a product to be offered in a way that maximizes the combined total SS across all of the chosen offers. Note that there may be a different number of products and customers. You may include code from external libraries as long as you cite the source.

###INPUT SAMPLE:

Your program should accept as its only argument a path to a file. Each line in this file is one test case. Each test case will be a comma delimited set of customer names followed by a semicolon and then a comma delimited set of product names. Assume the input file is ASCII encoded. For example (NOTE: The example below has 3 test cases): 

```Jack Abraham,John Evans,Ted Dziuba;iPad 2 - 4-pack,Girl Scouts Thin Mints,Nerf Crossbow```

```Jeffery Lebowski,Walter Sobchak,Theodore Donald Kerabatsos,Peter Gibbons,Michael Bolton,Samir Nagheenanajar;Half & Half,Colt M1911A1,16lb bowling ball,Red Swingline Stapler,Printer paper,Vibe Magazine Subscriptions - 40 pack```

```Jareau Wade,Rob Eroh,Mahmoud Abdelkader,Wenyi Cai,Justin Van Winkle,Gabriel Sinkin,Aaron Adelson;Batman No. 1,Football - Official Size,Bass Amplifying Headphones,Elephant food - 1024 lbs,Three Wolf One Moon T-shirt,Dom Perignon 2000 Vintage
OUTPUT SAMPLE:```

For each line of input, print out the maximum total score to two decimal places. For the example input above, the output should look like this:

21.00 

83.50

71.25

# Solution
This program was was developed and tested using Python 2.7.11. In addition to  the standard Python modules a user will have to install the Munkres Python module. 

It can be installed by executing the following command on MAC OS or Linux: 

        sudo easy_install munkres

To run the program issue the following command from command line:

        python assignment.py test.in

The problem of assigning each product to a customer is a combinatorial optimization problem. One of the algorithms to solve this is called the Munkres algorithm a.k.a the Hungarian algorithm. While the Munkres algorithm is designed to find the minimum cost, with a minor modifiction in the cost, it can be used to find the maximum cost.

I found a Python implementation of the Munkren algorithm below.  
https://github.com/bmc/munkres
this module takes a cost matrix as input and returns the index of the  elements that constitute the minimum cost. I used this module in my code. 

The Python implementation of maximum suitability score (SS) calculation first  reads the input from a file and create customer and product objects. A SS matrix is then created and populated with the SS between various customers and products. In order to find the maximum and not minimum SS, the maximum SS in the matrix is identified and each element in the matrix is then subtracted from that maximum SS. The effect of doing that is to invert the cell values -- the largest cells become smallest and the smallest cells become largest. This tranformation is done by a function "Munkres.make_cost_matrix" by providing a lambda function to it.

The cost matrix (inverse of SS matix) is then provided to the Munkres module to compute indices of the cells that constitute the lowest cost. Those indices are then used to pick corresponding cells from the original SS matrix and their values are aggregated. The aggregated value represents the maximum SS value.

In addition to the 3 tests provided with this coding challange, a few more test-cases were created to test this algorithm and are contained in test.in file.
