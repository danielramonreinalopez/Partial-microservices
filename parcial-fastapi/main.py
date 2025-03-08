from fastapi import FastAPI

app = FastAPI()

def five_attributes():
      person = {
          "name":"daniel",
          "age":21,
          "city":"armenia",
          "contry":"colombia",
          "job":"carpintero"
    }
      return person
      
@app.get("/person")
async def ob_person():
    return five_attributes()
