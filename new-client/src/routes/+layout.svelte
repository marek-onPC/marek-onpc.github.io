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
    position: relative;
    overflow: hidden;
  }

  :global(.button) {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 130px;
    height: 30px;
    color: #fff;
    font-size: 0.875rem;
    line-height: 1.75;
    font-weight: 600;
    background-color: #42b883;
    box-shadow:
      rgba(#000, 0.2) 0px 3px 1px -2px,
      rgba(#000, 0.14) 0px 2px 2px 0px,
      rgba(#000, 0.12) 0px 1px;
    padding: 10px;
    border-radius: 2px;
    border-width: 0px;
    text-decoration: none;
    transition: 0.25s ease-in-out;
    cursor: pointer;

    &:hover {
      background-color: #2e805b;
    }
  }

  :global(.input) {
    width: 175px;
    height: 20px;
    padding: 20px 10px 10px 10px;
    border-radius: 2px;
    border-width: 0px;

    &:focus {
      outline: none;
    }
  }
</style>
