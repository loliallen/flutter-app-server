from api.models import Diary, Transfer, TransferGroup, Configuration
from psycologist.models import User as Psycologist
from api.serializer import TransferSerializer, TransferGroupSerializer
from account.models import User

from api.exceptions import NotEnoughtDiaries, NotValidForSerialize

from bson.objectid import ObjectId

# User


def GetUserTransfers(user_id):
    user = User.objects.get(_id=ObjectId(user_id))
    transfers = user.transfer_groups.all()

    data = TransferGroupSerializer(transfers, many=True)

    return data.data

# Psy
def GetTransfers(filter=None):
    # TODO select fields
    tgs = []
    if filter != None:
        tgs = TransferGroup.objects.filter(**filter).all()
    else:
        tgs = TransferGroup.objects.all()

    data = TransferGroupSerializer(tgs, many=True)

    return data.data


def GetPsyTransfers(psy_id):
    psy = Psycologist.objects.get(_id=ObjectId(psy_id))
    transfers = psy.shared_transfers.all()

    data = TransferSerializer(transfers, many=True)

    return data.data

# Psy


def GetTranferGroup(tid):
    try:
        tranfer = TransferGroup.objects.get(_id=ObjectId(tid), moderation_status='c'    )
        data = TransferGroupSerializer(tranfer)
        return data.data
    except TransferGroup.DoesNotExist:
        return None

# User

EXTRA_WAIT = 7

def CreateTransfer(diary_ids: list, user_id, pid = None):
    """
        recive:
            diary_id
            user_id
            psy_id
    """
    try:
        config = Configuration.objects.all().last()

        user = User.objects.get(_id=ObjectId(user_id))
        
        count_of_diaries = len(user.diaries.all())
        
        mcodft = config.min_count_of_diaries_for_transfer + 1 

        print(count_of_diaries, diary_ids)
        
        #  TODO
        if hasattr(user.psycologist, "_id"):
            stf_len = len(user.psycologist.shared_transfers.all())
            if (count_of_diaries < (2 / mcodft + EXTRA_WAIT)):
                raise NotEnoughtDiaries
        elif count_of_diaries < config.min_count_of_diaries_for_transfer:
            raise NotEnoughtDiaries

        transfer_group = TransferGroup()
        for diary_id in diary_ids:
            diary = Diary.objects.get(_id=ObjectId(diary_id))

            transfer = Transfer()
            transfer.diary = diary
            transfer.save()
            transfer_group.group.add(transfer)            
        
        
        if pid:
            #  Added send transfer on moderation if psy is not verified
            psy = Psycologist.objects.get(_id=ObjectId(pid))
            if(psy.verified):
                psy.shared_transfers.add(transfer_group)
            else:
                transfer_group.moderation_status = 'r'
                psy.possible_transfers.add(transfer_group)
            psy.save()

        transfer_group.save()
    
        
        user.transfer_groups.add(transfer_group)    

        user.save()
        data = TransferGroupSerializer(transfer_group)

        return data.data
    except Diary.DoesNotExist:
        raise NotValidForSerialize
    except Psycologist.DoesNotExist:
        raise NotValidForSerialize
    except TransferGroup.DoesNotExist as e:
        raise NotValidForSerialize
    
# Psy
def UpdateTransferGroup(tgid, updates, psy: Psycologist):
    try:

        transfer_group = TransferGroup.objects.get(_id=ObjectId(tgid))
        
        if not psy.verified:
            transfer_group.moderation_status = 'r'

        for update in updates['group']:
            t_id = update['tid']
            feedback = update['fb']
            
            transfer = Transfer.objects.get(_id=ObjectId(t_id))

            transfer.feedback = feedback
            transfer.answered = True
            transfer.save()

        transfer_group.feedback = updates['feedback']
        transfer.status = updates['status']
        transfer_group.save()

        # if transfer is done, remove it and append to `done` 
        if (transfer.status == "a"):
            psy.shared_transfers.remove(transfer_group)
            psy.done_transfers.add(transfer_group)
            psy.save()

        data = TransferGroupSerializer(transfer_group)
        return data.data
    except TransferGroup.DoesNotExist:
        return None       
    except Transfer.DoesNotExist:
        return None


def UpdateTransferGroupStatus(tgid, updates, psy):
    try:
        transfer_group = TransferGroup.objects.get(_id=ObjectId(tgid))
        
        transfer_group.moderation_status = updates['moderation_status']
        transfer_group.save()

        data = TransferGroupSerializer(transfer_group)
        return data.data
    except TransferGroup.DoesNotExist:
        return None       
    except Transfer.DoesNotExist:
        return None

def AppendTGToPsycologist(tgid, psy_id):
    try:
        psy = Psycologist.objects.get(_id=ObjectId(psy_id))
        tg = TransferGroup.objects.get(_id=ObjectId(tgid))

        # Adds all user groups if user in patients

        psy.shared_transfers.add(tg)

        psy.save()

        return True
    except Psycologist.DoesNotExist:
        return False
    except TransferGroup.DoesNotExist:
        return False
    

def CheckAbleToTransfer(userId):
    config = Configuration.objects.all().last()
    user = User.objects.get(_id=ObjectId(user_id))

    psycologist = user.psycologist

    tg_l = len(user.transfer_groups)

    if psycologist != None:
        # psycologist.
        pass
