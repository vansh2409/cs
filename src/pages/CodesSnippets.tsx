import React, { useState, useEffect, useRef } from 'react';
import { Spin } from 'antd';

import './CodesSnippet.scss';

interface CodesSnippetProps {
	embedScript: string;
}

const CodesSnippets: React.FunctionComponent<CodesSnippetProps> = ({ embedScript }: { embedScript: string }) => {
	const [isLoading, setIsLoading] = useState(true);

	// Create iframe Ref
	const iframeRef: { current: any } = useRef({
		current: {},
	});

    // Get url from script tag
	const url = embedScript.match('//(.*).js"')[1];

	// function to get iframe doc height
	const getIframeDocHeight = doc => {
		doc = doc || document;
		const body = doc.body,
			html = doc.documentElement;
		const height = Math.max(
			body.scrollHeight,
			body.offsetHeight,
			html.clientHeight,
			html.scrollHeight,
			html.offsetHeight
		);
		return height;
	};

    // Do someting afeter iframe loaded
	const onIframeLoad = () => {
		setIsLoading(false);
		// We set iframe height dynamically based on iframe doc height
		const ifrm = iframeRef.current;
		const doc = ifrm.contentDocument ? ifrm.contentDocument : ifrm.contentWindow.document;
		ifrm.style.height = getIframeDocHeight(doc) + 'px';
	};

	return (
		<div className="iframe-container">
			{isLoading && <Spin tip="Codes snippet is loading..." />}
			<iframe
				ref={iframeRef}
				onLoad={onIframeLoad}
				className="iframe"
				// Set url 
				src={`/snippet?url=https://gist.github.com/vansh2409/c7145d0208d258b5779650a34dc78a05.js`}
			></iframe>
		</div>
	);
};

export default CodesSnippets;
