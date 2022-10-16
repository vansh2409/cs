import { NextPage } from 'next';

//Doesn't actually render anything and just runs server-side with getInitialProps
const Snippet: NextPage = () => null

//Get Gitlab or Gist script url from query
Snippet.getInitialProps = async ({ query, res }) => {
	const snippet = `
	<!doctype html>
	<html>
	<head>
		<title>Anna Coding</title>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<base target="_blank">
		<style>
			body {
				margin: 0
			}
			.gitlab-embed-snippets {
				margin: unset !important;
			}
			.gitlab-embed-snippets .btn-group a.btn {
				padding: 4px 4px !important;
			}
		</style>
	</head>
	<body>
	    //Get Gitlab or Gist script tag
		<script src="https://gist.github.com/vansh2409/c7145d0208d258b5779650a34dc78a05.js"></script>
	</body>
	</html>`;
	// Send snippet
	res.end(snippet);
};

export default Snippet;