
class Product:

    def __init__(self ,pid=0 ,pnm='' ,pprice=0.0 ,pqyt=0):
        self.productid =int(pid)
        self.productname =pnm
        self.productprice =float(pprice)
        self.productqyt =int(pqyt)

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)

