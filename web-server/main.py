import store
from fastapi import FastAPI

app1 = FastAPI()

@app1.get('/')
def get_list():
    return[1,2,3]

@app1.get('/contact')
def get_list():
    return{'name' : 'Platzi'}



def run():
    store.getCategories()

if __name__ == '__main__':
    run()

