import datetime
from django.db import models


class AbstractPerson(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get_age(self):
        date_now = datetime.now().year
        birth_year = self.birth_date
        return date_now -birth_year


class Employee(AbstractPerson):
    position = models.CharField(max_length=50)
    salary = models.IntegerField()
    work_experience = models.DateField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Специалист {self.name} в должности {self.position} сохранен')

    # def __str__(self):
    #     return self.position


class Passport(models.Model):
    inn = models.IntegerField()
    id_card = models.CharField(max_length=20)
    person_data = models.OneToOneField(Employee, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Специалист {self.name} с {self.inn} успешно сохранен!')

    def get_gender(self):
        inn_gen = str(self.inn)
        if inn_gen.startswith('1'):
            gen = 'female'
        else:
            gen = 'male'
        return gen

    def __str__(self):
        return f'Специалист: {self.name} Паспорт: {self.id_card}, ИНН: {self.inn}'

class WorkProject(models.Model):
    project_name = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Проект {self.project_name} создан')

    def __str__(self):
        return self.project_name


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def __str__(self):
        return f'{self.employee} - {self.work_project}'


class Client(AbstractPerson):
    address = models.CharField(max_length=50)
    phone_number = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Адрес и контакты {self.name} сохранены')


class VIPClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()
    vip_client = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'VIP клиент {self.name} сохранен')
