from .serializer import SupervisorSerializer, Supervisor

def comparePasswords(p1, p2):
    return p1 == p2

def createSupervisor(data):
    supervisor = SupervisorSerializer(data=data)

    if supervisor.is_valid():
        supervisor.save()
        return supervisor.data
    print(supervisor.errors)
    raise "Data not valid"

def loginSupervisor(email, password):
    try:
        supervisor = Supervisor.objects.get(email=email)
        if (comparePasswords(supervisor.password, password)):
            supervisor_data = SupervisorSerializer(supervisor)
            return supervisor_data.data
        raise "Password not valid"
    except:
        raise "Error"



def getAll():
    sups = Supervisor.objects.all()
    sups = SupervisorSerializer(sups, many=True)

    return sups.data
