<div class="cheat-sheets">
  <nav class="navigation">
    <a class="button navigation__button" href="/">Home</a>
    <a class="button navigation__button" href="/cheat-sheets">Cheet sheets</a>
    <a class="button navigation__button" href="/about">About</a>
  </nav>
  <slot />
</div>

<style lang="scss">
  .cheat-sheets {
    display: flex;
    flex-direction: column;
    width: calc(100% - 10px);
    max-width: 800px;
    padding: 10px;
    margin: 0 auto;
  }

  .navigation {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    width: auto;
    margin: 10px 10px 35px 10px;

    &__button {
      margin: 10px;
    }
  }
</style>
