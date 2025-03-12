def max_k_collections(n, collections):
    for i in xrange(n):
        shapes = [0]*37
        decors = [0]*37
        for shape, decor in collections[i]:
            shapes[shape] += 1
            decors[decor] += 1
        shapes.sort()
        decors.sort()
        for k in xrange(36, 0, -1):
            if sum(shapes[-k:]) >= k and sum(decors[-k:]) >= k:
                print(k)
                break
                
n = 3
collections = [
    [(1,1), (2,2), (3,3)],
    [(1,2), (2,3), (3,4)],
    [(1,1), (2,2), (3,3), (4,4), (5,5)]
]
max_k_collections(n, collections)