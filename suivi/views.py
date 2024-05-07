from django.shortcuts import render
from suivi.forms import *
from suivi.models import *
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from  django.views.decorators.cache import cache_control





@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    return render(request, 'suivi/home.html')





@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def itemsliste(request):
    items = Planitems.objects.all()
    context = {"items":items}
    return render(request, 'suivi/planitemsliste.html',context)




@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def addplanitems(request):
    if request.method=="POST":
        form = PlanitemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Ajour effectué !")
            return redirect('itemsliste')
        else:
            return render(request, 'suivi/add_planitems.html', {'form': form})
    else:
        form = PlanitemsForm()
        return render(request, 'suivi/add_planitems.html', {'form': form})
    




@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editplanitems(request, id):
    item = Planitems.objects.get(id=id)
    if request.method == 'POST':
        form = PlanitemsForm(request.POST, instance=item)
        if form.is_valid():
            form.save(id)
            messages.success(request, "Modification effectué avec susccès!")
            return redirect('itemsliste')
    else:
        form = PlanitemsForm(instance=item)
    return render(request, 'suivi/edit_planitems.html', {'item':item, 'form':form})





@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dossier(request):
    # Check if user is authenticated
    if request.user.is_authenticated:
        # Get user authenticated
        agent = user=request.user
        # get All planitems when user is owner
        items = Planitems.objects.filter(agent_id=agent)

        # Check id user have planitems
        if items.exists():
            context = {"items": items}
            return render(request, 'suivi/dossier.html', context)

    return render(request, 'suivi/dossier.html')





@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def listdoc(request):
    # Check if user is authenticated
    if request.user.is_authenticated:
        # Get user authenticated
        agent = user=request.user
        # get All Dossier when user is owner
        dossiers = Dossiers.objects.filter(owner=agent)

        # Check if user have Dossier
        if dossiers.exists():
            context = {"dossiers": dossiers}
            return render(request, 'suivi/listdoc.html',context)

    return render(request, 'suivi/listdoc.html')





@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adddossier(request, id):
    # Get a planitems objet
    plan_item = get_object_or_404(Planitems, id=id)

    if request.method == "POST":
        # Create a form
        form = DossierForm(request.POST, request.FILES)
        if form.is_valid():
            # Sauve a form
            dossier = form.save(commit=False)
            dossier.planitem_id = plan_item
            if request.user.is_authenticated:
                # Get user authenticated
                agent = user=request.user
                dossier.owner = agent
                dossier.save()
            messages.success(request, "Dossier ajouté avec succès !")
            return redirect('listdoc')

    else:
        # Initialize a form with data
        form = DossierForm(initial={'plan_item': plan_item})

    # Show a form
    return render(request, 'suivi/add_dossier.html', {'form': form})






@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editdossier(request, dossier_id):
    # Get a planitems objet
    dossier = get_object_or_404(Dossiers, id=dossier_id)

    if request.method == "POST":
         # Create a form
        form = DossierForm(request.POST, request.FILES, instance=dossier)

        if form.is_valid():
            # Save form
            updated_dossier = form.save(commit=False)
            
            # check if user authenticated
            if request.user.is_authenticated:
                updated_dossier.owner = request.user
            
            # Save a form
            updated_dossier.save()

            messages.success(request, "Dossier modifié avec succès !")
            return redirect('listdoc')

    else:
        # Initialize a form with data
        form = DossierForm(instance=dossier)

    # Show a form
    return render(request, 'suivi/editdossier.html', {'form': form})






@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def list_dossier_lots(request, dossier_id):
    # Récupère l'objet Dossier correspondant à l'identifiant
    dossier = get_object_or_404(Dossiers, id=dossier_id)

    # Récupère tous les lots associés à ce dossier
    lots = Lots.objects.filter(dossier_id=dossier)

    # Préparer le contexte à passer au template
    context = {
        'dossier': dossier,
        'lots': lots
    }

    # Rendre le template avec le contexte
    return render(request, 'suivi/dossier_lots.html', context)



@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adddlot(request, id):
    # Get a planitems objet
    dossier = get_object_or_404(Dossiers, id=id)

    if request.method == "POST":
        # Create a form
        form = LotForm(request.POST, request.FILES)
        if form.is_valid():
            # Sauve a form
            lot = form.save(commit=False)
            lot.dossier_id = dossier
            lot.save()
            messages.success(request, "Lot ajouté avec succès !")
            return redirect('dossier_lots', dossier_id=id)

    else:
        # Initialize a form with data
        form = LotForm(initial={'dossier': dossier})

    # Show a form
    return render(request, 'suivi/add_lot.html', {'form': form})




@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editlot(request, id):
    # Récupère l'objet Lot à modifier
    lot = get_object_or_404(Lots, id=id)

    if request.method == "POST":
        # Create new form data
        form = LotForm(request.POST, request.FILES, instance=lot)

        if form.is_valid():
            # Save form
            updated_lot = form.save()
            # Get dossier id
            dossier_id = updated_lot.dossier_id.id
            # Reddirect this url
            messages.success(request, f"{updated_lot.num_lot} de {updated_lot.dossier_id.numero_doss} modifié avec succès !")
            return redirect('dossier_lots', dossier_id=dossier_id)

    else:
        # Initialize a form with data
        form = LotForm(instance=lot)

    return render(request, 'suivi/editlot.html', {'form': form, 'lot': lot})




@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def suivi(request):
    # Check if user is authenticated
    if request.user.is_authenticated:
        # Get user authenticated
        agent = user=request.user
        # get All Dossier when user is owner
        dossiers = Dossiers.objects.filter(owner=agent)
        # Maintenant, filtrer les lots associés à ces dossiers
        lots_associated = Lots.objects.filter(dossier_id__in=dossiers).count()

        # Check if user have Dossier
        if dossiers.exists():
            context = {"dossiers": dossiers, "lots_associated":lots_associated}
            return render(request, 'suivi/suivi.html',context)

    return render(request, 'suivi/suivi.html')




@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def process_dossier(request):
    return render(request, 'suivi/process_dossier.html')
