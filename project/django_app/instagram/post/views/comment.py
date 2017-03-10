from django.shortcuts import redirect

from post.forms import CommentForm
from post.models.post import Post
from post.models.comment import Comment

__all__ = (
    'comment_add',
    'comment_delete',
)


def comment_add(request, post_id):
    print('test2')
    if request.method == 'POST':
        print('test1')
        # 전달받은 POST데이터에서 'content'값을 할당
        form = CommentForm(data=request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            # HttpRequest에는 항상 User정보가 전달된다
            user = request.user
            # URL인자로 전달된 post_id값을 사용
            post = Post.objects.get(id=post_id)
            post.add_comment(user, content)

        return redirect('post:list')


def comment_delete(request, post_id, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        if comment.author == request.user:
            comment.delete()
    return redirect('post:detail', post_id=post_id)
