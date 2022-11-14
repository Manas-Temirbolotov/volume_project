from employee.models import *
import datetime

manas = Employee.objects.create(name="Manas", birth_date="1984-11-21", position="manager", salary=5000)
ruslan = Employee.objects.create(name="Ruslan", birth_date="1985-01-30", position="сhief", salary=900)
aida = Employee.objects.create(name="Aida", birth_date="1983-05-06", position="specialist", salary=3000)
mirba = Employee.objects.create(name="Mirbek", birth_date="1988-03-16", position="manager", salary=2500)

Employee.objects.all()

manas_passport = Passport.objects.create(name="Manas Temirbolotov", inn='221111984', birth_date="1984-11-21",
                                         id_card=8965, person_data=Manas)
ruslan_passport = Passport.objects.create(name="Atai Narynov", inn='2222123', birth_date="1985-01-30", id_card=6985,
                                          person_data=Ruslan)
aida_passport = Passport.objects.create(name="Anam Tilenov", inn='1312124', birth_date="1983-05-06", id_card=1234,
                                        person_data=Aida)
mirba_passport = Passport.objects.create(name="Askar Dujsekeev", inn='16454124', birth_date="1988-03-16", id_card=2222,
                                         person_data=Mirbek)

Passport.objects.all()

manas_passport.get_gender()
ruslan_passport.get_gender()
aida_passport.get_gender()

mirba.delete()

w_project = WorkProject(project_name="Chang An project")
w_project.save()

manas_project_member = Membership(employee=manas, work_project=w_project, date_joined="2016-03-01")
manas_project_member.save()

ruslan_project_member = Membership.objects.create(employee=ruslan, work_project=w_project, date_joined="2016-03-01")
aida_project_member = Membership.objects.create(employee=aida, work_project=w_project, date_joined="2016-03-01")

rav = Employee.objects.create(name="Ravshan", birth_date="1979-06-06", position="aho", salary=600)
rav_project_member = Membership.objects.create(employee=rav, work_project=w_project, date_joined="2016-03-01")

cl1 = Client.objects.create(address='mkr1', phone_number='0555123456', name='client #1', birth_date='1987-01-01')
cl2 = Client.objects.create(address='mkr2', phone_number='0777123456', name='client #2', birth_date='1985-01-01')
cl3 = Client.objects.create(address='mkr3', phone_number='0705555555', name='client #3', birth_date='1980-03-03')

vip_client = VIPClient.objects.create(vip_status_start='2021-10-10', donation_amount=100, address='mkr4',
                                      phone_number='0555999999',
                                      name='Nurs VIP client', birth_date='1994-01-03')

Employee.objects.all()
Passport.objects.all()
WorkProject.objects.all()
WorkProject.objects.filter(projects__name__startswith='Manas')
Client.objects.all()
VIPClient.objects.all()
