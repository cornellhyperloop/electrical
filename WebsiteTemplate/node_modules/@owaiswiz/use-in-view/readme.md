## useInView

Check if your component is in viewport using this simple hook!

[![Build Status](https://travis-ci.org/elinadenfina/useInView.svg?branch=master)](https://travis-ci.org/elinadenfina/useInView)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
![GitHub top language](https://img.shields.io/github/languages/top/elinadenfina/useinview.svg)
![npm bundle size (scoped)](https://img.shields.io/bundlephobia/minzip/use-in-view/1.0.7.svg)
![David](https://img.shields.io/david/elinadenfina/useinview.svg)

⭐ ⭐ Check out a working demo [here](https://elinadenfina.github.io/useInView/) ⭐ ⭐

## Install

```
$ yarn add use-in-view
```

## Usage

```jsx
import useInView from 'use-in-view';

const AnimatedComponent = () => {
	const offset = 30;
	const [ref, inView] = useInView(offset);

	return (
		<div className={`${inView && 'in-view'}`} ref={ref}>
			Animate me!
		</div>
	);
};
```
