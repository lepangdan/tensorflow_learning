# empty = 'empty'
#
#
# def is_link(s):
#     """s is a linked list if it is empty or a (first, rest) pair"""
#     return s == empty or (len(s) == 2 and is_link(rest(s)))
#
#
# def link(first_s, rest_s):
#     """construct a linked list from its first element and rest"""
#     assert is_link(rest_s), "rest must be a linked list."
#     return [first_s, rest_s]
#
#
# def first(s):
#     """Return the first element of a linked list s."""
#     assert is_link(s), "first only applies to linked lists."
#     assert s != empty, "empty linked list has no first element."
#     return s[0]
#
#
# def rest(s):
#     """Return the rest of the elements of a linked list s."""
#     # assert is_link(s), "rest only applies to linked lists."
#     # assert s != empty, "empty linked list has no rest."
#     return s[1]
#
#
# def extend_link(s, t):
#     """Return a list with the elements of s followed by those of t."""
#     assert is_link(s) and is_link(t)
#     if s == empty:
#         return t
#     else:
#         return link(first(s), extend_link(rest(s), t))
#
#
# def apply_to_all_link(f, s):
#     """Apply f to each element of s."""
#     assert is_link(s)
#     if s == empty:
#         return s
#     else:
#         return link(f(first(s)), apply_to_all_link(f, rest(s)))
#
#
# def partitions(n, m):
#     """Return a linked list of partitions of n using parts of up to m.
#     Each partition is represented as a linked list"""
#     if n == 0:
#         return link(empty, empty)
#     elif n < 0 or m == 0:
#         return empty
#     else:
#         using_m = partitions(n-m, m)
#         # print('m',m)
#         with_m = apply_to_all_link(lambda s: link(m, s), using_m)
#         # print('with_empty',with_m)
#         without_m = partitions(n, m - 1)
#         # print('without_m',without_m)
#         return extend_link(with_m, without_m)
#
# print(partitions(2,2))

# def is_sort(n):
#     if n < 10:
#         return True
#     else:
#         return is_sort(n // 10) and (((n // 10) % 10) >= (n % 10))
#
# print(is_sort(2))
# print(is_sort(22222))
# print(is_sort(9876543210))
# print(is_sort(9087654321))

#
# def mario_number(level):
#     if level == 1:
#         return 1
#     elif level % 10 == 0:
#         return 0
#     else:
#         return mario_number(level // 10) + mario_number(level // 100)
#
# print(mario_number(10101))
# print(mario_number(11101))
# print(mario_number(100101))


# def make_change(n):
#
#     if n == 1 or n == 3 or n == 4:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         use1=1+make_change(n-1)
#         use3=1+make_change(n-3)
#         use4=1+make_change(n-4)
#         return min(use1, use3, use4)
#
# print(make_change(10))

# def elephant(name, age, can_fly):
#     return [name, age, can_fly]
#
# def elephant_name(elephant):
#     return elephant[0]
#
# def elephant_age(elephant):
#     return elephant[1]
#
# def elephant_can_fly(elephant):
#     return elephant[2]
#
# dumbo=elephant("Dumbo", 10, True)
# print(elephant_name(dumbo))
# print(elephant_age(dumbo))
# print(elephant_can_fly(dumbo))


# def elephant (name, age, can_fly):
#     def select(command):
#         if command == "name":
#             return name
#         elif command == "age":
#             return age
#         elif command == "can_fly":
#             return can_fly
#
#     return select
# def elephant_name(e):
#     return e("name")
# def elephant_age(e):
#     return e("age")
# def elephant_can_fly(e):
#     return e("can_fly")
#
# chris=elephant("Christs Martin", 38, False)
# print(elephant_name(chris))
# print(elephant_age(chris))
# print(elephant_can_fly(chris))

