from .models import Action
from django.contrib.contenttypes.models import ContentType
import datetime
from django.utils import timezone

def create_action(user, verb, target=None):
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similer_actions = Action.objects.filter(user_id = user.id, verb=verb, created__gte=last_minute)
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similer_actions = similer_actions.filter(target_ct=target_ct, target_id=target.id)
    if similer_actions:
        return False
    action = Action(user=user, verb=verb, target=target)
    action.save()
    return True
