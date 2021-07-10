from django.shortcuts import render, redirect
from django.views import View, generic
from home.forms import SignUpForm, AddPostForm
from django.urls import reverse_lazy
from .models import Post

class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Index(View):
    def get(self, request):
        user = request.user
        context = {
            'user': user
        }
        return render(request, 'index.html', context)

class Addpost(View):

    def get(self, request):

        if request.user.is_authenticated:
            user = request.user
            form = AddPostForm()

            context = {
                'form': form
            }

            return render(request, 'addpost.html', context)
        else:
            return render(request, 'addpost.html')
    
    def post(self, request):

        user = request.user
        form = AddPostForm(request.POST)
        
        if form.is_valid():
            mstr = form.save(commit = False)
            mstr.user = user
            mstr.save()
            return redirect('addpost')
        else:
            return render(request, 'addpost.html', {'form': form})

class ViewPost(View):

    def get(self, request):
        
        post = Post.objects.all()

        data = {
            'post': post
        }

        return render(request, 'viewpost.html', data)