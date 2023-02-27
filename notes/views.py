from django.shortcuts import render, redirect
from django.views.decorators import http 
from django.core.paginator import Paginator
from notes.models import Note, SiteNote, Category
from notes.forms import NoteForm


@http.require_http_methods(["GET", "POST"])
def notes(request):
    template = "notes/notes.html"
    notes = Note.objects.all()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.save()
            return render(
                request,
                template_name="notes/notes.html",
                context={"notes": notes, "form": NoteForm()}
            )
    form = NoteForm()
    return render(
        request,
        template_name="notes/notes.html",
        context={"notes": notes, "form": form}
    )


def delete_note(request, note_id):
    Note.objects.get(pk=note_id).delete()
    return redirect("/notes")   # redirect to url = url/notes

# ------------------------------------------------------------


@http.require_safe
def sites_all(request, category_name=''):
    if not category_name or category_name == "All": 
        sites = SiteNote.objects.all()
    else:
        sites = SiteNote.get_by_category(category_name)
    
    paginator = Paginator(sites, 7)
    if 'page' in request.GET:
        page_num = request.GET["page"]
    else:
        page_num = 1

    page = paginator.get_page(page_num)     # get current page
    sites_on_page = page.object_list

    # import pdb; pdb.set_trace()

    return render(
        request,
        template_name="notes/sites.html",
        context={
            "title": f"{category_name} Links",
            "sites": sites_on_page,
            "category": category_name,
            'page': page,
            # "categories": categorys,      # add in middleware
        }
    )


@http.require_POST
def add_site():
    pass


def delete_site(request, site_id):
    SiteNote.objects.get(pk=site_id).delete()
    return redirect("/notes/sites/")   # redirect to url = url/notes
