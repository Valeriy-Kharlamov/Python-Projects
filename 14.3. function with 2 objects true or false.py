def function(object_1, object_2):
    if object_1 is object_2:
        return True
    else:
        return False

# № 1

obj = function(9, 9)  # True, так как они ссылаются на одну и ту же область памяти
print(obj)            # И имеют одинаковые значения  
obj = function(9, 18) # False разные значения, хоть и одна область памяти
print(obj)

    # № 2

obj = function('cat', 'cat') # True
print(obj)
obj = function('cat', 'dog') # False
print(obj)

        # № 3

a = [1,2,3]   # В этом примере функция сравнивает объекты "a" и "b",
b = a         # и так как они ссылаются на одну и ту же область памяти, результат будет "True".
c = [1,2,3]   # Однако, когда сравниваются "a" и "c", которые содержат одинаковые значения,
              # но находятся в разных областях памяти, результат будет `False`.

print(function(a, b)) # True
print(function(a, c)) # False
