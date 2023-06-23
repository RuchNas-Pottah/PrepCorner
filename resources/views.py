from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Resources,Resource


@login_required
def resources(request):
    resources = Resources.objects.all()

    return render(request, 'resources/resources.html', {'resources': resources})

@login_required
def topic(request, slug):
    topic = Resources.objects.get(slug=slug)
    content = Resource.objects.filter(topic=topic)

    return render(request, 'resources/topic.html', {'topic': topic, 'contents': content})

