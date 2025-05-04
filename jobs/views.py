from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import ApplicantForm
from django.http import JsonResponse

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.job = job
            applicant.save()

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'name': applicant.name,
                    'email': applicant.email,
                    'resume_url': applicant.resume.url,
                })
            else:
                return redirect('application_success')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': 'Invalid form data'}, status=400)

    else:
        form = ApplicantForm()

    return render(request, 'jobs/job_detail.html', {'job': job, 'form': form})
