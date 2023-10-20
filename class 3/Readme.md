# Python crashe course

# Chapter 2 

- Python divides the operators in the following groups:

* Arithmetic operators
* Assignment operators
* Comparison operators
* Logical operators
* Identity operators
* Membership operators
* Bitwise operators

- Arithmetic operators are used with numeric values to perform common mathematical operations:

* Operator	               Name	                       Example                            	
*     +	                 Addition	                    x + y	
*     -	                Subtraction                    	x - y	
*     *	                Multiplication                 	x * y	
*    /	                  Division	                    x / y	
*    %	                  Modulus                   	x % y	
*    **	               Exponentiation                 	x ** y	
*    //	               Floor division                   x // y

- Assignment operators are used to assign values to variables:

*  Operator	           Example        	Same As
*   =                   x = 5       	x = 5	
*  +=	                x += 3      	x = x + 3	
*  -=	                x -= 3	        x = x - 3	
*  *=	                x *= 3	        x = x * 3	
*  /=	                x /= 3	        x = x / 3	
*  %=	                x %= 3	        x = x % 3	
*  //=	                x //= 3	        x = x // 3	
*  **=	                x **= 3	        x = x ** 3	
*  &=	                x &= 3	        x = x & 3	
*  |=	                x |= 3	        x = x | 3	
*  ^=	                x ^= 3	        x = x ^ 3	
*  >>=	                x >>= 3      	x = x >> 3	
*  <<=	                x <<= 3     	x = x << 3

- Comparison operators are used to compare two values:

*    Operator	      Name	                   Example	
*      ==	         Equal	                    x == y	
*      !=	        Not equal	                x != y	
*      > 	      Greater than    	            x > y	
*      <	       Less than	                x < y	
*      >=	  Greater than or equal to  	    x >= y	
*      <=	   Less than or equal to	        x <= y

- ASCII Code

* Z = 90

* a = 97
* z = 122 

* 0 = 48 
* 9 = 57

- Logical operators are used to combine conditional statements:

* Operator	                   Description	                                       Example	
* and 	        Returns True if both statements are true	                   x < 5 and  x < 10	
* or	     Returns True if one of the statements is true	                     x < 5 or x < 4	
* not	  Reverse the result, returns False if the result is true

- Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

* Operator	 Description	Example	Try it
* is 	Returns True if both variables are the same object	x is y	
* is not	Returns True if both variables are not the same object	x is not y

- To solve the equation step by step, follow the order of operations (PEMDAS/BODMAS), which stands for Parentheses/Brackets, Exponents/Orders (i.e., powers and square roots, etc.), Multiplication and Division (left-to-right), and Addition and Subtraction (left-to-right).

* The given equation is:

2 + 3 - 2 * 4/2 + 2

* First, perform the multiplication and division from left to right:

2 + 3 - 2 * 4/2 + 2
2 + 3 - 8/2 + 2
2 + 3 - 4 + 2

* Next, perform the addition and subtraction from left to right:

2 + 3 - 4 + 2
5 - 4 + 2

* Continue with the addition and subtraction:

5 - 4 + 2
1 + 2

* Finally, perform the last addition:

1 + 2
3

* So, the solution to the equation 2 + 3 - 2 * 4/2 + 2 is 3.