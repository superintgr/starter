# pip install wikipedia-api

import wikipediaapi
import json

def fetch_wikipedia_content(title):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(title)

    if not page_py.exists():
        return None

    content_dict = {'title': page_py.title, 'sections': []}

    for section in page_py.sections:
        section_dict = {'title': section.title, 'content': section.text}
        content_dict['sections'].append(section_dict)

    return content_dict

# Replace 'Your Wikipedia Article Title' with the desired article title
article_title = 'Your Wikipedia Article Title'
result = fetch_wikipedia_content(article_title)

if result:
    # Output the result as a JSON string
    json_result = json.dumps(result, indent=2)
    print(json_result)
else:
    print(f"The Wikipedia article '{article_title}' does not exist.")
