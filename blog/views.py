from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView , UpdateView
from django.views.generic import ListView ,DetailView , DeleteView ,View, TemplateView
from .forms import *
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout ,authenticate
from django.db.models import Q
import socket # for get id address
import random

# Starting  Working


class About(ListView):
    model = Category
    template_name = 'blog/about.html'
    context_object_name = 'category'


class Home(View):
    def get(self,request):
        context = {
            "blog":Blog.objects.all(),
            "category":Category.objects.all(),
        }
        return render(request,'blog/home.html',context)


class BlogDetail(View):
    def get(self,request,pk):
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        check = BlogView.objects.filter(Q(ip=IPAddr)&Q(blog=pk)).count()

        check_like = Like.objects.filter(ip=IPAddr,blog_id=pk)


        if(check != 1):
            data = BlogView()
            data.blog = Blog(pk)
            data.view += 1
            data.ip = IPAddr
            data.save()
        else:
            pass
        context = {
            "blog":Blog.objects.get(b_id=pk),
            "category":Category.objects.all(),
            "comments":Comments.objects.filter(blog_id=pk),
            "last":Comments.objects.filter(blog_id=pk).last(),
            "checklike":check_like,

        }
        return render(request,'blog/details.html',context)



class CategoryBlog(View):
    def get(self,request,pk):
        context = {
            "blog":Blog.objects.filter(category = pk),
            "category":Category.objects.all(),
        }
        return render(request,'blog/home.html',context)


class BlogofProfile(View):
    def get(self,request,pk):
        data = {
            "blog":Blog.objects.filter(bloger=pk),
            "category": Category.objects.all(),

        }
        return render(request,'blog/home.html',data)


class Search(View):
    def get(self,request):
        search = request.GET.get('search')
        cond = Q(title__icontains=search) | Q(category__title__icontains = search)
        context = {
            "blog":Blog.objects.filter(cond),
            "category":Category.objects.all(),
        }
        return render(request,'blog/home.html',context)


#_---------------------------------------------------------
class Signup(View):
    def get(self,request):
        form = SignupForm()
        no1 = random.randint(1,20)
        opr = random.choice(['+','-'])
        no2 = random.randint(0,20)
        ans = eval(str(no1)+opr+str(no2))
        context = {
            "form":form,"category":Category.objects.all(),
            "no1":no1,
            "opr":opr,
            "no2":no2,
            "ans":ans,
        }
        return render(request,'blog/signup.html',context)

    def post(self,request):
        form = SignupForm(request.POST or None)
        ans1 = request.POST.get('ans1')
        ans2 = request.POST.get('ans2')
        if (ans1 == ans2):
            if form.is_valid():
                form.save()
                return render(request,'blog/login.html')
            else:
                return redirect('signup')
        else:
            return redirect('signup')



class AddUserDetail(LoginRequiredMixin,View):
    def get(self,request):
        form = UserDetailForm()
        return render(request,'blog/adduserdetail.html',{"form":form})

    def post(self,request):
        form = UserDetailForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            f = form.save(commit=False)
            f.users = request.user
            f.save()
            return redirect('home')


class Login(View):
    def get(self,request):
        context = {"category": Category.objects.all()}
        return render(request,'blog/login.html',context)

    def post(self,request):
        username = request.POST.get('email')
        password = request.POST.get('password')

        try:
            email = User.objects.get(email=username)
            user = authenticate(username=email.username,password = password)
        except:
            return redirect('login')

        if(user is not None):
            login(request,user)
            cond = UserDetail.objects.filter(users=request.user).count()
            if(cond == 1):
                return redirect('profile')
            else:
                return redirect('adduserdetail')
        else:
            return render(request,'blog/login.html')




class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('home')




class Profile(LoginRequiredMixin,View):
    def get(self,request):
        if UserDetail.objects.filter(users=request.user).exists():
            context = {"profile":UserDetail.objects.get(users = request.user)}
            return render(request,'private/profile.html',context)
        else:
            return redirect('adduserdetail')



class AddNewArticle(LoginRequiredMixin,View):
    def get(self,request):
        if UserDetail.objects.filter(users=request.user).exists():
            form = BlogForm()
            return render(request,'private/addblog.html',{"forms":form})
        else:
            return redirect('adduserdetail')

    def post(self,request):
        form = BlogForm(request.POST or None , request.FILES or None)
        user  = UserDetail.objects.get(users=request.user)

        if form.is_valid():
            u = form.save(commit=False)
            u.bloger = user
            u.save()
            return redirect('addblog')
        else:
            return redirect('addblog')




class MyAllArticle(LoginRequiredMixin,View):
    def get(self,request):
        if UserDetail.objects.filter(users=request.user).exists():
            context = {"allarticle":Blog.objects.filter(bloger__users = request.user)}
            return render(request,'private/allblog.html',context)
        else:
            return redirect('adduserdetail')



class DeleteArticle(LoginRequiredMixin,View):
    def get(self,request,pk):
        data = Blog.objects.get(b_id=pk)
        data.delete()
        return redirect('allarticle')



class ProfileUpdate(LoginRequiredMixin,UpdateView):
    model = UserDetail
    form_class = UserDetailForm
    template_name = 'private/updateprofile.html'

    def form_valid(self,form):
        form.save()
        return redirect('profile')


class Likes(View):
    def get(self,request,pk):
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        check = Like.objects.filter(Q(ip=IPAddr) & Q(blog_id=pk)).count()

        if(check != 1):
            like = Like()
            like.ip = IPAddr
            like.blog_id = Blog(pk)
            like.save()
            return redirect('blogdetail', pk = pk)
        else:
            check = Like.objects.get(Q(ip=IPAddr) & Q(blog_id=pk))
            check.delete()
            return redirect('blogdetail', pk=pk)


class Comment(View):
    def post(self,request,pk):
        com  = request.POST.get('com')

        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        c = Comments()
        c.ip = IPAddr
        c.blog_id = Blog(pk)
        c.comment = com
        c.save()
        return redirect('blogdetail', pk=pk)

