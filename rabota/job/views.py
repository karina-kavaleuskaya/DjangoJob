from django.shortcuts import render, get_object_or_404, redirect
from job.models import Job
from job.forms import JobForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q



def job_list(request):
    search_query = request.GET.get('search', '')

    if request.user.is_authenticated and request.user.company:
        jobs = Job.objects.filter(Q(job_requirement__icontains=search_query) | Q(position__icontains=search_query) |
                                  Q(salary__icontains=search_query), author=request.user)
    else:
        jobs = Job.objects.filter(Q(job_requirement__icontains=search_query) | Q(position__icontains=search_query) |
                                  Q(salary__icontains=search_query))

    context = {
        'jobs': jobs,
        'search_query': search_query
    }

    return render(request, 'job_list.html', context)



def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'job_detail.html', {'job': job})


def create_job(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.author = request.user
            job.save()
            form.save_m2m()
            return redirect('job_list')
        else:
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, "create_job.html", {"form":form})


def edit(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm(instance=job)

    return render(request, "edit_job.html", {"form": form, "job": job})


@login_required
def job_delete(request, job_id):
    job = get_object_or_404(Job, id=job_id, author=request.user)

    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'job_delete.html', {'job': job})


@login_required
def send_resume(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        message = "You send your resume to company"
        return render(request, 'send_resume.html', {'message': message})

    return render(request, 'send_resume.html', {'job': job})

