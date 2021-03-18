from .serializer import SupervisorSerializer, Supervisor
from api.controller.Transfer import AppendTGToPsycologist, GetPsyTransfers, GetTransfers
from api.models import TransferGroup
from api.serializer import TransferGroupSerializer

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

def getTransferGroupById(tgid):
    try:
        group = TransferGroup.objects.get(tgid=tgid)

        data = TransferGroupSerializer(group)
        return data.data
    except:
        raise "Not found"

def updateTransferGroupTransfer(tgid, data):
    try:
        group = TransferGroup.objects.get(tgid=tgid)

        for update in data:
            transfer = group.group.get(_id=update['tid'])

    except:
        pass