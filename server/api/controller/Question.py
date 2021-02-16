from api.models import Question
from api.serializer import QuestionSerializer

from account.models import User, EmbQuestion
from bson.objectid import ObjectId

from random import randrange

def GetQuestions():
    questions = Question.objects.all()

    data = QuestionSerializer(questions, may=True)

    return data.data

def GetQuestionsByMood(mood: str, user_id):
    questions = Question.objects.all().filter(mood=mood)
    questions_len = len(Question.objects.all())
    user = User.objects.get(_id=ObjectId(user_id))
    used_questions = user.questions

    # serialize
    data = QuestionSerializer(questions, many=True)
    print(questions_len, len(used_questions))
    if used_questions == None:
        l = 0;
        user.questions = [
            { 'question': questions.first()._id, 'entries': 1 }
        ]
        user.save()
        print(data.data.get(_id=str(questions.first()._id)))
        return data.data.get(_id=str(questions.first()._id))
    elif len(used_questions) < questions_len:
        for q in data.data:
            if not q.get('_id') in list(map(lambda x: str(x['question']), used_questions)):
                user.questions.append({'question': ObjectId(q.get('_id')), 'entries':1})
                user.save()
                return q
    else:
        random_index = randrange(0, len(questions), 1)
        random_question = data.data[random_index]
        selected_question_id = data.data[random_index].get('_id')
        print(selected_question_id)
        for i, val in enumerate(used_questions):
                if str(val['question']) == selected_question_id:
                   user.questions[i]['entries']+=1
                   user.save()
        return random_question