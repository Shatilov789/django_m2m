from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tabel, Scope

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass

class TableInlineFormset(BaseInlineFormSet):

    def clean(self):
        super(TableInlineFormset, self).clean()
        total_checked = 0
        for form in self.forms:
            if not form.is_valid():
                return
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                if form.cleaned_data['is_main']:
                    total_checked += 1
        if total_checked > 1:
            raise ValidationError('У же есть один основной раздел, выебирте один!')

        if total_checked < 1:
            raise ValidationError("Вам необходимо выбрать один основной раздел!")

        return super().clean()  # вызываем базовый код переопределяемого метода


class TableInline(admin.TabularInline):
      model = Tabel
      formset = TableInlineFormset


class ArticleAdmin(admin.ModelAdmin):

    inlines = [
        TableInline
    ]

admin.site.register(Article, ArticleAdmin)
