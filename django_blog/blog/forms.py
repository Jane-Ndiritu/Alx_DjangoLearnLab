from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """Form for creating and updating blog posts"""
    
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Write your blog post here...'
            })
        }
        labels = {
            'title': 'Post Title',
            'content': 'Content'
        }
        help_texts = {
            'content': 'Markdown formatting is supported.'
        }
    
    def clean_title(self):
        """Custom validation for title field"""
        title = self.cleaned_data.get('title')
        
        # Title length validation
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        if len(title) > 200:
            raise forms.ValidationError("Title cannot exceed 200 characters.")
        
        # Check for profanity (simple example)
        banned_words = ['spam', 'advertisement', 'clickbait']
        for word in banned_words:
            if word in title.lower():
                raise forms.ValidationError(f"Title contains inappropriate word: {word}")
        
        return title
    
    def clean_content(self):
        """Custom validation for content field"""
        content = self.cleaned_data.get('content')
        
        # Minimum content length
        if len(content) < 50:
            raise forms.ValidationError("Content must be at least 50 characters long.")
        
        # Check content quality
        if len(content.split()) < 10:
            raise forms.ValidationError("Content seems too short. Please provide more detail.")
        
        return content