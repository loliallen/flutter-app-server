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

def updateSupervisor(id, updates):
    try:
        sup = Supervisor.objects.filter(pk=id).update(**updates)
        sup = sup.first()

        data = SupervisorSerializer(sup)
        return data.data
    except:
        raise "Nor found | Error"

def getAll():
    sups = Supervisor.objects.all()
    sups = SupervisorSerializer(sups, many=True)

    return sups.data


def getById(id):
    try:
        sup = Supervisor.objects.get(pk=id)
        sup = SupervisorSerializer(sups)

        return sup.data
    except:
        raise "Not found"

def getTransferGroupById(tgid):
    try:
        group = TransferGroup.objects.get(tgid=tgid)

        data = TransferGroupSerializer(group)
        return data.data
    except:
        raise "Not found"

def updateTransferGroupTransfer(tgid, data):
    """
        data:
        {
            group: {
                tid: "",
                comment
            },
            status
        }
    """
    try:
        group = TransferGroup.objects.get(tgid=tgid)

        for update in data['group']:
            try:
                transfer = group.group.get(_id=update['tid'])
                if "comment" in update:
                    transfer.moderation_feedback = update['comment'] 
            except:
                pass
        group.moderation_status = data['status']   
    except:
        pass


def deleteSupervisor(id):
    try:
        sup = Supervisor.objects.filter(pk=id).delete()
        
        data = SupervisorSerializer(sup)
        return data.data
    except:
        raise "Not Found"