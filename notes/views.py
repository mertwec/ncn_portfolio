import json
import os

from django.shortcuts import render, redirect
from django.views.decorators import http
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from notes.models import Note, SiteNote, Category
from notes.forms import NoteForm
from ncn import settings
from ncn.components.tools_view import paginate_object


# --Notes-----------------------------------------------------------
@never_cache
@http.require_http_methods(["GET", "POST"])
def notes(request):
    notes_list = Note.objects.all()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/notes")

    form = NoteForm()
    return render(
        request,
        template_name="notes/notes.html",
        context={
            "notes": notes_list,
            "form": form,
            "title": "Notes"
        }
    )


def delete_note(request, note_id):
    Note.objects.get(pk=note_id).delete()
    return redirect("/notes")   # redirect to url = url/notes


# --Sites----------------------------------------------------------

@never_cache
@http.require_safe
def sites_all(request, category_name=''):
    if not category_name or category_name == "All":
        sites = SiteNote.objects.all()
    else:
        sites = SiteNote.get_by_category(category_name)

    ppage = paginate_object(request, sites, 10)

    return render(
        request,
        template_name="notes/sites.html",
        context={
            "title": f"{category_name} Links",
            "sites": ppage['objects_on_page'],
            "category": category_name,
            'page': ppage['page'],
            # "categories": categorys,      # add in middleware
        }
    )


def delete_site(request, site_id):
    SiteNote.objects.get(pk=site_id).delete()
    return redirect("/notes/sites/")   # redirect to url = url/notes


@login_required(login_url=settings.LOGIN_URL)
def dump_sites_db(request):
    data_sites = SiteNote.get_sites()
    file = os.path.join(settings.DUMP_DB_PATH, settings.DUMP_FILE)

    if not os.path.exists(settings.DUMP_DB_PATH):
        os.makedirs(settings.DUMP_DB_PATH)

    with open(file, "w") as write_file:
        json.dump(data_sites, write_file, ensure_ascii=False)
        print('\ncreated \n')
    return render(
        request,
        template_name="notes/dump_sites.html",
        context={
            "title": "Dump sites_DB",
            "dump_file": settings.DUMP_FILE,
        }
    )


@login_required(login_url=settings.LOGIN_URL)
def load_dump_sites_db(request):
    """get uploaded file
    """
    if request.method == "POST":
        # if the post request has a file under the input name 'document'
        request_file = request.FILES['document'] if 'document' in request.FILES else None

        if request_file:

            if request_file.name.split('.')[1] != 'json':
                print('load only json file')
                return redirect("/notes/sites/")

            # open and read uploaded file
            with request_file.open(mode='r') as rfile:
                upload_data = json.loads(rfile.read())     # list[dict]
                for upl_site in upload_data:
                    category_ = Category.objects.get_or_create(
                        name=upl_site["cat_name"])

                    print(f'{upl_site["cat_name"]} added {category_}')
                    sn = SiteNote.objects.update_or_create(
                        title=upl_site["title"],
                        url=upl_site["url"],
                        description=upl_site["description"],
                        category=category_[0],
                    )
                    print(sn)

            # save attached file
            # fs = FileSystemStorage()
            # file = fs.save(request_file.name, request_file)
            # # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
            # fileurl = fs.url(file)
        return redirect("/notes/sites/")

    return render(
        request,
        template_name="notes/load_sites.html",
        context={
            "title": "Load sites_DB",
        }
    )
