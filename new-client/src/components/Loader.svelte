<script lang="ts">
  import { onDestroy, onMount } from 'svelte';

  export let isSmall: boolean = false;
  export let isWhite: boolean = false;

  let loaderSymbols = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'];
  let symbol: string = '⚀';
  let symbolSelector: number;

  onMount(() => {
    symbolSelector = setInterval(() => {
      symbol = loaderSymbols[Math.floor(Math.random() * loaderSymbols.length)];
    }, 350);
  });

  onDestroy(() => {
    clearInterval(symbolSelector);
  });
</script>

<div class="loader">
  <p class={`loader__character ${isSmall && '--small'} ${isWhite && '--white'}`}>
    {symbol}
  </p>
</div>

<style lang="scss">
  .loader {
    display: flex;
    justify-content: center;
    width: auto;
    margin: 75px 25px;

    &__character {
      font-size: 68px;
      color: #42b883;
      margin: 0;

      &.--small {
        font-size: 24px;
      }

      &.--small {
        color: #fff;
      }
    }
  }
</style>
