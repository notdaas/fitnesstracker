from django.shortcuts import render, redirect
from .models import Activity, Goal
from .forms import ActivityForm, GoalForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    activities = Activity.objects.filter(user=request.user)
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'fitness/dashboard.html', {'activities': activities, 'goals': goals})

@login_required
def log_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            return redirect('dashboard')
    else:
        form = ActivityForm()
    return render(request, 'fitness/log_activity.html', {'form': form})

@login_required
def set_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('dashboard')
    else:
        form = GoalForm()
    return render(request, 'fitness/set_goal.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'fitness/profile.html')