# class Car(object):
#     num_wheels = 4
#     gas = 30
#     headlights = 2
#     size = 'Tiny'
#
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#         self.color = 'No color yet. You need to paint me.'
#         self.wheels = Car.num_wheels
#         self.gas = Car.gas
#
#     def paint(self, color):
#         self.color = color
#         return self.make + ' ' + self.model + ' is now ' + color
#
#     def drive(self):
#         if self.wheels < Car.num_wheels or self.gas <= 0:
#             return self.make + ' ' + self.model + ' cannot drive!'
#         self.gas -= 10
#         return self.make + ' ' + self.model + ' goes vroom!'
#
#     def pop_tire(self):
#         if self.wheels > 0:
#             self.wheels -= 1
#
#     def fill_gas(self):
#         self.gas += 20
#         return self.make + ' ' + self.model + ' gas level: ' + str(self.gas)
#
#
# class MonsterTruck(Car):
#     size = 'Monster'
#
#     def rev(self):
#         print('Vroom! This Monster Truck is huge!')
#
#     def drive(self):
#         self.rev()
#         return Car.drive(self)
#
#
# class FoodTruck(MonsterTruck):
#     delicious = 'meh'
#     def serve(self):
#         if FoodTruck.size == 'delicious':
#             print('Yum!')
#         if self.food != 'Tacos':
#             return 'But no tacos...'
#         else:
#             return 'Mmm!'
#
# taco_truck = FoodTruck('Tacos', 'Truck')
# taco_truck.food = 'Guacamole'
# taco_truck.serve()
# taco_truck.food = taco_truck.make
# FoodTruck.size = taco_truck.delicious
# taco_truck.serve()
# taco_truck.size = 'delicious'
# taco_truck.serve()
# #FoodTruck.pop_tire()
# FoodTruck.pop_tire(taco_truck)
# print(taco_truck.drive())


# class VendingMachine:
#     def __init__(self, product, price, num=0, paid=0):
#         self.product = product
#         self.price = price
#         self.paid = paid
#         self.num = num
#
#     def vend(self):
#         if self.num == 0:
#             return 'Machine is out of stock.'
#         elif self.paid < self.price:
#             return 'You must deposit $%s more.' % (self.price - self.paid)
#         elif self.paid == self.price:
#             self.num -= 1
#             return 'Here is your %s' % self.product
#         else:
#             self.num -= 1
#             temp_paid = self.paid
#             self.paid = 0
#             return 'Here is your %s and $%s change' % (self.product, temp_paid - self.price)
#
#     def deposit(self, paid):
#         if self.num == 0:
#             return 'Machine is out of stock. Here is your $%s.' % paid
#         else:
#             self.paid += paid
#             return 'Current balance: $%s' % self.paid
#
#     def restock(self, num):
#         self.num += num
#         return 'Current %s stock: %s' % (self.product, self.num)
#
# v=VendingMachine('candy', 10)
# print(v.vend())
# print(v.deposit(15))
# print(v.restock(2))
# print(v.vend())
# print(v.deposit(7))
# print(v.vend())
# print(v.deposit(5))
# print(v.vend())
# print(v.deposit(10))
# print(v.vend())
# print(v.deposit(15))
#
# w = VendingMachine ('soda', 2)
# print(w.restock(3))
# print(w.restock(3))
# print(w.deposit(2))
# print(w.vend())
#
# ten, twenty,thirty = 10, 'twenty', [30]
# print('{0} plus {1} is {2}'.format(ten, twenty, thirty))


# class Link:
#     """A linked list.
#
#     >>> s = Link(1)
#     >>> s.first
#     1
#     >>> s.rest is Link.empty
#     True
#     >>> s = Link(2, Link(3, Link(4)))
#     >>> s.second
#     3
#     >>> s.first = 5
#     >>> s.second = 6
#     >>> s.rest.rest = Link.empty
#     >>> s                                    # Displays the contents of repr(s)
#     Link(5, Link(6))
#     >>> s.rest = Link(7, Link(Link(8, Link(9))))
#     >>> s
#     Link(5, Link(7, Link(Link(8, Link(9)))))
#     >>> print(s)                             # Prints str(s)
#     <5 7 <8 9>>
#     """
#     empty = ()
#
#     def __init__(self, first, rest=empty):
#         assert rest is Link.empty or isinstance(rest, Link)
#         self.first = first
#         self.rest = rest
#
#     @property
#     def second(self):
#         return self.rest.first
#
#     @second.setter
#     def second(self, value):
#         self.rest.first = value
#
#     def __repr__(self):
#         if self.rest is not Link.empty:
#             rest_repr = ', ' + repr(self.rest)
#         else:
#             rest_repr = ''
#         return 'Link(' + repr(self.first) + rest_repr + ')'
#
#     def __str__(self):
#         string = '<'
#         while self.rest is not Link.empty:
#             string += str(self.first) + ' '
#             self = self.rest
#         return string + str(self.first) + '>'
#
# link = Link(1)
# print(link)
# link.rest = link
#
# print(link.rest.rest.rest.rest.first)


