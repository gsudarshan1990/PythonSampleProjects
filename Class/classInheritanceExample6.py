class model():
    def __init__(self):
        print('A model is created')


class agile(model):
    def __init__(self):
        model.__init__(self)
        print('Agile model is used')


class waterfall(model):
    def __init__(self):
        model.__init__(self)
        print('waterfall model is used')

myagile=agile()
print('-'*100)
mywaterfallmodel=waterfall()
