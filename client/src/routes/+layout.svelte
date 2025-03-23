<script lang="ts">
  import { fade } from 'svelte/transition';

  export let data;

  const URL = '/about|/sheets';
  let isNavDisabled = !data.url.match(URL) ? true : false;

  $: data.url &&
    setTimeout(() => {
      isNavDisabled = !data.url.match(URL) ? true : false;
    }, 125);
</script>

<svelte:head>
  <title>marek-onpc</title>
</svelte:head>

<div class="layout">
  <div class={`${!isNavDisabled ? 'cheat-sheets' : 'home'}`}>
    <nav
      class={`navigation ${!data.url.match(URL) ? '--faded' : ''} ${isNavDisabled ? '--disabled' : ''}`}
    >
      <a class="button navigation__button" href="/">Home</a>
      <a class="button navigation__button" href="/sheets">Cheet sheets</a>
      <a class="button navigation__button" href="/about">About</a>
    </nav>
    {#key data.url}
      <div
        class={`layout__transition ${data.url.match(URL) ? '--nav-on' : '--nav-off'}`}
        in:fade={{ duration: 250, delay: 125 }}
        out:fade={{ duration: 125 }}
      >
        <slot />
      </div>
    {/key}
  </div>
</div>

<style lang="scss">
  :global(body) {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu',
      'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  :global(.--no-scroll) {
    overflow: hidden;
  }

  .cheat-sheets {
    display: flex;
    flex-direction: column;
    width: calc(100% - 20px);
    max-width: 1440px;
    padding: 10px;
    margin: 0 auto;
  }

  .home {
    width: 100%;
  }

  .navigation {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    width: auto;
    margin: 10px 10px 35px 10px;
    opacity: 1;
    transition: opacity 0.25s;

    &__button {
      margin: 10px;
    }

    &.--faded {
      opacity: 0;
    }

    &.--disabled {
      display: none;
      height: 0;
      margin: 0;
    }
  }

  .layout {
    display: flex;
    width: calc(100% - 10px);
    min-height: calc(100vh - 10px);
    background-color: #35495e;
    border: 5px solid #42b883;
    position: relative;
    overflow: hidden;

    &__transition {
      display: flex;
      width: 100%;
      min-height: calc(100vh - 10px);
      overflow: hidden;

      &.--nav-on {
        width: 100%;
        min-height: calc(100vh - 145px);
        justify-content: center;
      }

      &.--nav-off {
        min-height: calc(100vh - 30px);
      }

      &:nth-of-type(2) {
        position: absolute;
      }
    }
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

  :global(button) {
    height: 50px !important;
  }

  :global(.input) {
    width: 175px;
    height: 20px;
    padding: 15px;
    border-radius: 2px;
    border-width: 0px;

    &:focus {
      outline: none;
    }
  }
</style>