# print([2, 3, 4][::-1])

# a = [1, 2, 3]
# print(a[len(a):])

from doctest import testmod
from doctest import run_docstring_examples

#
# def sum_naturals(n):
#     """Return the sum of the first n natural numbers.
#
#     >>> sum_naturals(10)
#     55
#     >>> sum_naturals(100)
#     5050
#     """
#     total, k = 0, 1
#     while k <= n:
#         total, k = total + k, k + 1
#     return total
#
# print(testmod())
# run_docstring_examples(sum_naturals, globals(),True)




# def is_sorted(n):
#     """
#     >>> is_sorted(2)
#     True
#     >>> is_sorted(22222)
#     True
#     >>> is_sorted(9876543210)
#     True
#     >>> is_sorted(9087654321)
#     False
#     """
#     if n < 10:
#         return True
#     return is_sorted(n // 10) and (n // 10 % 10 >= n % 10)
#
# print(testmod())

# def mario_number(level):
#     """
#        Return the number of ways that Mario can traverse the
#        level, where Mario can either hop by one digit or two
#        digits each turn. A level is defined as being an integer
#        with digits where a 1 is something Mario can step on and 0
#     is something Mario cannot step on. >>> mario_number(10101)
#     >>> mario_number(10101)
#     1
#     >>> mario_number(11101)
#     2
#     >>> mario_number(100101)
#     0
#     """
#     if level == 1:
#         return 1
#     elif level % 10 == 0:
#         return 0
#     elif level % 10 == 1:
#         return mario_number(level // 10) + mario_number(level // 100)
#
# print(testmod())


# def make_change(n):
#     """
#     Write a function, make_change that takes in an integer amount, n, and returns the minimum number
#     of coins we can use to make change for that n,
#     using 1-cent, 3-cent, and 4-cent coins.
#     Look at the doctests for more examples.
#     >>> make_change(5)
#     2
#     >>> make_change(6) # tricky! Not 4 + 1 + 1 but 3 + 3
#     2
#     """
#     if n <= 4:
#         return 1
#     return min(make_change(n-4), make_change(n-3), make_change(n-1))+1
# print(testmod())

# def elephant(name, age, can_fly):
#     """
#     Takes in a string name, an int age, and a boolean can_fly. Constructs an elephant with these attributes.
#     >>> dumbo = elephant("Dumbo", 10, True)
#     >>> elephant_name(dumbo)
#     'Dumbo'
#     >>> elephant_age(dumbo)
#     10
#     >>> elephant_can_fly(dumbo)
#     True
#     """
#
#     return [name, age, can_fly]
# def elephant_name(e):
#     return e[0]
# def elephant_age(e):
#     return e[1]
# def elephant_can_fly(e):
#     return e[2]
#
# print(testmod())

# a = [1,5, 4, [2, 3], 3]
# print(a[0], a[-1])
# print(len(a))
# print(2 in a)
# print(4 in a)
# print(a[3][0])

