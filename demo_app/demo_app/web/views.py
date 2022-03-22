from django.views import generic as views

from demo_app.web.models import Item


class IndexView(views.ListView):
    template_name = 'index.html'
    model = Item


'''
# File path
- Correct:
```
file_path = path.join('dir1', 'dir2', 'dir3', ...)
```

- Incorrect
```
file_path = 'dir1/dir2/dir3/...' (Unix-style)
file_path = 'dir1\dir2\dir3\... (Win-style)
```
'''
