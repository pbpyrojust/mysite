from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reversedfrom django.views import generic

from polls.models import Choice, Poll

class IndexView(generic.ListView):
	template


def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the poll voting form.
		return render(request, 'polls/detail.html', {
			'poll': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return a HttpResponseRedirect after succesfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
