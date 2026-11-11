def greet(name):
    return f"Hello, {name}!"
result = greet("Michael")
print(result)

#res1 = greet()
#print(res1)

def create_user(name,role = "user"):
    return {
        "name": name,
        "role": role
    }
print(create_user("Michael"))
print(create_user("Michael", "admin"))

print()

def calculate_discount(price,discount = 10):
    return price-(price*discount/100)
print(calculate_discount(100))
print(calculate_discount(100,25))

#def foo(a=1,b):
    #return a+b
#print(foo(5))

def add_test_res(name,results=[]):
    results.append(name)
    return results
print(add_test_res("test_login"))
print(add_test_res("test_logout"))

def add_test_res(name,results=None):
    if results is None:
        results = []
    results.append(name)
    return results
print(add_test_res("test_login"))
print(add_test_res("test_logout"))
##
##
##
##
##
#микс позиционное вызов и именнованный вызов
print(create_user1("Kristina",role="admin",email="kris@gm.com"))

