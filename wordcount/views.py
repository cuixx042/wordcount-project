from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request, 'home.html')
	#return HttpResponse('Hello') simple test case

def about(request):
	return render(request, 'about.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()

	word_dict = {}
	for word in wordlist:
		word_dict[word] = word_dict.get(word, 0) + 1

	sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sorted_words})
