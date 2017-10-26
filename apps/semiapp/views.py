from __future__ import unicode_literals
from django.contrib.messages import error						# IF YOU USE ERROR MESSAGE, USE THIS LINE!
from django.shortcuts import render, HttpResponse, redirect
from .models import User 										#IF YOU USE MODEL, ADD THIS LINE!!!!

def index(request):												# 
    context = {													# 
        "userList": User.objects.all() 							# RETRIEVE ALL FROM DB. userList is a variable name
        }														# 
    return render(request, "index.html", context)				# RETURN TO INDEX.HTML
																# 
def new(request):												# 
    return render(request, "new.html")							# RETURN TO NEW.HTML
																# 
def create(request):											# 
    errors = User.objects.basic_validator(request.POST) 		# USE MODELS.PY TO CHECK BASIC VALIDATOR
    if len(errors):												# CHECK THE REQUIREMENT FROM MODELS.PY
        for field, message in errors.iteritems():				# CHECK ERROR IN EVERY FIELD OF CLASS 
            error(request, message, extra_tags=field)			# SHOW ERROR MESSAGE
        return redirect('/new')									# IF ERROR, RETURN TO NEW.HTML
    User.objects.create(										# 
        first_name=request.POST['first_name'],					# 
        last_name=request.POST['last_name'],					# 
        email=request.POST['email'],							# 
        # created_at=strftime("%H:%M:%S, %B %d, %Y", gmtime()	# ??
    )															# 
    return redirect("/")										# return to where?
																# 
def show(request, user_id):											# RETRIEVE INFO USING ID
    userObj = User.objects.get(id = user_id)							# userObj is a variable for User.objects.get
    return render(request, "show.html", {"user":userObj})		# BRING DATA TO SHOW.HTML WITH USER'S INFORMATION.
																# 
def edit(request, user_id):											# FROM SHOW.HTML AND SEE IF USER SATISIFIES WITH HIS/HER INFO.
    userObj = User.objects.get(id = user_id)							# IF NOT, EDIT IT AND
    print "edit"												# 
    return render(request, "edit.html", {"user":userObj})		# BRING DATA TO EDIT.HTML WITH USER'S REVISED INFORMATION
																# 
def update(request, user_id):										# 
    errors = User.objects.basic_validator(request.POST)			# CONTINUE FROM EDIT.HTML AND USE MODELS.PY TO CHECK BASIC VALIDATOR
    if len(errors):												# 
        for field, message in errors.iteritems():				# 
            error(request, message, extra_tags=field)    		# 
        return redirect('/{}/edit'.format(id))					# HOW DO YOU GET THIS (RETURN TO WHERE?)
																# 
    u = User.objects.get(id=user_id)									# SAME AS CREATE
    # instead of a multi-line update, try this:					# 
    # User.objects.filter(id=id).update(your params)			# 
    u.first_name = request.POST['first_name']					# 
    u.last_name = request.POST['last_name']						# 
    u.email = request.POST['email']								# 
    u.save()													# 
    return redirect('/')										# 
																# 
def destroy(request, user_id):										# FROM SHOW.HTML
    dest = User.objects.get(id = user_id)							# dest is a variable for USER.OBJECTS.GET AND DELETE
    dest.delete()												# 
    return redirect('/')										# 