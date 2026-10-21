def arithmoi():
    print("Δώσε 3 αριθμούς: ")
    x = int(input())
    y = int(input())
    z = int(input())
    if x*y >= x*z:
        print("H τιμή",x*y,"είναι μεγαλύτερη ή ίση απο την τιμή",x*z,)
    else:
        print("Η τιμή",x*y,"είναι μικρότερη απο την τιμή",x*z)
arithmoi()