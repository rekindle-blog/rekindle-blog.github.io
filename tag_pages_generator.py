#!/usr/bin/env python

'''
Initial version by Long Qian
Modified by James Cuénod
'''

import os
import yaml

post_dir = '_posts/'
tag_dir = 'tag/'

def get_filenames():
    files = []
    for path in os.listdir(post_dir):
        if path.endswith(".md") or path.endswith(".html"):
            files.append(post_dir + path)
    return files

filenames = get_filenames()

total_tags = []
for filename in filenames:
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    file_yml_string = ""
    for line in f:
        if line.strip() == '---':
            if not crawl:
                crawl = True
                next
            else:
                crawl = False
                break
        if crawl:
            file_yml_string += line + "\n"
    f.close()
    yaml_object = yaml.safe_load(file_yml_string)
    if "tags" in yaml_object:
        total_tags.extend(yaml_object["tags"])
total_tags = set([t.strip() for t in total_tags])

tl = list(total_tags)
tl.sort()
print(tl)

existing_tags = []
old_tags = os.listdir(tag_dir)
for tag in old_tags:
    if tag.endswith(".md"):
        os.remove(tag_dir + tag)
        existing_tags.append(tag)
    
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    tag_filename = tag_dir + tag.replace(" ", "-") + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tag_page\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("---")
print("Tags generated:")
total_tag_count = total_tags.__len__()
print("Total Tags: ", str(total_tag_count).rjust(4))
new_tag_count = total_tag_count - existing_tags.__len__()
print("Total New:  ", str(new_tag_count).rjust(4))

