from django import template
register = template.Library()

@register.filter(name='page_filter')
def filtro_navegador(self,items):
    current_value = items.number
    valmax = items.paginator.page_range[-1]
    gapval = 12
    valini = current_value-gapval

    if valini <=0:
        valini = 1
    
    valend = 1+current_value+gapval
    if valend > valmax:
        valend = valmax+1

    return range(valini, valend)