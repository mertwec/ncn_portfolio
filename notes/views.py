from django.shortcuts import render, redirect

from notes.models import Note, SiteNote, Category
from notes.forms import NoteForm


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

    notes = Note.objects.all()
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


def sites_all(request):
    sites = SiteNote.objects.all()
    # import pdb; pdb.set_trace()

    return render(
        request,
        template_name="notes/sites.html",
        context={
            "title": "Useful Links",
            "sites": sites,
            # "categories": categorys,
        }
    )


def sites_by_category(request, category_name):
    sites = SiteNote.get_by_category(category_name)
    return render(
        request,
        template_name="notes/sites.html",
        context={
            "title": "Useful Links",
            "sites": sites,
            # "categories": categorys,
        }
    )


def delete_site(request, site_id):
    SiteNote.objects.get(pk=site_id).delete()
    return redirect("/notes/sites/")   # redirect to url = url/notes