# a = [3, 1, 4, 2, 5, 3]
# print(a[1::2])
# print(a[:])
# print(a[4:2])
# print(a[1:-2])
# print(a[::-1])
#
# print([i + 1 for i in [1, 2, 3, 4, 5] if i % 2 == 0])
# print( [i * i - i for i in [5, -1, 3, -1, 3] if i > 2])
# print([[y * 2 for y in [x, x + 1]] for x in [1, 2, 3, 4]])
# def is_leaf(tree):
#     return not branches(tree)
#
#
# def tree(label, branches=[]):
#     return [label] + list(branches)
#
#
# def label(tree):
#     return tree[0]
#
#
# def branches(tree):
#     return tree[1:]
#
#
# def tree_max(t):
#     if is_leaf(t):
#         return label(t)
#     return max(label(t), max([tree_max(branch) for branch in branches(t)]))
#
#
# def height(t):
#     """Return the height of a tree"""
#     if is_leaf(t):
#         return 0
#     return 1+ max(height(branch) for branch in branches(t))
#
#
# def square_tree(t):
#     if is_leaf(t):
#         return label(t) ** 2
#     return tree(label(t) ** 2, [square_tree(branch) for branch in branches(t)])
#
#
# def find_path(tree, x):
#     if label(tree) == x : # 在这个问题里面，最简单的子问题应该是这个！！ 与是不是Leaf没有关系
#         return [label(tree)]
#     for b in branches(tree):  # if i in []: pass!
#         path = find_path(b, x)
#         if path:
#             return [label(tree)] + path
#     #after running function body, it will return None automatically if there is no return  command
#     #！！！！什么都不返回 就会返回None!!
#
#
# def prune(t,k):
#     if k == 0:
#         # return label(t)  #终止条件也要返回的是一棵树才行啊！！
#         return tree(label(t))
#     return tree(label(t), [prune(branch, k-1) for branch in branches(t)])
#
#
# t = tree(1,
#       [tree(3,
#           [tree(4),
#             tree(5),
#            tree(6)]),
#       tree(2)])
#
# t1= (2,[tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])

# print(is_leaf(t1))
# print(tree_max(t))
# print(height(t))
# print(square_tree(t))
# print(find_path(t, 5))


from doctest import testmod
from doctest import run_docstring_examples
#
# def list_of_lists(lst):
#     """
#     >>> list_of_lists([1, 2, 3])
#     [[0], [0, 1], [0, 1, 2]]
#     >>> list_of_lists([1])
#     [[0]]
#     >>> list_of_lists([])
#     []
#     """
#     result = []
#     for i in lst:
#         result.append([x for x in range(i)])
#     return result
#
# run_docstring_examples(list_of_lists, globals(),True)


# def tree(label, branches=[]):
#     return [label] + branches
#
# def label(tree):
#     return tree[0]
#
# def branches(tree):
#     return tree[1:] #returns a list of branches
#
# def sum_of_node(tree):
#     """
#    >>> t =  tree(9,[tree(2),tree(4,[tree(1)]),tree(4, [tree(7), tree(3)])])# Tree from question 2.
#    >>> sum_of_node(t) # 9 + 2 + 4 + 4 + 1 + 7 + 3 = 30
#    30
#     """
#     if not branches(tree):
#         return label(tree)
#     return label(tree) + sum([sum_of_node(branch) for branch in branches(tree)])
#
# # t = tree(4,
# #     [tree(5, []),
# #      tree(2,
# #         [tree(2, []),
# #          tree(1, [])]),
# #      tree(1, []),
# #      tree(8,
# #         [tree(4, [])])])
# #
# # print(t)
# t1 = tree(9,[tree(2),tree(4,[tree(1)]),tree(4, [tree(7), tree(3)])])
# run_docstring_examples(sum_of_node,globals(),True)
#
# def memory(n):
#     """
#     >>> f = memory(10)
#     >>> f = f(lambda x: x * 2)
#     20
#     >>> f = f(lambda x: x - 7)
#     13
#     >>> f = f(lambda x: x > 5)
#     True
#     """
#     def cal(func):
#         nonlocal n
#         n = func(n)
#         print(n)
#         return cal
#     return cal
# print(testmod())
#run_docstring_examples(memory, globals(), True)

#
# def add_this_many(x, el, lst):
#     """ Adds el to the end of lst the number of times x occurs in lst.
#     >>> lst = [1, 2, 4, 2, 1]
#     >>> add_this_many(1, 5, lst)
#     >>> lst
#     [1, 2, 4, 2, 1, 5, 5]
#     >>> add_this_many(2, 2, lst)
#     >>> lst
#     [1, 2, 4, 2, 1, 5, 5, 2, 2]
#     """
#     count =0
#     for i in lst:
#         if x == i:
#             count += 1
#     for i in range(count):
#         lst.append(el)
#
# print(testmod())

