from django.shortcuts import render, get_object_or_404, redirect
from resume.models import Resume
from resume.forms import ResumeForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def resume_list(request):
    search_query = request.GET.get('search', '')

    if request.user.is_authenticated:
        if request.user.company:
            resumes = Resume.objects.filter(Q(position__icontains=search_query) | Q(skills__icontains=search_query))
        else:
            resumes = Resume.objects.filter(Q(position__icontains=search_query) | Q(skills__icontains=search_query),
                                            author=request.user)
    else:
        resumes = Resume.objects.none()

    context = {
        'resumes': resumes,
        'search_query': search_query,
        'user': request.user
    }

    return render(request, 'resume_list.html', context)


def resume_detail(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    return render(request, 'resume_detail.html', {'resume': resume})


def create_resume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.author = request.user
            resume.save()
            form.save_m2m()
            return redirect('resume_list')
        else:
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, "create_resume.html", {"form": form})


def edit(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)

    if request.method == "POST":
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = ResumeForm(instance=resume)

    return render(request, "edit_resume.html", {"form": form, "resume": resume})


@login_required
def resume_delete(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, author=request.user)

    if request.method == 'POST':
        resume.delete()
        return redirect('resume_list')
    return render(request, 'resume_delete.html', {'resume': resume})
