from django.http import *
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from Location.forms import *
#from Employee.forms import *



def gps(request):
    data = dict()
    if request.method == "POST":
        CarID = request.POST.get("CarID")
        Latitude = request.POST.get("Latitude")
        Longitude = request.POST.get("Longitude")
        GPS.object.create(
            Longitude = Longitude,
            Latitude = Latitude,
            CarID = CarID,
            )

    return JsonResponse(data)
def gpspost(request):
	if request.method == 'GET':
		form = gps_form(request.GET)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/showgps/')
	else:
		form = gps_form()
	return render(request,'postgps.html',{'form':form})

def showgps(request):
	context=Gps.objects.all()

	return render(request,'showgps.html',{"context":context})