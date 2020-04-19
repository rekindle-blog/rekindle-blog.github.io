---
title: Tags
permalink: /tags/:tag
---
<div class="section-title col-md-12 mt-4">
	<h2 id="{{ tag | replace: " ","-" }}">Tag <span class="text-capitalize">{{ tag }}</span></h2>
</div>
<div class="row listrecent">
	{% for t in site.tags | where_exp: "t", "t[0] == tag" %}
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
</div>
