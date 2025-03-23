# Local
# Enclosure
# Global
# Built-in [len(), str(), print()]

#scope
#namespace

# global
# non local

y = "Глобальна змінна"

def outer():

    # y = "Охоплююча змінна"

    def inner():
        global y
        y = "Локальна змінна"


        print("Результат Маленької функції:", y)


    inner()
    print("Виклик Охоплюючої:", y)



outer()

print("Зовнішній виклик:", y)


