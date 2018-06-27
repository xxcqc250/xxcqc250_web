from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.http import HttpResponseRedirect

def agri_home(request):
	return render_to_response('index.html',locals())