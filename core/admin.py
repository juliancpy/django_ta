from django.contrib import admin
from .models import MedicalTerm, Post

class MedicalTermInline(admin.StackedInline):
    #form = MedicalTermForm
    model = MedicalTerm
    fields = ('start','end','ngram', 'term', 'cui', 'similarity','semtype','preferred')
    extra = 1
    verbose_name_plural = 'Medical Terms (Sortable)'
    sortable = 'order'
    show_change_link = True




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('guid','title')
    list_display = ('date', 'title', 'content', 'url','isAEs_choices','medterms')
    sortable = 'order'
    inlines = (MedicalTermInline,)

    def medterms(self, obj):
        return len(obj.medicalterm_set.all())
