<H1 id="up" align="center"><H1>Basics Of Discrete Math </H1>

<details>
  <summary>Navigation</summary>
  <ol >
    <li>
        <a href="#info">About The Project</a>
        <ul>
            <li>
                <a href="#operaions">About Operations</a>
                <ul>
                    <li><a href="#sets">Operations on Set</a></li>
                    <li><a href="numberPerm">Number of permutations</a></li>
                    <li><a href="numberPlace">Number placements</a></li>
                    <li><a href="numberComb">Number Of Combinations</a></li>
                </ul>
            </li>
        </ul>
        <ul>
            <li><a href="#build_with">Build With</a></li>
        </ul>
    </li>
  </ol>
</details>


<H2 id="info"> General Info </H2>

It's the biggest project what I tried to do

I tried to do something what I need, it's <a href="https://basicsofdiscretemath.onrender.com/">site with basic discrete math's operations</a>

After I did most of the parts, I'll know python have set() function, and I was like :neutral_face:  'cause I did functions by myself

It's not a super well code, and he can be better, but I did it by myself and I think with that fact it's kinda ok.

And site has kinda "adaptation" for mobiles and laptops

I think I'll update some functions, 'cause I didn't add all what I want. And refactoring of course

<H3 id="operations"> About Operations </H3>

<H4 id="sets">Operations on set</H4>

    A = { 1, 2, 3, 4 }
    
    B = { 3, 4, 5, 6 }

- **Merge**

    Write the elements of the set A and B in ascending order; if an element occurs >1 time, write it once
    
    A ⋃ B = { 1, 2, 3, 4, 5, 6 }


- **Intersection**

    Write out identical elements from A and B

    A ⋂ B = { 3, 4 }


- **Difference**

    A \ B - Rewrite A, removing elements that are in B
    
    A \ B = { 1, 2 }


- **Symmetrical Difference**

    Write out elements from A ⋃ B, removing elements from A ⋂ B
    
    A △ B = { 1, 2, 5, 6}


- **Complement**

        U = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    
        X = {1, 2, 3, 4}  

    Write the elements of the set U by removing elements from set X ( X can be A′ or B′ )
    
    X′ = { 5, 6, 7, 8, 9}


<H4 id="numberPerm">Number of Permutations</H4> 

**Calculating the number of permutations of n elements**

The number of permutations Pn is the number of different ways in which a given set consisting of n elements can be ordered.

P_n = n! = P₁₀ = 10! = 3628800


<H4 id="numberPlace">Number Placements</H4> 

**Calculating the number of placements of n by k elements**

The number of placements of Ank is the arrangement of “items” on some “places”, provided that each place is occupied by exactly one object and all objects are different. More formally, an arrangement (from n to k) is an ordered set of k distinct elements of some n-element set.

A_9^2 = 9!/(9-2)! = 9!/7! = 72


<H4 id="numberComb">Number of Combination</H4> 

**Calculating the number of combinations of n by k elements**

The number of combinations from n to k (C_n^k) is a set of k elements selected from given n elements. Sets that differ only in the order of elements (but not in composition) are considered identical.

C_9^2 = 9!/(9-2)! * 2! = 9!/7! * 2! = 36

<H3 id="build_with"> Build With: </H3>

* <a href="https://flask.palletsprojects.com/en/3.0.x/">Flask</a>
* <a href="https://flask-wtf.readthedocs.io/en/1.2.x/">Flask WTF</a>
* <a href="https://wtforms.readthedocs.io/en/3.1.x/">WTForms</a>
* <a href="https://render.com/">Render</a>


