from django.urls import get_resolver

resolver = get_resolver()
urls = []

for urlpattern in resolver.url_patterns:
    if hasattr(urlpattern, 'url_patterns'):
        # Handle include() patterns
        for include_pattern in urlpattern.url_patterns:
            urls.append(str(include_pattern.pattern))
    else:
        urls.append(str(urlpattern.pattern))

for url in urls:
    print(url)
