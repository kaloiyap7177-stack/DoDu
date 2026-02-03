from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, Category, TaskCategory
from .forms import TaskForm, CategoryForm

# Create your views here.

def home(request):
    context = {
        'title': 'DuDo - Home',
    }
    return render(request, 'dudo_app/home.html', context)

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    categories = Category.objects.filter(user=request.user)
    
    # Filter by category if specified
    category_id = request.GET.get('category')
    if category_id:
        tasks = tasks.filter(taskcategory__category_id=category_id)
    
    # Filter by completion status
    completed = request.GET.get('completed')
    if completed is not None:
        tasks = tasks.filter(completed=completed == 'true')
    
    context = {
        'tasks': tasks,
        'categories': categories,
        'title': 'My Tasks',
    }
    return render(request, 'dudo_app/task_list.html', context)

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    context = {
        'task': task,
        'title': task.title,
    }
    return render(request, 'dudo_app/task_detail.html', context)

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            
            # Handle categories
            categories = request.POST.getlist('categories')
            for category_id in categories:
                category = Category.objects.get(id=category_id, user=request.user)
                TaskCategory.objects.create(task=task, category=category)
            
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()
    
    categories = Category.objects.filter(user=request.user)
    context = {
        'form': form,
        'categories': categories,
        'title': 'Create Task',
    }
    return render(request, 'dudo_app/create_task.html', context)

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            
            # Update categories
            TaskCategory.objects.filter(task=task).delete()
            categories = request.POST.getlist('categories')
            for category_id in categories:
                category = Category.objects.get(id=category_id, user=request.user)
                TaskCategory.objects.create(task=task, category=category)
            
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
        selected_categories = task.taskcategory_set.values_list('category_id', flat=True)
    
    categories = Category.objects.filter(user=request.user)
    context = {
        'form': form,
        'task': task,
        'categories': categories,
        'selected_categories': selected_categories,
        'title': 'Update Task',
    }
    return render(request, 'dudo_app/update_task.html', context)

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')
    
    context = {
        'task': task,
        'title': 'Delete Task',
    }
    return render(request, 'dudo_app/delete_task.html', context)

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    context = {
        'categories': categories,
        'title': 'Categories',
    }
    return render(request, 'dudo_app/category_list.html', context)

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'Category created successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    
    context = {
        'form': form,
        'title': 'Create Category',
    }
    return render(request, 'dudo_app/create_category.html', context)
