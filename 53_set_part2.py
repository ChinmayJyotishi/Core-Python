# methods for mathematical use

# UNION
# s={12,25,6,89,78}
# s1={12,36,89,88,78}
# print(s.union(s1))
# print(s|s1)
# s.update(s1)
# print(s)

# intersection
# s={12,25,6,89,78}
# s1={12,36,89,88,78}
# print(s.intersection(s1))
# print(s & s1)

# difference
# s={12,25,6,89,78}
# s1={12,36,89,88,78}
# print(s.difference(s1))
# print(s - s1)
# print(s1.difference(s))
# print(s1 - s)

# symmetric difference 
# it will return the non common things only 
s={12,25,6,89,78}
s1={12,36,89,88,78}
print(s.symmetric_difference(s1))
print(s ^ s1)


# isSubset
# s={1,2,3,56,45,89,6,48,8}
# s1={1,2,3}
# print(s1.issubset(s))
# it is mendatory to have some or all the element of superset to be a subset

# superset
# s={1,2,3,56,45,89,6,48,8}
# s1={1,2,3}
# print(s.issuperset(s1))


# disjoint==notcommon/no relation
s={22,56,98,669,6,4}
s1={25,1,2,3}
print(s.isdisjoint(s1))
# it will return as true n false



