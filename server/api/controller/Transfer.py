from api.models import Diary, Transfer, TransferGroup
from psycologist.models import User as Psycologist
from api.serializer import TransferSerializer, TransferGroupSerializer
from account.models import User

from bson.objectid import ObjectId

# User


def GetUserTransfers(user_id):
    user = User.objects.get(_id=ObjectId(user_id))
    transfers = user.transfers.all()

    data = TransferSerializer(transfers, many=True)

    return data.data

# Psy


def GetPsyTransfers(psy_id):
    psy = Psycologist.objects.get(_id=ObjectId(psy_id))
    transfers = psy.shared_transfers.all()

    data = TransferSerializer(transfers, many=True)

    return data.data

# Psy


def GetTranferGroup(tid):
    try:
        tranfer = TransferGroup.objects.get(_id=IbjectId(tid))

        data = TransferGroupSerializer(tranfer)
        return data.data
    except TransferGroup.DoesNotExist:
        return None

# User


def CreateTransfer(diary_ids: list, user_id, pid = None):
    """
        recive:
            diary_id
            user_id
            psy_id
    """
    try:
        user = User.objects.get(_id=ObjectId(user_id))
        transfer_group = TransferGroup()
        for diary_id in diary_ids:
            diary = Diary.objects.get(_id=ObjectId(diary_id))

            transfer = Transfer()
            transfer.diary = diary
            transfer.save()
            transfer_group.group.add(transfer)            
        
        transfer_group.save()
        
        if pid:
            psy = Psycologist.objects.get(_id=ObjectId(pid))
            psy.shared_transfers.add(transfer_group)
    
        
        user.transfer_groups.add(transfer_group)    

        psy.save()
        user.save()

        return True
    except Diary.DoesNotExist:
        return False
    except Psycologist.DoesNotExist:
        return False
    except TransferGroup.DoesNotExist as e:
        print(e.args)
        return False
    
# Psy
def UpdateTransferGroup(tgid, updates):
    try:
        transfer_group = TransferGroup.objects.get(_id=ObjectId(tgid))
        
        for update in updates['group']:
            t_id = update['tid']
            feedback = update['fb']
            
            transfer = Transfer.objects.get(_id=ObjectId(t_id))

            transfer.feedback = feedback
            transfer.answered = True
            transfer.save()

        transfer_group.feedback = updates['feedback']
        transfer_group.save()

        data = TransferGroupSerializer(transfer_group)
        return data.data
    except TransferGroup.DoesNotExist:
        return None       
    except Transfer.DoesNotExist:
        return None