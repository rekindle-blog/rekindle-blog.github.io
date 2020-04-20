---
title: Tags
permalink: /tags/:name
---
<h1>Archive of posts with {{ page.type }} '{{ page.title }}'</h1>
<ul class="posts">
  {% for post in page.posts %}
    <li>
      <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
      <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

<!--<div class="section-title col-md-12 mt-4">
	<h2 id="{{ name | replace: " ","-" }}">Tag <span class="text-capitalize">{{ name }}</span></h2>
</div>
<div class="row listrecent">
	{% for t in site.tags | where_exp: "t", "t[0] == name" %}
		{% assign pages_list = t[1] %}
		{% for post in pages_list %}
			{% if post.title != null %}
				{% if group == null or group == post.group %}
					{% include postbox.html %}
				{% endif %}
			{% endif %}
		{% endfor %}
		{% assign pages_list = nil %}
		{% assign group = nil %}
	{% endfor %}
</div>-->
