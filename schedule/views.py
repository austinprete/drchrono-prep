from string import split
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from schedule.models import Vaccine, Schedule, PatientFamily, Patient


@login_required
def index(request):
    user = request.user
    families = user.patientfamily_set.all()
    return render(request, 'schedule/index.html', {'request': request, 'families': families,})


@login_required
def chart(request, family_id, member_id):
    user = request.user
    family = user.patientfamily_set.filter(pk=family_id)[0]
    member = family.patient_set.filter(pk=member_id)[0]
    schedule = member.schedule_set.all()
    doses = None
    if schedule:
        schedule = schedule[0]
        vaccines = schedule.vaccine_set.all()
        doses = []
        for vaccine in vaccines:
            doses.append(vaccine.dose_set.all())
    return render(request, 'schedule/chart.html', {'request': request, 'family': family, 'member': member, 'doses': doses})


@login_required
def update_schedule(request, family_id, member_id):
    user = request.user
    family = user.patientfamily_set.filter(pk=family_id)[0]
    member = family.patient_set.filter(pk=member_id)[0]
    schedule = member.schedule_set.all()[0]
    vaccines = schedule.vaccine_set.all()
    doses = []
    for vaccine in vaccines:
        doses.append(vaccine.dose_set.all())
    values = []
    for value in request.POST:
        for dose_list in doses:
            for dose in dose_list:
                if dose.name in value:
                    if request.POST[value] != '':
                        dose.given = True
                        date = request.POST[value]
                        formatted_date = datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
                        dose.date = formatted_date
                        dose.save()
                        return HttpResponseRedirect(reverse('schedule:chart', args=(family.id,member.id,)))

    return render(request, 'schedule/update.html', {'values': values})


@login_required
def new_family_view(request):
    return render(request, 'schedule/new_family.html', None)


@login_required
def add_family(request):
    user = request.user
    family = user.patientfamily_set.create(last_name=request.POST['last_name'])
    family.save()
    return HttpResponseRedirect(reverse('schedule:family', args=(family.id,)))


@login_required
def family_view(request, family_id):
    user = request.user
    family = user.patientfamily_set.filter(id=family_id)[0]
    members = family.patient_set.all()
    return render(request, 'schedule/family.html', {'family': family, 'members': members, })


# Helper function used by new_schedule()
def create_doses(vaccine, number):
    for i in range(1, number+1):
        dose = vaccine.dose_set.create(name=vaccine.name+"_"+str(i))
        dose.save()


def new_schedule(member):

    # Create schedule
    schedule = member.schedule_set.create()
    schedule.save()

    # Hepatitis B Vaccine
    hepatitis_b = schedule.vaccine_set.create(name="hepatitis_b",description="Hepatitis B")
    hepatitis_b.save()
    create_doses(hepatitis_b, 5)

    # DTAP Vaccine
    dtap = schedule.vaccine_set.create(name="dtap",description="Diptheria, Tetanus, Pertusis")
    dtap.save()
    create_doses(dtap, 6)

    # H. Influenzae Vaccine
    influenzae = schedule.vaccine_set.create(name="influenzae", description="H. influenzae type b")
    influenzae.save()
    create_doses(influenzae, 4)

    # Pollo Vaccine
    pollo = schedule.vaccine_set.create(name="pollo", description="Inactivated Pollo")
    pollo.save()
    create_doses(pollo, 4)

    # Pneumococcal Vaccine
    pneumococcal = schedule.vaccine_set.create(name='pneumococcal', description="Pneumococcal Conjugate")
    pneumococcal.save()
    create_doses(pneumococcal, 4)

    # MMR Vaccine
    mmr = schedule.vaccine_set.create(name='mmr', description='Measles, Mumps, Rubella')
    mmr.save()
    create_doses(mmr, 3)

    # Varicella Vaccine
    varicella = schedule.vaccine_set.create(name='varicella', description="Varicella (Chickenpox)")
    varicella.save()
    create_doses(varicella, 2)

    # Hepatitis A Vaccine
    hepatitis_a = schedule.vaccine_set.create(name='hepatitis_a', description="Hepatitis A")
    hepatitis_a.save()
    create_doses(hepatitis_a, 1)


@login_required
def add_member(request, family_id):
    user = request.user
    family = user.patientfamily_set.filter(id=family_id)[0]
    member = family.patient_set.create(last_name=request.POST['last_name'], first_name=request.POST['first_name'])
    member.save()
    new_schedule(member)
    return HttpResponseRedirect(reverse('schedule:family', args=(family_id,)))