# def reverse(lst):
#     """ Reverses lst in place.
#     >>> x = [3, 2, 4, 5, 1]
#     >>> reverse(x)
#     >>> x
#     [1, 5, 4, 2, 3]
#     """
#     for i in range(len(lst) // 2):
#         lst[i], lst[-1-i]  = lst[-1-i], lst[i]
# print(testmod())

# def group_by(s, fn):
#     """
#     >>> group_by([12, 23, 14, 45], lambda p: p // 10)
#     {1: [12, 14], 2: [23], 4: [45]}
#     >>> group_by(range(-3, 4), lambda x: x * x)
#     {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
#     """
#     groups = {}
#     for i in s:
#         key = fn(i)
#         if key in groups:
#             groups[key].append(i)
#         else:
#             groups[key] = [i]
#     return groups
#
# print(testmod())
# def replace_all_deep(d, x, y):
#     """
#     >>> d = {1: {2: 'x', 'x': 4}, 2: {4: 4, 5: 'x'}}
#     >>> replace_all_deep(d, 'x', 'y')
#     >>> d
#     {1: {2: 'y', 'x': 4}, 2: {4: 4, 5: 'y'}}
#     """
#     for key in d:
#         if type(d[key]) != dict:
#             if d[key] == 'x':
#                 d[key] = 'y'
#         else:
#             replace_all_deep(d[key],x, y)
#
# print(testmod())


# Constructor
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def Tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + branches

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# For convenience
def is_leaf(tree):
    return not branches(tree)

# def sum_range(t):
#     """
#     Returns the range of the sums of t, that is, the\
#     difference between the largest and the smallest
#     sums of t.
#     """
#     def helper(t):
#         # return largest sum and smallest sum
#         if is_leaf(t):
#             return [label(t), label(t)]
#         else:
#             a = min([helper(branch)[1] for branch in branches(t)])
#             b = max([helper(branch)[0] for branch in branches(t)])
#             x = label(t)
#             return [b+x, a+x]
#     x, y = helper(t)
#     return x - y
#
#
# t = tree(5, [tree(1,[tree(7, [tree(4, [tree(3)])]),tree(2)]),tree(2, [tree(0), tree(9)])])
# print(sum_range(t))


# def no_eleven(n):
#     """
#     Return a list of lists of 1's and 6's that do not contain 1 after 1.
#     >>> no_eleven(2)
#     [[6, 6], [6, 1], [1, 6]]
#     >>> no_eleven(3)
#     [[6, 6, 6], [6, 6, 1], [6, 1, 6], [1, 6, 6], [1, 6, 1]]
#     >>> no_eleven(4)[:4] # first half
#     [[6, 6, 6, 6], [6, 6, 6, 1], [6, 6, 1, 6], [6, 1, 6, 6]]
#     >>> no_eleven(4)[4:] # second half
#     [[6, 1, 6, 1], [1, 6, 6, 6], [1, 6, 6, 1], [1, 6, 1, 6]]
#     """
#     result = []
#     if n == 0:
#         return []
#     elif n == 1:
#         return [[6], [1]]
#     else:
#         for i in no_eleven(n-1):
#             if i[-1] == 6:
#
#                 result.append(i+[1])
#                 result.append(i+[6])
#
#             else:
#                 result.append(i+[6])
#     return result
# print(testmod())

# def eval_with_add(t):
#     """
#     Evaluate an expression tree of * and + using only
#     addition.
#     >>> plus = Tree('+', [Tree(2), Tree(3)])
#     >>> eval_with_add(plus)
#     5
#     >>> times = Tree('*', [Tree(2), Tree(3)])
#     >>> eval_with_add(times)
#     6
#     >>> deep = Tree('*', [Tree(2), plus, times])
#     >>> eval_with_add(deep)
#     60
#     >>> eval_with_add(Tree('*'))
#     1
#     """
#
#     if label(t) == '+':
#         return sum([eval_with_add(branch) for branch in branches(t)])
#     elif label(t) == '*':
#         total =1
#
#         for b in branches(t):
#             total, term = 0, total
#             for _ in range(eval_with_add(b)):
#                 total = total + term
#
#         return total
#
#     else:
#         return label(t)
# print(testmod())


