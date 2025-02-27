def find_closest_price_ending_with_99(product_cost: int) -> int:
    """
    Ingrid is the founder of a company that sells bicycle parts.
    She used to set the prices of products quite arbitrarily, but
    now she has decided that it would be more profitable if the
    prices end in $99$.
    You are given a positive integer $N$, the price of a product. Your task
    is to find the nearest positive integer to $N$ which ends in $99$. If there are two such numbers


    Input
    The input contains one integer $N$ ($1
    \leq N \leq 10^4$), the price of a product. It is
    guaranteed that the number $N$ does not end in $99$.
    Output
    Print one integer, the closest positive integer that ends in
    $99$. In case of a tie,
    print the bigger one.
    """

    below_num = (product_cost // 100) * 100 - 1
    above_num = (product_cost // 100 + 1) * 100 - 1

    if abs(below_num - product_cost) <= abs(above_num - product_cost):
        return below_num
    else:
        return above_num