from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from child.models import Child

class ChildForm(ModelForm):
    class Meta:
        model = Child

def child_list(request, template_name='child/child_list.html'):
    child = Child.objects.all()
    data = {}
    data['object_list'] = child
    return render(request, template_name, data)

def child_create(request, template_name='child/child_form.html'):
    form = ChildForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('child_list')
    return render(request, template_name, {'form':form})

def child_update(request, pk, template_name='child/child_form.html'):
    child = get_object_or_404(Child, pk=pk)
    form = ChildForm(request.POST or None, instance=child)
    if form.is_valid():
        form.save()
        return redirect('child_list')
    return render(request, template_name, {'form':form})

def child_delete(request, pk, template_name='child/child_confirm_delete.html'):
    child = get_object_or_404(Child, pk=pk)    
    if request.method=='POST':
        child.delete()
        return redirect('child_list')
    return render(request, template_name, {'object':child})