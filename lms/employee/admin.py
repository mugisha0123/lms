from django.contrib import admin
from employee.models import Role,Department,Employee,Leave_policy



admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Leave_policy)