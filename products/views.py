from django.shortcuts import render, redirect
from .forms import NewProductForm, ProductForm
from .models import ProductImage, Product, Comment
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required(login_url='login')
def new_product(request):
    if request.method == 'GET':
        form =NewProductForm()
        context ={
            'form':form
        }

        return render(request,'product_new.html',context)

    elif request.method == 'POST':
        form =NewProductForm(data =request.POST, files = request.FILES)

        if form.is_valid():
            product = form.save(request)

            for image in request.FILES.getlist('images'):
                ProductImage.objects.create(product=product,image=image)
            messages.success(request,'Product Added Successfully')
            return redirect('main:index')

        return render(request,'product_new.html',{'form':form})


def product_detail(request,product_id):
    product = get_object_or_404(Product, id=product_id)

    if 'recently_viewed' in request.session:
        r_viewed = request.session['recently_viewed']
        if not product.id in r_viewed:
            r_viewed.append(product.id)
            request.session['recently_viewed'] = r_viewed
            request.session.modified = True
    else:
        request.session['recently_viewed'] =[product.id]
        
    context = {
        'product':product
    }
    return render(request,'product_detail.html',context)

@login_required(login_url='login')
def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user==product.author:
        if request.method=='GET':
            form = ProductForm(instance=product)
            return render(request, 'product_update.html', {'form':form, 'product':product})
        elif request.method == 'POST':
            form = ProductForm(instance = product, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                if request.FILES.getlist('images'):
                    ProductImage.objects.filter(product=product).delete()
                    productimages = []
                    for image in request.FILES.getlist("images"):
                        productimages.append(ProductImage(image=image, product=product))
                    ProductImage.objects.bulk_create(
                        productimages
                    )
                messages.success(request, 'Successfully Updated!')        
                return redirect('products:detail', product.id)
            return render(request, 'product_update.html', {'form':form, 'product':product})
    else:
        messages.error(request, 'Access danied!')
        return redirect('main:index')   


def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user == product.author:
        if request.method == 'POST':
            product.delete()
            messages.info(request, 'Successfully Deleted!')
            return redirect('main:index')
        return render(request, 'product_delete.html', {'product':product})

    else:
        messages.error(request, 'Access denied!')
        return redirect('main:index')

@login_required(login_url='login')
def new_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)   
    if request.method == 'POST':
        Comment.objects.create(
            author = request.user,
            product= product,
            body = request.POST['body']
        )
        messages.info(request, 'Successfully Sended!')
        return redirect('products:detail', product_id)
    return HttpResponse("add comment")

@login_required(login_url='login')
def delete_comment(request, product_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        comment.delete()
        messages.info(request, 'Successfully Deleted!')
        return redirect('products:detail', product_id)
    return redirect('products:detail', product_id)

    