const SITE_REPOSITORY=`rekindle-blog/rekindle-blog.github.io`

const url = query => `https://api.github.com/search/code\?q\=${query}+in:file+repo:${SITE_REPOSITORY}`
const sanitize = q => encodeURI(q.replace(" ", "+"))

const fetch_results = async query => {
	const q = sanitize(query)
	const result_blob = await fetch(url(q), {
		method: 'GET',
		mode: 'cors',
		headers: {
			'Accept': 'application/vnd.github.v3.text-match+json',
			'Content-Type': 'application/json'
		}
	})
	const results = await result_blob.json()
	console.log(results)
	const {items} = results
	const post_items = items.filter(i => i.path.startsWith("_posts"))
}

console.log("search test")
