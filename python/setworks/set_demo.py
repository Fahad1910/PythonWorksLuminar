# st={} it will take as dictionary
# st={10,20} it take as set
# st=set() we can call empty set by calling set() method


# st1={10,20,11,12}
# st2={20,21,11,30,40}

# union_set=st1.union(st2)
# print(union_set)


# intersection_set=st1.intersection(st2)
# print(intersection_set)

# difference_set=st1.difference(st2)
# print(difference_set)

# st1.remove(20)
# print(st1)

# st1.discard(10)
# print(st1)

# st1.pop()
# print(st1)

# st.add(200)
# print(st)


st1={4,5,2,8}
st2={2,8,6,7}

symm_diff=st1.symmetric_difference(st2)
print(symm_diff)







# set methods =>
# add()
# union()
# intersection()
# difference()
# remove()
# discard()
# pop()
# symmetric_difference()


# {10,20}=>

# duplicate value not allowed - every object is unique
# insertion order not preserved
# set does not support indexing
# set can be updated - mutable
# union() is used to find the union of the two set
# intersection() is used to find common elements of the two set
# difference () = the elements from set 1 are removed from  set 2
# remove() = remove object from a set
# discard() = remove object from the set
# pop() = remove random object
# symmetric difference() = remove the common from both set  