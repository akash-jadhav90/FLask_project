from flask import  Flask,request,render_template
from productinfo import Product
app=Flask(__name__)

productlist=[]
@app.route('/wel')
def WELCOME():
    return render_template('index.html')

@app.route('/SAVE/PRO',methods=['post','get'])
def Save_Product():
    message=''
    if request.method=='POST':
        formdata=request.form
        print('post data',formdata)
        pid=int(formdata.get('proid'))
        isDuplicate=False
        for i in productlist:
            if i.productid==pid:
                i.productname=formdata.get('pronm')
                i.productqyt =int(formdata.get('proqyt'))
                i.productprice =float(formdata.get('proprice'))
                isDuplicate=True
                break

        if isDuplicate:
            message='PRoduct are duplaicate then update the product...'
        else:


            produ=Product(pid=formdata.get('proid'),pnm=formdata.get('pronm'),pprice=formdata.get('proprice'),pqyt=formdata.get('proqyt'))
            productlist.append(produ)
            message='PRoduct is successfully added...'

    #elif request.method=='GET':
    #    formdata=request.args
    #print(formdata)
    #print(type(formdata))
    return render_template('Add_Product.html',result=message,product1=Product())

@app.route('/Show/pro',methods=['post','get'])
def Show_products():
    return render_template('ShowProduct.html',pro=productlist)

@app.route('/serach/pro',methods=['post','get'])
def Serach_product():
    if request.method=='POST':
        formdata=request.form
        pid=int(formdata.get('proid'))

        for i in productlist:
            if i.productid==pid:
                return render_template('searchproducts.html',products2=i)
    return render_template('searchproducts.html',products2=None)


@app.route('/Edit/PRo/<int:pid>' ,methods=['GET'])
def Edit_Product(pid):
    PRoduct=None
    for pro in productlist:
        if pro.productid == pid:
            PRoduct=pro
    return  render_template('Add_Product.html',product1=PRoduct)


@app.route('/Delete/PRo/<int:pid>')
def Delete_product(pid):
    mesg=''
    for pro in productlist:
        if pro.productid==pid:
            productlist.remove(pro)
            msg='PRoduct is successfully delete...'
            break
    return render_template('ShowProduct.html',mesg1=mesg,pro=productlist)

if __name__ == '__main__':
    app.run(debug=True)