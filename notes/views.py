from django.shortcuts import render, redirect

from notes.models import Note
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
                    context={"notes": notes, "form":NoteForm()}
                    )
        
    notes = Note.objects.all()
    form = NoteForm()
    return render(
        request, 
        template_name="notes/notes.html",
        context={"notes": notes, "form":form}
        )


def note_delete(request, note_id):
    Note.objects.get(pk=note_id).delete()
    return redirect("/notes")
