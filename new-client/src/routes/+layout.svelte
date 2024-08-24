<div class="layout">
	<slot />
</div>

<style lang="scss">
	:global(body) {
		margin: 0;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu',
			'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
	}

	.layout {
		display: flex;
		width: calc(100% - 10px);
		min-height: calc(100vh - 10px);
		background-color: #35495e;
		border: 5px solid #42b883;
	}
</style>
