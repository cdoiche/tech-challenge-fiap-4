import random
import time
from faker import Faker
from locust import HttpUser, task

class ConsultarContatoUser(HttpUser):
    @task
    def consultar_todos_os_contatos(self):
        self.client.get("/ConsultarContato")
    
    @task(3)
    def consultar_contatos_por_ddd(self):
        for ddd in range(10, 100):
            print(f"/ConsultarContato?ddd={ddd}")
            self.client.get(f"/ConsultarContato?ddd={ddd}", name="/ConsultarContato")
            time.sleep(0.5)
    
    # @task
    # def criar_contato(self):
    #     faker = Faker()
    #     phone = "".join(random.choices('0123456789', k=9))
    #     ddd = "".join(random.choices('123456789', k=2))
    #     name = faker.name()
    #     email = faker.email()

    #     self.client.post("/CriarContato", json={"nome": name, "ddd": ddd, "telefone": phone, "email": email})


