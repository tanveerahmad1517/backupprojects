from django import forms
from .models import Post, Comment, Category
from tinymce import TinyMCE



class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False




class TweetModelForm(forms.ModelForm):
    description = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = (
            # 'user',
             'title', 'description', 'image', 'category'
        )

    def __init__(self, user, *args, **kwargs):
        super(TweetModelForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)
