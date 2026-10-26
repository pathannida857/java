# res=lambda x,y:x+y
# p=10
# q=20
# res=(p,q)

# res=lambda x,y:print(x+y)
# p=10
# q=20
# # res=(p,q)
# print(res(p,q))

# l=[1,2,3,4,5,6]
# res=map(lambda n:n+5,l)
# print(list(res))

# l=[1,2,3,4,5,6]
# res=filter(lambda n:n%2==0,l)
# print(list(res))

# l=[1,2,3,4,5,6]
# res=filter(lambda n:n%2!=0,l)
# print(list(res))

# from functools import reduce
# l=[1,2,3,9,4,5,6]
# res= reduce(lambda n1,n2:n1 if n1>n2 else n2,l)
# print(res)

# from functools import reduce
# l=[1,2,3,9,4,5,6]
# res= reduce(lambda n1,n2:n1 if n1<n2 else n2,l)
# print(res)


# from functools import reduce
# n=int(input("please enter num"))
# l=[1,3,2,9,4,5,6]
# for i in range(n): 
#   res= reduce(lambda n1,n2:n1 if n1>n2 else n2,l)
#   l.remove(res)
# print(res)

# from functools import reduce
# n=int(input("please enter num"))
# l=[1,3,2,9,4,5,6]
# for i in range(n): 
#   res= reduce(lambda n1,n2:n1 if n1<n2 else n2,l)
#   l.remove(res)
# print(res)


